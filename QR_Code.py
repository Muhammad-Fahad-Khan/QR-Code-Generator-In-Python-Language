# Hii everyone how are you?
# In this today's video we are going to develop a QR Code Image by through Python Development Language
# So Let's Get Started!!

import qrcode
from PIL import Image

# i created a function in which image will be print out in PNG Form
def GenerateQrCode(data, filename="QR_Code_By_Kingsman.png"):
    
    # This will Create A Box & Border of Image
    qr = qrcode.QRCode(version=1, box_size=20, border=10)
    qr.add_data(data)
    qr.make(fit=True)

    #image of URL will be in Black
    img = qr.make_image(fill= "Black", blackcolor="white")
    img.save(filename)
    print(f"QR Code is Generated & also Saved as: {filename}")

data = "https://www.instagram.com/coding_by_kingsman/"
#this is enter data in QR COde
GenerateQrCode(data)


                        # In Next Video We will Develop a Encode of QR Code
                        # So Subcribe our Youtube Channel for More Updates
                        # Thank  You for Watching!!!