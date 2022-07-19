def convert(number):
    """Проверяем полученное число и преобразуем его в строку эмодзи"""
    numbers_dict = {
        "0": '0️⃣', "1": '1️⃣', "2": '2️⃣', "3": '3️⃣', "4": '4️⃣', "5": '5️⃣', "6": '6️⃣', "7": '7️⃣', "8": '8️⃣', "9": '9️⃣', ".":"⏺", ",":"⏺"
    }
    emoji = ""

    number = str(number)

    for i in number:
        emoji += numbers_dict[i]

    return emoji


if __name__ == "__main__":
    num = input("Введите число: ")
    emoji = convert(num)
    print(emoji)

