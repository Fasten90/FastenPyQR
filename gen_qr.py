import qrcode


def generate_qr(info_text, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(info_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)


if __name__ == '__main__':
    print('Generate QR')
    generate_qr('TestData', 'test/test_file.png')

