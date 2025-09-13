import qrcode
from PIL import Image

data = input("Enter you text to generate QR: ")
qr = qrcode.QRCode(version=3, box_size=8, border=4)

qr.add_data(data)
qr.make(fit= True)

image = qr.make_image(fill="black", back_color="white")

file = input("Enter name to save: ")
path = f"{file}.png"

image.save(f"{file}.png")

Image.open(path)