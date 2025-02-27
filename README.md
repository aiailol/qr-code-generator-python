=============================
QR code Generator on Python
=============================

Generate QR codes.

A standard install uses pypng_ to generate PNG files and can also render QR
codes directly to the console. A standard install is just::

    pip install qrcode

For more image functionality, install qrcode with the ``pil`` dependency so
that pillow_ is installed and can be used for generating images::

    pip install "qrcode[pil]"


Usage
=====

Running the Script
To generate a QR code, run the script from the command line:

    python qr_generator.py


Generating a QR Code
Once the script is running, follow the prompts:

Enter the text or link you want to convert into a QR code.
Enter a filename (without the .png extension).
The generated QR code will be saved in the examples/ folder.

Example:

    Enter text or link (or 'exit' to quit): https://example.com  
    Enter filename (without extension): example_qr  
    QR code saved: examples/example_qr.png  

Using in Python
--------------

You can also generate QR codes directly in your Python code using the provided function:

.. code:: python

    from qr_generator import generate_qr  
    generate_qr("https://example.com", "examples/example_qr.png")
