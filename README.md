# Python_DeltaPLC_Communication

基於 Python 和 PySide6 的專案，用於與台達 PLC (Delta PLC) 進行 Modbus 通信，並結合圖形化界面進行操作。

---

## 專案目錄結構

```plaintext
Python_DeltaPLC_Communication/
├── modules/                      # 自訂義模組
│   ├── delta_plc_modbus.py       # Modbus 通信模組
├── plc/                          # PLC 程式碼
│   ├── Practice_V1_20241226.dvp  # PLC 步階圖程式碼
├── tests/                        # 單元測試
│   ├── ModbusASCII_Multi_Test.py
│   ├── ModbusASCII_Single_Test.py
├── main.py                       # 主程序入口
├── requirements.txt              # 需要的庫
├── main_window.py                # 主界面設計文件
└── resource_rc.py                # 編譯後的資源文件
```

---
## 功能特性
- Modbus 通信：支援 Modbus ASCII 和 Modbus RTU 協議。
- 圖形化界面：使用 PySide6 提供直觀的操作界面。
- PLC 支援：適配台達 PLC，支持參數讀取與即時控制(結合多執行緒)。
- 單元測試：提供測試模組，確保通信可靠性。

---
聯絡方式
如果有問題，請通過以下方式聯繫我：

Email: achieve8822@gmail.com
