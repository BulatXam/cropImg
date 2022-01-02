# Crop Image

___

Module from crop image by proportions

## How use
___

```python3
from PIL import Image
import crop

img = Image.open("crop_img.jpg")
crop_img = crop.crop_image_by_proportions(
    img, 3, 4
)  # Обрезать до размера 3 на 4
crop_img.show()
```

## Example
___

![Alt-текст](https://sun9-64.userapi.com/impg/ovVupunHj3sXOkZk7QhiF0492h828japynzz3g/dh0PwmhqFtk.jpg?size=2048x1152&quality=96&sign=e4c91219ab172a08d9c72009edda0a35&type=album "alt")
___
### 3x4 center
![Alt-текст](https://sun9-14.userapi.com/impg/tDslnltshTbbs0DukNyvDdETRtFhlwag7dYksQ/gBM3VXAdHaQ.jpg?size=864x1152&quality=96&sign=78c3cac52bd08360a0b0178c303d445f&type=album "alt")
