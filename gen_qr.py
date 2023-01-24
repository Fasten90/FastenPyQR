import qrcode

from PIL import Image


def merge_images(qr_img, logo_img):
    """ https://stackoverflow.com/questions/63355160/how-to-concatenate-two-images-one-on-top-of-the-other-in-python """

    # Scale the logo image. The width of the scaled logo shall be equal to the width of the QR code
    qr_width, qr_height = qr_img.size
    logo_current_width, logo_current_height = logo_img.size
    scaling_factor = qr_width / logo_current_width
    logo_new_height = int(scaling_factor * logo_current_height)
    logo_new_size = (qr_width, logo_new_height)
    logo_img = logo_img.resize(logo_new_size)

    # Create an empty image to paste both images on
    margin = 20
    result = Image.new(mode='RGB', size=(qr_width, qr_height + margin + logo_new_height), color='white')
    result.paste(logo_img, (0, 0))
    result.paste(qr_img, (0, qr_height + margin))
    return result


def generate_qr(info_text, ):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(info_text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img


def main():
    print('Generate QR')
    save_path = 'test/test_file.png'
    # Generate QR code image
    qr_img = generate_qr('TestData')
    # Load the logo
    logo_img = Image.open('template.png')
    # Merge
    merged_img = merge_images(qr_img, logo_img)

    merged_img.save(save_path)


if __name__ == '__main__':
    main()

