from setuptools import setup, find_packages

setup(
    name="qr_generator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "qrcode[pil]"
    ],
    entry_points={
        "console_scripts": [
            "qrgen=qr_generator.generator:generate_qr",
        ],
    },
    author="aiailol",
    description="A simple QR code generator",
    url="https://github.com/yourusername/qr-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
