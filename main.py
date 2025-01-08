# Python libraries
import sys

# Qt libraries
from PySide6.QtCore import Qt, QTimer, QThread, QMutex, Signal
from PySide6.QtGui import QPainter, QColor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Qt UI & Resource
from main_window import Ui_MainWindow
import resource_rc

# Custom libraries
from modules.delta_plc_modbus import ModbusASCII

class CoilReadMonitorThread(QThread):
    """
    A QThread that continuously reads a coil (or discrete inputs) from a Modbus device.
    It uses a QMutex to ensure thread-safe access to the shared modbus object.
    """
    updated_coil_state = Signal(list)  # Signal to emit the coil state (a list of 0/1).

    def __init__(self, modbus, modbus_lock, params, parent=None):
        """
        :param modbus: The shared ModbusASCII object.
        :param modbus_lock: A QMutex to protect modbus access.
        :param params: Dictionary containing read parameters (e.g., COIL_NAME, SLAVE_ADDRESS, COUNT).
        """
        super().__init__(parent)
        self.modbus = modbus
        self.modbus_lock = modbus_lock
        self.params = params
        self._running = True  # Controls the while loop in run().

    def run(self):
        """
        Continuously read from modbus at a fixed interval (0.5s).
        """
        while self._running:
            try:
                # Use QMutex to lock/unlock explicitly.
                self.modbus_lock.lock()
                try:
                    response = self.modbus.read_discrete_inputs(self.params)
                finally:
                    self.modbus_lock.unlock()

                coil_values = self.modbus.decode_discrete_inputs_response(response)
                if coil_values is not None:
                    self.updated_coil_state.emit(coil_values)
                else:
                    print("Warning: read_coil response is None or empty.")

            except Exception as e:
                print(f"Error in CoilReadMonitorThread: {e}")

            # Sleep for 0.5 seconds to avoid hammering the device.
            self.msleep(500)

    def stop(self):
        """
        Stops the thread gracefully by breaking the while loop.
        """
        self._running = False


