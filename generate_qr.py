import qrcode

url = "http://127.0.0.1:8000"

img = qrcode.make(url)

img.save("bhagavad_gita_qr.png")

print("QR Code generated successfully!")