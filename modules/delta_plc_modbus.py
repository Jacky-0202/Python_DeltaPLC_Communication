import serial
import serial.tools.list_ports

class ModbusASCII:
    """
    A class to handle Modbus ASCII communication with a PLC.
    """

    def __init__(self, port, baudrate=9600, stopbits=1, bytesize=7, parity="E"):
        """
        Initialize serial communication parameters.
        """
        self.port = port
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.parity = parity
        self.serial_connection = None

    @staticmethod
    def get_com_ports():
        """
        Static method to list all available COM ports on the system.
        """
        ports = serial.tools.list_ports.comports()
        com_ports = [port.device for port in ports]
        sorted_ports = sorted(com_ports, key=lambda x: int(x[3:]))
        return sorted_ports

    def connect(self):
        """
        Establish a connection to the PLC using the serial port.
        """
        if self.serial_connection and self.serial_connection.is_open:
            return True  # Avoid reconnecting if already open
        try:
            # Initialize the serial connection
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=self.bytesize,
                parity=self.parity,
                stopbits=self.stopbits,
                timeout=1  # Set a timeout for the connection
            )
            if self.serial_connection.is_open:
                return True
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.serial_connection = None
            return False

    def disconnect(self):
        """
        Close the connection to the PLC if it is open.
        """
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.close()
                print("Serial connection closed.")
            except Exception as e:
                print(f"Error closing serial connection: {e}")
        else:
            print("No open serial connection to close.")
        self.serial_connection = None

    def build_modbus_message(self, slave_address, function_code, start_address, data):
        """
        Build a Modbus ASCII message.
        """
        message = [
            slave_address,                  # Slave address
            function_code,                  # Function code
            (start_address >> 8) & 0xFF,    # High byte of the start address
            start_address & 0xFF,           # Low byte of the start address
            (data >> 8) & 0xFF,             # High byte of the data
            data & 0xFF                     # Low byte of the data
        ]
        lrc = self.calculate_lrc(message)
        message.append(lrc)  # Append LRC
        return ":" + "".join(f"{byte:02X}" for byte in message) + "\r\n"

    def calculate_lrc(self, data):
        """
        Calculate the Longitudinal Redundancy Check (LRC) for a Modbus ASCII message.
        """
        lrc = 0
        for byte in data:
            lrc += byte  # Sum all bytes
        lrc &= 0xFF  # Keep only the lower 8 bits

        # Take the 2's complement explicitly
        lrc = ~lrc & 0xFF  # Take bitwise negation and keep lower 8 bits
        lrc = (lrc + 1) & 0xFF  # Add 1 and keep lower 8 bits
        return lrc

    def map_device_to_address(self, device_name):
        """
        Map a device name (e.g., M600) to its corresponding Modbus address.
        """
        if device_name.startswith("S"):
            base_address = 0
            offset = int(device_name[1:])
            if 0 <= offset <= 255:
                return base_address + offset
            else:
                raise ValueError("Invalid S range. Must be between S000-S255.")
        elif device_name.startswith("X"):
            base_address = 1024
            offset = int(device_name[1:], 8)
            if 0 <= offset <= 377:
                return base_address + offset
            else:
                raise ValueError("Invalid X range. Must be between X000-X377.")
        elif device_name.startswith("Y"):
            base_address = 1280
            offset = int(device_name[1:], 8)
            if 0 <= offset <= 377:
                return base_address + offset
            else:
                raise ValueError("Invalid Y range. Must be between Y000-Y377.")
        elif device_name.startswith("T"):
            base_address = 1536
            offset = int(device_name[1:])
            if 0 <= offset <= 255:
                return base_address + offset
            else:
                raise ValueError("Invalid T range. Must be between T000-T255.")
        elif device_name.startswith("M"):
            offset = int(device_name[1:])
            if 0 <= offset <= 1535:
                base_address = 2048
            elif 1536 <= offset <= 4095:
                base_address = 45057
            else:
                raise ValueError("Invalid M range. Must be between M000-M4095.")
            return base_address + offset
        elif device_name.startswith("D"):
            offset = int(device_name[1:])
            if 0 <= offset <= 1279:
                base_address = 4096
            elif 1280 <= offset <= 4095:
                base_address = 5376
            else:
                raise ValueError("Invalid D range. Must be between D000-D4095.")
            return base_address + offset
        elif device_name.startswith("C"):
            offset = int(device_name[1:])
            if 0 <= offset <= 199:
                base_address = 3584
                return base_address + offset
            elif 200 <= offset <= 255:
                base_address = 3784
                return base_address + (offset - 200)
            else:
                raise ValueError("Invalid C range. Must be between C000-C255.")
        else:
            raise ValueError(f"Unknown device type: {device_name}")

    def address_to_hex(self, address):
        """
        Convert a Modbus address to a 4-digit hexadecimal string.
        """
        if not (0 <= address <= 0xFFFF):
            raise ValueError("Address out of range. Must be between 0 and 65535.")
        return f"{address:04X}"

    def send_modbus_message(self, message):
        """
        Send a Modbus ASCII message via the serial port.
        """
        if not self.serial_connection or not self.serial_connection.is_open:
            print("No open connection. Establishing a new connection...")
            if not self.connect():
                print("Failed to establish connection.")
                return None
        try:
            self.serial_connection.write(message.encode('ascii'))
            response = self.serial_connection.readline().decode('ascii').strip()
            return response
        except Exception as e:
            print(f"Communication error: {e}")
            return None

    def write_coil(self, params):
        """
        Write a single coil (Function Code 05).
        """
        address = self.map_device_to_address(params["COIL_NAME"])
        force_data = 0xFF00 if params["STATE"] == 1 else 0x0000
        message = self.build_modbus_message(params["SLAVE_ADDRESS"], 5, address, force_data)

        return self.send_modbus_message(message)

    def read_discrete_inputs(self, params):
        """
        Read the status of discrete inputs (Function Code 02).
        """
        address = self.map_device_to_address(params["COIL_NAME"])
        count = params.get("COUNT", 1)
        if not (1 <= count <= 2000):
            raise ValueError("COUNT must be between 1 and 2000.")
        message = self.build_modbus_message(params["SLAVE_ADDRESS"], 2, address, count)
        return self.send_modbus_message(message)
    
    def decode_discrete_inputs_response(self, response):
        """
        Decode the response from reading discrete inputs (Function Code 02).
        """
        try:
            # Validate response length and structure
            if not response.startswith(":"):
                raise ValueError("Invalid response format.")
                
            # Convert ASCII to binary data
            response_data = bytes.fromhex(response[1:].strip("\r\n"))
                
                # Extract the relevant fields
            slave_address = response_data[0]
            function_code = response_data[1]
            byte_count = response_data[2]
            input_status = response_data[3:3 + byte_count]
            lrc = response_data[3 + byte_count]

            # Validate LRC
            if self.calculate_lrc(response_data[:-1]) != lrc:
                raise ValueError("LRC checksum mismatch.")

            # Decode input status
            status = []
            for byte in input_status:
                # Extract individual bits
                for bit in range(8):
                    status.append((byte >> bit) & 1)

            # Return the status of the requested points
            return status
        except Exception as e:
            print(f"Error parsing response: {e}")
            return None


    def read_registers(self, params):
        """
        Read the content of holding registers (Function Code 03).
        """
        address = self.map_device_to_address(params["REGISTER_NAME"])
        count = params.get("COUNT", 1)
        if not (1 <= count <= 125):
            raise ValueError("COUNT must be between 1 and 125.")
        message = self.build_modbus_message(params["SLAVE_ADDRESS"], 3, address, count)
        return self.send_modbus_message(message)

    def decode_registers_response(self, response):
        """
        Decode the response from reading holding registers (Function Code 03).
        """
        try:
            # Validate response format
            if not response.startswith(":"):
                raise ValueError("Invalid response format.")
            
            # Convert ASCII response to binary data
            response_data = bytes.fromhex(response[1:].strip("\r\n"))
            
            # Extract fields from the response
            slave_address = response_data[0]
            function_code = response_data[1]
            byte_count = response_data[2]
            register_values = response_data[3:3 + byte_count]
            lrc = response_data[3 + byte_count]
            
            # Validate LRC
            if self.calculate_lrc(response_data[:-1]) != lrc:
                raise ValueError("LRC checksum mismatch.")
            
            register_values = []
            for i in range(0, byte_count, 2):
                # Combine two bytes into a 16-bit register value
                register_value = (response_data[3 + i] << 8) | response_data[3 + i + 1]
                register_values.append(register_value)
            
            # Extract LRC and validate it
            lrc = response_data[3 + byte_count]
            if self.calculate_lrc(response_data[:-1]) != lrc:
                raise ValueError("LRC checksum mismatch.")
            
            # Return the list of register values
            return register_values
        except Exception as e:
            print(f"Error parsing response: {e}")
            return None

    def write_register(self, params):
        """
        Write a single holding register (Function Code 06).
        """
        address = self.map_device_to_address(params["REGISTER_ADDRESS"])
        value = params["VALUE"]
        message = self.build_modbus_message(params["SLAVE_ADDRESS"], 6, address, value)
        return self.send_modbus_message(message)
    
    def write_multiple_coils(self, params):
        """
        Write multiple coils (Function Code 15).
        """
        address = self.map_device_to_address(params["START_ADDRESS"])
        coil_states = params["COIL_STATES"]

        # Convert coil states to bytes
        byte_count = (len(coil_states) + 7) // 8  # Calculate byte count
        coil_data = bytearray(byte_count)
        for i, state in enumerate(coil_states):
            if state:
                coil_data[i // 8] |= (1 << (i % 8))

        message = [
            params["SLAVE_ADDRESS"],            # Slave address
            15,                                 # Function code
            (address >> 8) & 0xFF,              # High byte of start address
            address & 0xFF,                     # Low byte of start address
            (len(coil_states) >> 8) & 0xFF,     # High byte of quantity of coils
            len(coil_states) & 0xFF,            # Low byte of quantity of coils
            len(coil_data)                      # Byte count
        ] + list(coil_data)

        lrc = self.calculate_lrc(message)
        message.append(lrc)

        ascii_message = ":" + "".join(f"{byte:02X}" for byte in message) + "\r\n"
        return self.send_modbus_message(ascii_message)

    def write_multiple_registers(self, params):
        """
        Write multiple registers (Function Code 16).
        """
        address = self.map_device_to_address(params["START_ADDRESS"])
        register_values = params["VALUES"]

        # Convert register values to bytes
        byte_count = len(register_values) * 2
        register_data = bytearray()
        for value in register_values:
            register_data.append((value >> 8) & 0xFF)  # High byte
            register_data.append(value & 0xFF)        # Low byte

        message = [
            params["SLAVE_ADDRESS"],             # Slave address
            16,                                  # Function code
            (address >> 8) & 0xFF,               # High byte of start address
            address & 0xFF,                      # Low byte of start address
            (len(register_values) >> 8) & 0xFF,  # High byte of quantity of registers
            len(register_values) & 0xFF,         # Low byte of quantity of registers
            byte_count                           # Byte count
        ] + list(register_data)

        lrc = self.calculate_lrc(message)
        message.append(lrc)

        ascii_message = ":" + "".join(f"{byte:02X}" for byte in message) + "\r\n"
        return self.send_modbus_message(ascii_message)
