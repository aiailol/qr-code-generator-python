import qrcode
import os

def generate_qr(data, filename="qr_code.png"):
    """Generate QR code and save it in the 'examples' folder"""
    
    save_path = os.path.join(os.path.dirname(__file__), "examples")
    os.makedirs(save_path, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    file_path = os.path.join(save_path, filename)
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_path)

    print(f"QR code saved: {file_path}")

if __name__ == "__main__":
    while True:
        url = input("Enter text or link (or 'exit' to quit): ").strip()
        if url.lower() == "exit":
            break
        if not url:
            print("Input cannot be empty. Please enter valid text or link.")
            continue

        filename = input("Enter filename (without extension): ").strip() or "qr_code"
        try:
            generate_qr(url, filename + ".png")
        except Exception as e:
            print(f"An error occurred: {e}")