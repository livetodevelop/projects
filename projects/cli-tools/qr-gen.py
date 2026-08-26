#!/usr/bin/env python3
"""generates qr codes from text or urls"""

import argparse
import qrcode

def generate_qr(data, filename="qrcode.png"):
    """generates a qr code and saves it"""
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    
    print(f"qr code saved to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate qr codes")
    parser.add_argument("data", help="text or url to encode")
    parser.add_argument("--output", "-o", default="qrcode.png",
                        help="output filename")
    
    args = parser.parse_args()
    
    generate_qr(args.data, args.output)
