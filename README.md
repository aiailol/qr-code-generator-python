QR Code Generator 📷🔳
A simple Python-based QR code generator that allows you to create QR codes for any text or link and automatically saves them in the examples/ folder.

📌 Features
✔️ Generates QR codes from text or URLs
✔️ Saves generated QR codes in the examples/ folder
✔️ Supports custom file names for QR codes
✔️ Automatically creates the output directory if it doesn't exist

🚀 Installation
1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/qr-generator.git
cd qr-generator

2️⃣ Install Dependencies
Ensure you have Python 3.6+ installed. Then, install the required package:

pip install -r requirements.txt
If you don't have pip installed, install it first:

python -m ensurepip --default-pip

🛠️ Usage
📌 Run the Script

python qr_generator.py

🔹 Generate QR Codes
Enter the text or link you want to convert into a QR code.
Enter a filename (without .png extension).
The QR code will be saved in the examples/ folder.
Example:

Enter text or link (or 'exit' to quit): https://example.com
Enter filename (without extension): example_qr
QR code saved: examples/example_qr.png
