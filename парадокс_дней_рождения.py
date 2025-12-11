#Эксперимент Монте карло
from datetime import datetime
import random
#Год в нашей имитации роли не играет
#Акцент на дне и месяце
#Возвращаем список объектов дат для случайного дня рождения(нескольких)
def getBirthday(numberOfbirthdays):
    birthdays = []  #1. в виде переменной
    for i in range(numberOfbirthdays):
        startofyear = datetime.date(2000,1,1)
        #получаем для работы случайный день года
        randomNumberofdays = datatime.timedelta(randint(0,364))
        birthday = startofyear + randomNumberofdays
        birthdays.append(birthday)
    return birthdays
def getMatch(birthday):
    if len(birthdays) == len(set(birthdays)):
        return none
    for a,birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1 : ]):
            if birthdayA == birthdayB:
                return birthdayA
            #возвращаем совпадения
def main():
    month = ("jan","feb","march","april","may","june", #4. написать полные названия месяцев
             "jul","aug","sep","oct","nov","dec")
    while True:
        print("Сколько дат вы хотите сгенерировать P.S. Максимум сто")
        response = int(input("Введите число"))
        if 0 < response:
            numBDays = response # артем код запорол и ошибки нет :(
            break
        print()
        birthdays = getBirthday(numBDays)
        print("Here are",numBDays, "birthday")
        for i,birthday in enumerate(birthdays):
            if i != 0:
                print(',', end = '')
            monthName = month(birthday.month - 1)
            dateText = f"{monthName},{birthday.day}"
            print(dateText, end = '')
        print()
        print()
        #создаём проверку на совпадение дат
        match = getMatch(birthdays)
        print("Результаты генерации...", end = "")
        if match != None:
            monthName = month(match.month - 1)
            dateText = f"{MonthName} {matchday}"
            print('Несколько совпадений дат', dateText, end = '')
        else:
            print("Даты не совпали")
        print()
        print("Генерация", numBDays, "Дат рождения")
        input("Введите Enter для старта")
        simMatch = 0 #число операций
        for i in range(100): #2. сделать знаение выше 100
            if i % 100 == 0:
                print(i, "Симуляция")
            birthdays = getBirthday(numBDays)
            if getMatch(birthdays) == None:
                simMatch += 1
            print("Симуляция завершена")
            probablity = round(simMatch / 100 * 100, 2) # 5. заменить в 100 * 100, вторую сотню на 10
            print("количество дат", numBDays)
            print("количество симуляций", simMatch)
            print("процент совпадений", probablity)
            print("Завершение работы")
if __name__ == '__main__':
    main()
