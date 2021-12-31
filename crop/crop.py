def crop_image_by_proportions(image, width_p=3, height_p=4):
    if image.width < image.height:
        width = image.width
        height = image.width
    else:
        width = image.height
        height = image.height

    common_percent = 100 / height_p + width_p

    width_percent = width / 100 * (common_percent * width_p)
    width_percent1 = (width - width_percent) / 2
    width_percent2 = width - width_percent1

    height_percent = height / 100 * (common_percent * height_p)
    height_percent1 = (height - height_percent) / 2
    height_percent2 = height - height_percent1

    crop_coordinates = \
        (width_percent1, height_percent1, width_percent2, height_percent2)
    image = image.crop(crop_coordinates)
    return image
