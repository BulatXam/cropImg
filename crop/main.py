import crop
from PIL import Image


def main():
    img = Image.open("crop_img.jpg")
    crop_img = crop.crop_image_by_proportions(
        img, 3, 4
    )  # Обрезать до размера 3 на 4
    crop_img.show()


if __name__ == '__main__':
    main()
