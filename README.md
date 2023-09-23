# 🖥️ Windows Stick Maker on Mac (WSMOM)

It's like Windows Media Creation Tool, but for Mac.

WSMOM is a utility that allows users to create a Windows 11 bootable USB installer, on a Mac, for installing on a PC. Say goodbye to complicated workarounds; with WSMOM, setting up a Windows 11 installation USB on your Mac is a breeze.

## 🔧 Requirements

Ensure you meet the following prerequisites:

- **USB Drive**: 
  - FAT-formatted
  - At least 8GB of storage
  
- **Software & Libraries**:
  - [Homebrew](https://brew.sh/)
    - `wimlib`: Install using `brew install wimlib`
  - Python module:
    - `pycdlib`: Install using `pip3 install pycdlib`
    
- **Python Version**: 
  - Tested on `Python 3.11.5 64-bit`. It might work on earlier versions, but this version is recommended.

## 🚀 Usage

1. **Setup**: 
   - Place `wsmom.py` in the same directory as your Windows 11 ISO.

2. **Run the Script**:
   - Navigate to the directory in a terminal.
   - Execute the script using:
     ```bash
     python3 wsmom.py
     ```

3. **Copy the files from `usb_files` to your USB stick**:
   - After the script completes, copy the files from the `usb_files` directory:
     ```bash
     cp -r /path/to/usb_files/ /Volumes/USB_DRIVE_NAME/
     ```
   - **Note**: Replace the placeholder paths (`/path/to/usb_files/` and `USB_DRIVE_NAME`) with your specific details.

4. **Boot from the USB**
