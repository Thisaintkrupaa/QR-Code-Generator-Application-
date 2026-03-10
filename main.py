import qrcode
import argparse
import os
import logging

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/app.log", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://github.com/kaw393939")
args = parser.parse_args()

os.makedirs("qr_codes", exist_ok=True)
img = qrcode.make(args.url)
filename = f"qr_codes/qr_{args.url.replace('https://','').replace('http://','').replace('/','_')}.png"
img.save(filename)

logging.info(f"QR code generated for {args.url}")
print(f"✅ QR code saved to {filename}")