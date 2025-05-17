import qrcode

# Read the URL and filename from the file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    url = lines[0].strip()
    filename = lines[1].strip()

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill='black', back_color='white')

# Save image
img.save(filename)