class MainWindow(QMainWindow):
    """
    Main application window demonstrating:
      - Single-threaded Modbus write operations (with QTimer for periodic writes).
      - Multi-threaded continuous read operations via QThread.
      - Thread-safe modbus access with a QMutex.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove the title bar (frameless window)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Enable a transparent background
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Initialize the stacked widget to the first page
        self.ui.stackedWidget.setCurrentIndex(0)

        # Page switch buttons
        self.ui.pushButton_singleTestPage.clicked.connect(lambda: self.switch_page(0))
        self.ui.pushButton_multiTestPage.clicked.connect(lambda: self.switch_page(1))
        self.ui.pushButton_monitorPage.clicked.connect(lambda: self.switch_page(2))

        # Record variables
        self.modbus = None
        self.selected_port = None
        self.selected_slave_id = None
        self.side_menu_visible = True

        # QTimer for periodic write coil operations
        self.timer = QTimer(self)
        self.monitor_connection = None

        # Track drag position for window movement
        self._drag_position = None

        # A QThread for continuously reading coils
        self.coil_read_thread = None

        # Use QMutex for thread-safe modbus operations
        self.modbus_lock = QMutex()

        # Populate available COM ports
        com_ports = ModbusASCII.get_com_ports()
        if com_ports:
            self.ui.comboBox_comport.addItems(com_ports)
        else:
            QMessageBox.warning(self, "Error", "No COM ports available on this system.")

        # Get default slave ID from UI
        self.selected_slave_id = self.ui.comboBox_slaveID.currentText()

        # Attempt initial connection to the selected port
        self.update_selected_port()

        # Connect UI signals
        # Header
        self.ui.pushButton_closeApp.clicked.connect(self.close_application)
        self.ui.pushButton_minimizeApp.clicked.connect(self.minimize_application)
        self.ui.pushButton_menu.clicked.connect(self.toggle_side_menu)

        # Single Page
        self.ui.pushButton_excuteSingle.clicked.connect(self.singleTestPage_excute)

        # CheckBox signals
        self.ui.checkBox_writeCoil.stateChanged.connect(self.update_selection)
        self.ui.checkBox_writeRegister.stateChanged.connect(self.update_selection)
        self.ui.checkBox_readCoil.stateChanged.connect(self.update_selection)
        self.ui.checkBox_readRegister.stateChanged.connect(self.update_selection)

        # ComboBox signals
        self.ui.comboBox_comport.currentIndexChanged.connect(self.update_selected_port)
        self.ui.comboBox_slaveID.currentIndexChanged.connect(self.update_selected_slave_id)

        # Multi Page
        self.ui.pushButton_excuteMultiCoil.clicked.connect(
            lambda: self.execute_write_multiple_coils(int(self.selected_slave_id))
        )
        self.ui.pushButton_excuteMultiRegister.clicked.connect(
            lambda: self.execute_write_multiple_registers(int(self.selected_slave_id))
        )

        # Monitor Page
        # Periodic coil write (QTimer)
        self.ui.pushButton_excuteMonitorCoil.clicked.connect(
            lambda: self.execute_write_monitor_coil(int(self.selected_slave_id))
        )
        self.ui.pushButton_cancelMonitorCoil.clicked.connect(self.stop_monitor)

        # Continuous coil read (QThread)
        self.ui.pushButton_excuteMonitorCoilState.clicked.connect(
            lambda: self.start_read_monitor_coil(int(self.selected_slave_id))
        )
        self.ui.pushButton_cancelMonitorCoilState.clicked.connect(self.stop_read_monitor_coil)

    # -------------------- Window Movement & Painting --------------------
    def mousePressEvent(self, event):
        """
        Record the initial mouse position for dragging a frameless window.
        """
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """
        Enable window dragging when left mouse button is held.
        """
        if event.buttons() == Qt.LeftButton and self._drag_position is not None:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """
        Reset drag position after mouse release.
        """
        if event.button() == Qt.LeftButton:
            self._drag_position = None
            event.accept()

    def paintEvent(self, event):
        """
        Optional painting logic for a transparent background.
        """
        painter = QPainter(self)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    # -------------------- Window Closing & Minimizing --------------------
    def close_application(self):
        """
        Close the application via button press.
        """
        QApplication.quit()

    def minimize_application(self):
        """
        Minimize the application via button press.
        """
        self.showMinimized()

    # -------------------- Single Page --------------------
    def singleTestPage_excute(self):
        """
        Execute a single operation (read/write coil/register) based on which CheckBox is selected.
        """
        slave_id = int(self.selected_slave_id)
        mode = self.get_current_mode()

        if mode == "write_coil":
            self.execute_write_coil(slave_id)
        elif mode == "write_register":
            self.execute_write_register(slave_id)
        elif mode == "read_coil":
            self.execute_read_coil(slave_id)
        elif mode == "read_register":
            self.execute_read_register(slave_id)
        else:
            QMessageBox.warning(self, "Error", "No mode selected. Please check a mode.")

    def get_current_mode(self):
        """
        Determine which operation is currently selected (via the CheckBox states).
        """
        if self.ui.checkBox_writeCoil.isChecked():
            return "write_coil"
        elif self.ui.checkBox_writeRegister.isChecked():
            return "write_register"
        elif self.ui.checkBox_readCoil.isChecked():
            return "read_coil"
        elif self.ui.checkBox_readRegister.isChecked():
            return "read_register"
        return None

    def execute_write_coil(self, slave_id):
        """
        Write a single coil.
        """
        self.ui.textBrowser_singleResponse.clear()
        self.ui.textBrowser_prase.clear()

        coil_name = self.ui.comboBox_writeCoilName.currentText()
        coil_number = self.ui.lineEdit_writeCoilNumber.text().strip()
        if not coil_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid coil number. Must be numeric.")
            return

        coil_state_str = self.ui.lineEdit_singleExcute.text().strip()
        try:
            coil_state = int(coil_state_str)
            if coil_state not in [0, 1]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coil state. Must be 0 or 1.")
            return

        full_coil_name = f"{coil_name}{coil_number}"
        params = {
            "COIL_NAME": full_coil_name,
            "STATE": coil_state,
            "SLAVE_ADDRESS": slave_id
        }

        # Lock/Unlock via QMutex
        self.modbus_lock.lock()
        try:
            response = self.modbus.write_coil(params)
        finally:
            self.modbus_lock.unlock()

        if response:
            self.ui.textBrowser_singleResponse.append(f"Response: {response}")
        else:
            self.ui.textBrowser_singleResponse.append(
                f"Error: Failed to write to coil {full_coil_name}."
            )

    def execute_write_register(self, slave_id):
        """
        Write a single register.
        """
        self.ui.textBrowser_singleResponse.clear()
        self.ui.textBrowser_prase.clear()

        register_name = self.ui.comboBox_writeRegisterName.currentText()
        register_number = self.ui.lineEdit_writeRegisterNumber.text().strip()
        if not register_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid register number. Must be numeric.")
            return

        full_register_name = f"{register_name}{register_number}"
        register_value_str = self.ui.lineEdit_singleExcute.text().strip()
        try:
            register_value = int(register_value_str)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid register value. Must be numeric.")
            return

        params = {
            "REGISTER_ADDRESS": full_register_name,
            "VALUE": register_value,
            "SLAVE_ADDRESS": slave_id
        }

        self.modbus_lock.lock()
        try:
            response = self.modbus.write_register(params)
        finally:
            self.modbus_lock.unlock()

        if response:
            self.ui.textBrowser_singleResponse.append(f"Response: {response}")
        else:
            self.ui.textBrowser_singleResponse.append(
                f"Error: Failed to write to register {full_register_name}."
            )

    def execute_read_coil(self, slave_id):
        """
        Read one or more coils (discrete inputs).
        """
        self.ui.textBrowser_singleResponse.clear()
        self.ui.textBrowser_prase.clear()

        coil_name = self.ui.comboBox_readCoilName.currentText()
        coil_number = self.ui.lineEdit_readCoilNumber.text().strip()
        full_coil_name = f"{coil_name}{coil_number}"

        coil_count_str = self.ui.lineEdit_singleExcute.text().strip()
        try:
            coil_count = int(coil_count_str)
            if coil_count <= 0 or coil_count > 2000:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coil count. Must be 1-2000.")
            return

        params = {
            "COIL_NAME": full_coil_name,
            "SLAVE_ADDRESS": slave_id,
            "COUNT": coil_count
        }

        self.modbus_lock.lock()
        try:
            response = self.modbus.read_discrete_inputs(params)
        finally:
            self.modbus_lock.unlock()

        parsed_response = self.modbus.decode_discrete_inputs_response(response)
        if response:
            self.ui.textBrowser_singleResponse.append(f"Response: {response}")
            self.ui.textBrowser_prase.append(f"Prase: {parsed_response}")
        else:
            self.ui.textBrowser_singleResponse.append(
                f"Error: Failed to read coil {full_coil_name}."
            )

    def execute_read_register(self, slave_id):
        """
        Read one or more holding registers.
        """
        self.ui.textBrowser_singleResponse.clear()
        self.ui.textBrowser_prase.clear()

        register_name = self.ui.comboBox_readRegisterName.currentText()
        register_number = self.ui.lineEdit_readRegisterNumber.text().strip()
        if not register_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid register number. Must be numeric.")
            return

        full_register_name = f"{register_name}{register_number}"

        register_count_str = self.ui.lineEdit_singleExcute.text().strip()
        try:
            register_count = int(register_count_str)
            if register_count <= 0 or register_count > 125:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid register count. Must be 1-125.")
            return

        params = {
            "REGISTER_NAME": full_register_name,
            "SLAVE_ADDRESS": slave_id,
            "COUNT": register_count
        }

        self.modbus_lock.lock()
        try:
            response = self.modbus.read_registers(params)
        finally:
            self.modbus_lock.unlock()

        parsed_response = self.modbus.decode_registers_response(response)
        if response:
            self.ui.textBrowser_singleResponse.append(f"Response: {response}")
            self.ui.textBrowser_prase.append(f"Prase: {parsed_response}")
        else:
            self.ui.textBrowser_singleResponse.append(
                f"Error: Failed to read register {full_register_name}."
            )

    # -------------------- Update CheckBoxes --------------------
    def update_selection(self):
        """
        Ensure only one CheckBox is checked at a time.
        """
        sender = self.sender()
        all_checkboxes = [
            self.ui.checkBox_writeCoil,
            self.ui.checkBox_writeRegister,
            self.ui.checkBox_readCoil,
            self.ui.checkBox_readRegister,
        ]
        for checkbox in all_checkboxes:
            if checkbox != sender:
                checkbox.blockSignals(True)
                checkbox.setChecked(False)
                checkbox.blockSignals(False)

    # -------------------- Update Port & Slave ID --------------------
    def update_selected_port(self):
        """
        Connect or reconnect to the selected COM port with QMutex locking.
        """
        self.selected_port = self.ui.comboBox_comport.currentText()

        if self.modbus and self.modbus.serial_connection and self.modbus.serial_connection.is_open:
            try:
                self.modbus.disconnect()
            except Exception as e:
                print(f"Error closing serial connection: {e}")

        try:
            if not self.selected_port:
                QMessageBox.warning(self, "Error", "Please select a COM port.")
                return

            self.modbus = ModbusASCII(port=self.selected_port)
            self.modbus_lock.lock()
            try:
                if not self.modbus.connect():
                    QMessageBox.critical(self, "Connection Failed", f"Failed to connect to {self.selected_port}.")
                    return
            finally:
                self.modbus_lock.unlock()

        except Exception as e:
            print(f"Error connecting to new port: {e}")

    def update_selected_slave_id(self):
        """
        Retrieve the current Slave ID from the UI.
        """
        self.selected_slave_id = self.ui.comboBox_slaveID.currentText()

    # -------------------- Page Switching --------------------
    def switch_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    # -------------------- Multi Page --------------------
    def execute_write_multiple_coils(self, slave_id):
        """
        Write multiple coils at once.
        """
        self.ui.textBrowser_multiResponse.clear()

        coil_name = self.ui.comboBox_writeMultiCoilName.currentText()
        coil_number = self.ui.lineEdit_writeMultiCoilNumber.text().strip()
        if not coil_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid coil number. Must be numeric.")
            return

        coil_states_input = self.ui.lineEdit_excuteMultiCoil.text().strip()
        coil_states = [int(c) for c in coil_states_input]

        start_address = f"{coil_name}{coil_number}"
        params = {
            "SLAVE_ADDRESS": slave_id,
            "START_ADDRESS": start_address,
            "COIL_STATES": coil_states,
        }

        self.modbus_lock.lock()
        try:
            response = self.modbus.write_multiple_coils(params)
        finally:
            self.modbus_lock.unlock()

        if response:
            self.ui.textBrowser_multiResponse.append(f"Response: {response}")
        else:
            self.ui.textBrowser_multiResponse.append(
                f"Error: Failed to write multiple coils starting at {start_address}."
            )

    def execute_write_multiple_registers(self, slave_id):
        """
        Write multiple registers at once.
        """
        self.ui.textBrowser_multiResponse.clear()

        register_name = self.ui.comboBox_writeMultiRegisterName.currentText()
        register_number = self.ui.lineEdit_writeMultiRegisterNumber.text().strip()
        if not register_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid register number. Must be numeric.")
            return

        values_input = self.ui.lineEdit_excuteMultiRegister.text().strip()
        try:
            values = [int(v.strip()) for v in values_input.split(",")]
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid values. Must be comma-separated integers.")
            return

        start_address = f"{register_name}{register_number}"
        params = {
            "SLAVE_ADDRESS": slave_id,
            "START_ADDRESS": start_address,
            "VALUES": values,
        }

        self.modbus_lock.lock()
        try:
            response = self.modbus.write_multiple_registers(params)
        finally:
            self.modbus_lock.unlock()

        if response:
            self.ui.textBrowser_multiResponse.append(f"Response: {response}")
        else:
            self.ui.textBrowser_multiResponse.append(
                f"Error: Failed to write multiple registers starting at {start_address}."
            )

    # -------------------- Monitor Page: Write Coil (QTimer) --------------------
    def execute_write_monitor_coil(self, slave_id):
        """
        Use QTimer to periodically write a coil with a specified interval (seconds).
        """
        coil_name = self.ui.comboBox_writeMonitorCoilName.currentText()
        coil_number = self.ui.lineEdit_writeMonitorCoilNumber.text().strip()
        interval_str = self.ui.lineEdit_writeMonitorCoilInterval.text().strip()

        try:
            interval = int(interval_str)
        except ValueError:
            QMessageBox.warning(self, "Error", "Interval must be an integer.")
            return

        if not coil_number.isdigit():
            QMessageBox.warning(self, "Error", "Invalid coil number. Must be numeric.")
            return

        coil_state_str = self.ui.lineEdit_excuteMonitorCoil.text().strip()
        try:
            coil_state = int(coil_state_str)
            if coil_state not in [0, 1]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coil state. Must be 0 or 1.")
            return

        start_address = f"{coil_name}{coil_number}"
        params = {
            "SLAVE_ADDRESS": slave_id,
            "COIL_NAME": start_address,
            "STATE": coil_state,
        }

        # Cancel previous connection if any
        if self.monitor_connection is not None:
            self.timer.timeout.disconnect(self.monitor_connection)
            self.monitor_connection = None

        self.monitor_connection = self.timer.timeout.connect(
            lambda: self.write_coil_monitor(params)
        )
        self.timer.start(interval * 1000)

    def stop_monitor(self):
        """
        Stop the periodic coil writing timer if active.
        """
        if self.monitor_connection is not None:
            self.timer.timeout.disconnect(self.monitor_connection)
            self.monitor_connection = None
        self.timer.stop()

    def write_coil_monitor(self, params):
        """
        Periodically called by QTimer to write a coil.
        """
        if (not self.modbus or
                not self.modbus.serial_connection or
                not self.modbus.serial_connection.is_open):
            return

        self.modbus_lock.lock()
        try:
            response = self.modbus.write_coil(params)
        finally:
            self.modbus_lock.unlock()

        if not response:
            QMessageBox.critical(self, "Error", "Failed to write coil. Monitoring stopped.")
            self.stop_monitor()

    # -------------------- Monitor Page: Read Coil (QThread) --------------------
    def start_read_monitor_coil(self, slave_id):
        """
        Start a QThread (CoilReadMonitorThread) to continuously read coils.
        """
        if self.coil_read_thread and self.coil_read_thread.isRunning():
            QMessageBox.warning(self, "Warning", "Read monitor is already running.")
            return

        coil_name = self.ui.comboBox_readMonitorCoilName.currentText()
        coil_number = self.ui.lineEdit_readMonitorCoilNumber.text().strip()
        coil_count_str = self.ui.lineEdit_excuteMonitorCoilState.text().strip()

        if not coil_number.isdigit():
            QMessageBox.warning(self, "Error", "Coil number must be numeric.")
            return

        try:
            coil_count = int(coil_count_str)
            if coil_count <= 0 or coil_count > 2000:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid coil count. Must be 1-2000.")
            return

        coil_address = f"{coil_name}{coil_number}"
        params = {
            "COIL_NAME": coil_address,
            "SLAVE_ADDRESS": slave_id,
            "COUNT": coil_count
        }

        # Create and start the QThread for continuous reading
        self.coil_read_thread = CoilReadMonitorThread(
            modbus=self.modbus,
            modbus_lock=self.modbus_lock,
            params=params
        )
        self.coil_read_thread.updated_coil_state.connect(self.on_coil_state_updated)
        self.coil_read_thread.start()

        print("Coil read monitor thread started.")

    def stop_read_monitor_coil(self):
        """
        Stop the coil read thread if it is running.
        """
        if self.coil_read_thread and self.coil_read_thread.isRunning():
            self.coil_read_thread.stop()
            self.coil_read_thread.wait()
            self.coil_read_thread = None
            print("Coil read monitor thread stopped.")
        else:
            print("No coil read monitor thread is running.")

    def on_coil_state_updated(self, state_list):
        """
        Slot called when the coil read thread emits updated_coil_state.
        """
        self.ui.textBrowser_monitorResponse.clear()
        self.ui.textBrowser_monitorResponse.append(f"Read: {state_list}")

    # -------------------- Close App --------------------
    def closeEvent(self, event):
        """
        Ensure all monitors are stopped before closing the application.
        """
        self.stop_monitor()
        self.stop_read_monitor_coil()
        super().closeEvent(event)

    # -------------------- Hide side bar  --------------------
    def toggle_side_menu(self): 
        self.side_menu_visible = not self.side_menu_visible 
        self.ui.side_menu.setVisible(self.side_menu_visible)

        if self.side_menu_visible:
            self.ui.pushButton_menu.setIcon(QIcon(":/ICONS/resource/ICONS/arrow-right-circle.svg"))
        else:
            self.ui.pushButton_menu.setIcon(QIcon(":/ICONS/resource/ICONS/arrow-left-circle.svg"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
