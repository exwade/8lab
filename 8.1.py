from PIL import Image

def crop_image(input_image_path, output_image_path, crop_area):
    """
    Обрезает изображение по заданным координатам.
    
    Параметры:
    - input_image_path: путь к исходному изображению.
    - output_image_path: путь для сохранения обрезанного изображения.
    - crop_area: кортеж (x1, y1, x2, y2), задающий область для обрезки (верхний левый угол x1, y1 и нижний правый угол x2, y2).
    """
    # Открыть изображение
    with Image.open(input_image_path) as img:
        # Обрезать изображение по заданным координатам
        cropped_img = img.crop(crop_area)
        # Сохранить обрезанное изображение
        cropped_img.save(output_image_path)

# Путь к исходному изображению
input_image_path = "images/otkritka.jpg"
    
# Путь для сохранения обрезанного изображения
output_image_path = "images/cropped_image.jpg"  # Имя нового обрезанного изображения
    
# Координаты области для обрезки: (x1, y1, x2, y2)
crop_area = (50, 50, 500, 600)  # Пример координат: обрежем изображение с позиции (100, 100) до (400, 300)
    
# Вызов функции для обрезки изображения
crop_image(input_image_path, output_image_path, crop_area)
