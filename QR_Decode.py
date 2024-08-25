# hii everyone how are you?
# in this today video we are going to create a decoder of QR Code in Python Development lanuage
# So Let's Get Started!!

import cv2

def decodeQR(qrcode):
    
    #this code will read the image of code 
    img = cv2.imread(qrcode)

    detector = cv2.QRCodeDetector()

    #this will detect and decode the QR
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("\nQR Code Data:\n", data, "\n\n")

    else:
        print("QR Code not Detected. Try Again!!")


#this will get the QR Code Image by Through Image_Name
qrcode = "QR_Code_By_Kingsman.png"

#Call the function
decodeQR(qrcode)

                            # Thank You for Watching my Video
                            # Subscribe my YouTube Channel For more Videos Related to Python Development

                            # Don't Forget to Watch Previous video of QR Code Generator