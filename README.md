# Caesar Cipher Tool

Caesar Cipher implementation with both GUI and command-line interfaces for encrypting and decrypting text and files.

## Installation Options

1. **Pre-built Executable**:
   - Download `CaesarCipher.exe` from the releases section
   - No Python installation required
   - Just double-click to run

2. **From Source**:
   - Clone the repository
   - Ensure you have Python 3.6 or higher installed
   - No additional dependencies required (tkinter comes with Python)

## Required Files (For Source Installation)
- `CaesarCipher.py` - Core encryption/decryption functionality
- `CaesarCipherUI.py` - Graphical user interface

## Usage

### Graphical Interface
1. Run the GUI:
   ```
   python CaesarCipherUI.py
   ```
2. Use the tabs to switch between string and file encryption
3. Enter text or select files to process
4. Choose encrypt/decrypt and set shift value (1-99)
5. Click "Process" button to see results

### Command Line Interface
1. Run the CLI:
   ```
   python CaesarCipher.py
   ```
2. Follow the interactive menu options

## Features
- String encryption and decryption
- File and folder processing
- Custom shift values (1-99)
- Supports letters, numbers, and special characters
- Preserves formatting and line breaks
- Copy to clipboard functionality
- Real-time processing

## Important Notes
- Remember your shift value - you need it for decryption
- Files are modified in place - backup important files
- Default shift value is 5
- Not recommended for sensitive data

## Creating Executable
To create a standalone .exe:
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Create the executable:
   ```
   python -m PyInstaller --onefile --windowed CaesarCipherUI.py
   ```
3. Find the executable in the `dist` folder

## License
This project is open source under the MIT License.

## Support
Create an issue in the GitHub repository for:
- Bug reports
- Feature requests
- Questions 