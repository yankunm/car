from PIL import Image


def crop_image(input_image_path, output_image_path, crop_box):
    """
    Crop the image to the specified box.

    Args:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the cropped image.
        crop_box (tuple): Tuple containing the coordinates (left, upper, right, lower) of the crop box.
    """
    # Open the input image
    image = Image.open(input_image_path)
    width, height = image.size
    print("Image shape (width, height):", width, height)

    # Crop the image
    cropped_image = image.crop(crop_box)

    # Save the cropped image
    cropped_image.save(output_image_path)


# Example usage:
if __name__ == "__main__":
    input_image_path = "/Users/yankunmeng/Desktop/S24_DUKE/car/html5up-future-imperfect/images/ferrari.png"
    output_image_path = "/Users/yankunmeng/Desktop/S24_DUKE/car/html5up-future-imperfect/images/ferrari2.png"
    crop_box = (0, 510 // 2 - 50, 800, 490)  # (left, upper, right, lower)
    crop_image(input_image_path, output_image_path, crop_box)
