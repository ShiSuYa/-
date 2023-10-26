def get_health_indicators(weight:float, height:float):

    height = height * 0.01

    # расчет ИМТ
    bmi = weight / (height ** 2)

    value = f"Ваш ИМТ - {round(bmi, 1)}\n"

    if bmi < 18.5:
        value += "У вас недовес"
        return value
    elif 18.5 <= bmi < 25:
        value += "Показатели в норме"
        return value
    else:
        value += "У вас перевес"
        return value