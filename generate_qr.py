import qrcode

url = "https://bhagavad-gita-c7xw.onrender.com"

img = qrcode.make(url)

img.save("bhagavad_gita_qr.png")

print("QR Code generated successfully!")