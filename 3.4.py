import qrcode
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys

def scan():
    cap = cv2.VideoCapture(0)
    isScaned = False
    while not isScaned:
        ret, frame = cap.read()
        if ret:
            decoded_objects = pyzbar.decode(frame)
            for obj in decoded_objects:
                if obj.type == "QRCODE":
                    print("Wartość:", obj.data.decode('utf-8'))
                    isScaned = True
    cap.release()

def make():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    data = ''
    try:
        input = open(sys.argv[1])
        for line in input:
            data += line
    except:
        data = sys.argv[1]

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(sys.argv[2] + '.jpg')
    except:
        img.save('qr.jpg')

def main():
    if sys.argv[1].lower == 'scan':
        scan()
    else:
        make()

if __name__ == "__main__":
    main()