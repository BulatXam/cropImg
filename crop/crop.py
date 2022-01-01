def crop_image_by_proportions(image, width_p=3, height_p=4):
    width_sqr = height_sqr = min(image.width, image.height)

    max_proportion = max(width_p, height_p)
    min_proportion = min(width_p, height_p)

    size_proportion = (width_sqr / max_proportion) * min_proportion

    # Точка начала выреза ширины с середины
    width_center1 = (image.width - size_proportion) / 2
    # Точка конца выреза ширины с середины
    width_center2 = image.width - width_center1

    # Точка начала выреза высоты с середины
    height_center1 = (image.height - height_sqr) / 2
    # Точка конца выреза высоты с середины
    height_center2 = image.height - height_center1

    # В итоге получается прямоугольный четырехугольник,
    # который находится в центре картинки

    crop_coordinate = \
        (width_center1, height_center1, width_center2, height_center2)

    image = image.crop(
        crop_coordinate
    )

    return image
