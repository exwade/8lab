from PIL import Image

# Словарь с парами "Название праздника - имя файла с открыткой"
holiday_cards = {
    "День рождения": "images/birthday_card.jpg",
    "Новый год": "images/new_year_card.jpg",
    "8 Марта": "images/womens_day_card.jpg",
    # Добавьте другие праздники и соответствующие файлы с открытками по вашему выбору
}

def display_card(holiday):
    """
    Отображает открытку для указанного праздника.
    
    Параметры:
    - holiday: строка с названием праздника.
    """
    # Получаем имя файла с открыткой из словаря по названию праздника
    card_file = holiday_cards.get(holiday)
    
    if card_file:
        try:
            # Открываем и отображаем изображение
            with Image.open(card_file) as img:
                img.show()
        except FileNotFoundError:
            print(f"Файл открытки для праздника '{holiday}' не найден.")
    else:
        print(f"Открытка для праздника '{holiday}' не найдена.")

# Спрашиваем у пользователя, к какому празднику он хочет получить открытку
chosen_holiday = input("К какому празднику вам нужна открытка? Введите название: ")
    
# Отображаем открытку для выбранного праздника, если такая есть
display_card(chosen_holiday)
