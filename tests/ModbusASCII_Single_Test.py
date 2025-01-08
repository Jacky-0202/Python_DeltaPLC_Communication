# Python Libery
import sys
from pathlib import Path
# Custom Libery
sys.path.append(str(Path(__file__).parent.parent / "modules"))
from delta_plc_modbus import ModbusASCII


# Initialize the ModbusASCII class
ports = ModbusASCII.get_com_ports()
print(ports)
modbus = ModbusASCII(port="COM4")

# Connect PLC
if modbus.connect():
    print("Connected to PLC.")

    # Write coil
    write_params = {"SLAVE_ADDRESS": 1, "COIL_NAME": "M520", "STATE": 1}
    response = modbus.write_coil(write_params)
    print(f"Write Coil Response: {response}")

    # Read status inputs
    read_params = {"SLAVE_ADDRESS": 1, "COIL_NAME": "M0", "COUNT": 5}
    response = modbus.read_discrete_inputs(read_params)
    bits = modbus.decode_discrete_inputs_response(response)
    print(f"Discrete Input Status: {response}")
    print(f"Decode Input Status: {bits}")

    # Read Registers
    read_register_params = {"SLAVE_ADDRESS": 1, "REGISTER_NAME": "D410", "COUNT": 8}
    response = modbus.read_registers(read_register_params)
    values = modbus.decode_registers_response(response)
    print(f"Holding Register Values: {response}")
    print(f"Decode Register Response: {values}")

    # Write Registers
    write_register_params = {"SLAVE_ADDRESS": 1, "REGISTER_ADDRESS": "D417", "VALUE": 8}
    response = modbus.write_register(write_register_params)
    print(f"Write Register Response: {response}")

    # Disconnect
    modbus.disconnect()
else:
    print("Failed to connect to PLC.")
