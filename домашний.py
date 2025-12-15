#1.
'''
import re
def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
def scrabl():
    point_en = {1:'AEIOULNSTR',
                    2:'DG',
                    3:'BCMP',
                    4:'FHVWY',
                    5:'K',
                    8:'JX',
                    10:'QZ'}
    point_ru = {1:'АВЕИНОСТ',
                2:'ДКЛМПУ',
                3:'БГЁЬЯ',
                4:'ЙЫ',
                5:'ЖЗЧЦЧ',
                8:'ШЭЮ',
                10:'ФЩЪ'}
    while True:
        text_user = input("Для отмены напишите 0. Игрок 1 Введите слово:").upper()
        if text_user == "0":
            print("Прощайте")
            break
        text_user2 = input("Для отмены напишите 0. Игрок 2 Введите слово:").upper()
        if text_user2 == "0":
            print("Прощайте")
            break
        player1 = 0
        player2 = 0
        if isCyrillic(text_user):
                print('Кол-во очков:',sum([key for i in text_user for key, value in point_ru.items() if i in value]))
                player1 = player1 + sum([key for i in text_user for key, value in point_ru.items() if i in value])
                player2 = player2 + sum([key for i in text_user2 for key, value in point_ru.items() if i in value])
        else:
                print('Кол-во очков:',sum([key for i in text_user for key, value in point_en.items() if i in value]))
                player1 = player1 + sum([key for i in text_user for key, value in point_en.items() if i in value])
                player2 = player2 + sum([key for i in text_user2 for key, value in point_en.items() if i in value])
        print(f"кол-во очков первого игрока {player1}, кол-во очков второго игрока {player2} ")
'''
#2.
'''
def camping():
    backpack = {'Зажигалка': 20, 'Компас': 100, 'Фрукты': 500, 'Рубашка': 300,
                'Термос': 1000, 'аптечка': 200, 'Куртка': 600, 'Бинокль': 400,
                'Удочка': 1300, 'Салфетки': 40, 'Бутерброды': 800, 'Палатка': 5500,
                'Спальный мешок': 2500, 'Изолента': 250, 'Котел': 3000
                }
    human1_massa = int(input("Введите допустимый вес рюкзака первого человека: ")) * 1000
    human2_massa = int(input("Введите допустимый вес рюкзака первого человека: ")) * 1000
    print("Могу взять: ")
    for key, value in backpack.items():
        if value < human1_massa or value < human2_massa:
            print(key, value, end=' ')
            print()
            print("Не Могу взять: ")
    for key, value in backpack.items():
        if value > human1_massa or value > human2_massa:
            print(key, value, end=' ')
'''
#3.
'''
def contact_list():
    note_book = {"Маша":
                     {'tel': '+7922123561', 'vk': 'vk.com/masha321', 'youtube': 'youtube.com/masha321', 'telegram'
                     : 't.me/masha321'},
                 "Даша":{'tel': '+79023321293', 'vk': 'vk.com/dashulya1910', 'telegram': '@Egoistik_manyak'},
                 "Олег":{'tel': '+79522301092', 'vk': 'vk.com/CODStyle', 'youtube': 'youtube.com/CodeSky',
                         'telegram':'@CODProf'}}
    user_search = input(f"Введите имя из списка контактов:Маша,Даша,Олег ").capitalize()
    for key, value in note_book[user_search].values():
        print(value)
'''