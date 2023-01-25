import qrcode

from PIL import Image, ImageFont, ImageDraw


def merge_images(qr_img, logo_img):
    """ https://stackoverflow.com/questions/63355160/how-to-concatenate-two-images-one-on-top-of-the-other-in-python """
    """ Merge qr + logo (left + right) """

    # Scale the logo image. The width of the scaled logo shall be equal to the width of the QR code
    qr_width, qr_height = qr_img.size
    logo_current_width, logo_current_height = logo_img.size
    #scaling_factor = qr_width / logo_current_width
    #logo_new_height = int(scaling_factor * logo_current_height)
    logo_new_width = int(qr_width + logo_current_width)
    logo_new_height = max(logo_current_height, qr_height)
    logo_new_size = (logo_new_width, logo_new_height)
    logo_img = logo_img.resize(logo_new_size)

    # Create an empty image to paste both images on
    margin = 20
    result = Image.new(mode='RGB', size=(logo_new_width, logo_new_height), color='white')
    result.paste(logo_img, (0, 0))
    result.paste(qr_img, (logo_current_width, 0))
    return result


def generate_qr(info_text):
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


def add_text_to_image(edit_image, text_lines):
    """ https://towardsdatascience.com/adding-text-on-image-using-python-2f5bf61bf448 """
    text_size = 14
    title_font = ImageFont.truetype('verdana.ttf', text_size)

    start_position = (40, 15)
    text_color = (0, 0, 0)

    for line in text_lines:
        image_editable = ImageDraw.Draw(edit_image)
        image_editable.text(start_position, line, text_color, font=title_font)
        new_pos_y = start_position[1] + text_size + 2
        pos_x = start_position[0]
        start_position = (pos_x, new_pos_y)
    return edit_image


def load_image(image_name):
    image_loaded = Image.open(image_name)
    return image_loaded


def main():
    print('Generate QR')
    save_path = 'test/test_file.png'
    # Generate QR code image
    qr_text = 'TestData'
    qr_img = generate_qr(qr_text)
    # Load the logo
    logo_img = load_image('template.png')
    # Edit image
    img_text = [ 'test_text', 'line 2...' ]
    edited_image = add_text_to_image(logo_img, img_text)
    # Merge
    merged_img = merge_images(qr_img, edited_image)

    merged_img.save(save_path)


if __name__ == '__main__':
    main()

