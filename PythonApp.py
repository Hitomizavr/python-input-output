# Start

# Ввод значений

type_of_pet = input ("Введите тип животного: ");
name = input ("Введите кличку животного: ");
age = abs(int(input("Введите возраст животного: ")));

# Функция проверки падежей именования возраста

def padeg(num, one, two, three):
    if ( 2 <= age % 10 <= 4) and not(11 <= age % 100 <= 14):
        return one;
    elif age % 10 == 1 and age % 100 != 11:
        return two;
    else:
        return three;
    return "";

# Вывод строки с собранными значениями

print("Это", type_of_pet.lower().strip(), "по кличке \"" + name.capitalize().strip() + "\".", "Возраст:", age, padeg(age, "года", "год", "лет") + ".");

# End