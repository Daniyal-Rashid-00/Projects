import qrcode
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('I am Daniyal (The Coder)')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save("QR Test.png")