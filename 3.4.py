import qrcode
import sys

def main():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(sys.argv[1])
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(sys.argv[2] + '.jpg')
    except:
        img.save('qr.jpg')

if __name__ == "__main__":
    main()