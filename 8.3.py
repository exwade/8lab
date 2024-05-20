from PIL import Image, ImageDraw, ImageFont

def add_greeting_card(input_image_path, output_image_path, crop_area, recipient_name):
    """
    Вырезает область изображения, добавляет текст с поздравлением и сохраняет новое изображение.
    
    Параметры:
    - input_image_path: путь к исходному изображению.
    - output_image_path: путь для сохранения нового изображения.
    - crop_area: кортеж (x1, y1, x2, y2), задающий область для обрезки изображения.
    - recipient_name: имя получателя поздравления.
    """
    # Открытие и обрезка изображения
    with Image.open(input_image_path) as img:
        cropped_img = img.crop(crop_area)
        
        # Добавление текста с поздравлением
        draw = ImageDraw.Draw(cropped_img)
        width, height = cropped_img.size
        font_size = 30
        font = ImageFont.truetype("arial.ttf", font_size)
        greeting_text = f"{recipient_name}, поздравляю!"
        text_width, text_height = draw.textbbox(greeting_text, font=font) # РАЗОБРАТЬСЯ ПОЧЕМУ ОШИБКА
        text_position = ((width - text_width) // 2, height - text_height - 10)
        draw.text(text_position, greeting_text, fill="red", font=font)


# Путь к исходному изображению
input_image_path = "images/otkritka.jpg" 
    
# Путь для сохранения нового изображения
output_image_path = "greeting_card.png"  # Имя нового изображения
    
# Координаты области для обрезки: (x1, y1, x2, y2)
crop_area = (100, 100, 400, 300)  # Пример координат: обрежем изображение с позиции (100, 100) до (400, 300)
    
# Имя получателя поздравления
recipient_name = input("Кого вы хотите поздравить? ")
    
# Вызов функции для обрезки изображения, добавления текста и сохранения нового изображения
add_greeting_card(input_image_path, output_image_path, crop_area, recipient_name)
