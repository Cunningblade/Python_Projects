import qrcode
def generate_qr(data):
    qr = qrcode.QRCode()# Create a qr code object whose name is qr
    qr.add_data(data)# add the data internal to the qr object
    qr.make()#make the qr code
    img = qr.make_image(fill_color="white",back_color="black")
    img.show()
    

data = input("Generate QR of : ")
generate_qr(data)


