# Python Libery
import sys
from pathlib import Path
# Custom Libery
sys.path.append(str(Path(__file__).parent.parent / "modules"))
from delta_plc_modbus import ModbusASCII

modbus = ModbusASCII(port="COM4")

params = {
    "SLAVE_ADDRESS": 1,
    "START_ADDRESS": "M001",  # Starting address for coils
    "COIL_STATES": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # States for M001 ~ M008
}

response = modbus.write_multiple_coils(params)
if response:
    print(f"Response: {response}")
else:
    print("Failed to write multiple coils.")

params = {
    "SLAVE_ADDRESS": 1,
    "START_ADDRESS": "D410",  # Starting address for registers
    "VALUES": [111, 112, 113, 114]  # Values to write into D410 ~ D413
}

response = modbus.write_multiple_registers(params)
if response:
    print(f"Response: {response}")
else:
    print("Failed to write multiple registers.")