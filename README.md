SignaPlus
**Automated Multi-Format Document Signer & Organizer**

SignaPlus is a Python-based desktop utility that automates the placement of digital signatures on **PDF, DOCX, and XLSX** files. Designed for professionals who handle high-volume paperwork, it eliminates manual editing by watching a folder and signing documents the moment they arrive.



Key Features
* **Intelligent Scanning:** Specifically targets the *last* mention of a name to ensure the signature lands on the signatory line, not the header.
* **Multi-Format Support:** Handles `.pdf`, `.docx`, and `.xlsx` natively.
* **Browser-Style UI:** A clean, real-time activity manager to track success/fail states of processed files.
* **Daily Organization:** Automatically sorts signed documents into date-stamped folders (`YYYY-MM-DD`).
* **Portable & User-Friendly:** Generates its own config files and desktop shortcuts on the first run.
* **Privacy First:** Processes everything locally on your machine. No documents are uploaded to the cloud.

Getting Started

### Prerequisites
* Python 3.8+
* Pip (Python package manager)

### Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/4-ja/SignaPlus.git](https://github.com/4-ja/SignaPlus.git)
   cd SignaPlus
   
2. Install dependencies:
    Bash
    pip install watchdog pymupdf python-docx openpyxl pystray Pillow winshell pypiwin32
    🛠️ Usage
    Run the script: python smart_signer.py
    
    First Run: The app will create three folders: To_Be_Signed, My_Signature, and Signed_Documents.
    
    Setup: * Place your signature PNG in the My_Signature folder.
    
    Open settings.txt and update NAME_TO_SIGN with your full name.
    
    Sign: Drop any file into To_Be_Signed. The signed version will appear in Signed_Documents instantly.


Building the Executable
To create a standalone .exe for Windows:

Bash
pyinstaller --onefile --windowed --icon="icon.ico" --hidden-import="winshell" --hidden-import="pythoncom" smart_signer.py

👤 Author
JL (4JA) - Lead Developer

---

   
