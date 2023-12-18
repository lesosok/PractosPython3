import random
import json
import os
import csv

Enemy = [
    {"Имя": "Алёша", "Здоровье": 50},
    {"Имя": "Андрей", "Здоровье": 100},
    {"Имя": "Николай", "Здоровье": 150},
    {"Имя": "Павел", "Здоровье": 200}
]

def csvSave(kills):
    data = [f"Имя - {Player['Имя']}", f"HP - {Player['Здоровье']}", "Убийств - " + str(kills), f"Аптечки - {Equipment['Аптечки']}", f"Деньги - {Equipment['Деньги']}"]
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def jsonSave(kills):
    data = {}
    data['Пользователи'] = []
    data['Пользователи'].append({
        "name": Player['Имя'],
        "HP": Player['Здоровье'],
        "kills": kills,
        "medkits": Equipment['Аптечки'],
        "money": Equipment['Деньги']
    })

    if os.path.exists('data.json'):
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

    else:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

def battle():
    enemy = random.choice(Enemy)
    print(f"На вашем пути появился {enemy['Имя']}")

    while enemy['Здоровье'] > 0 and Player['Здоровье'] > 0:
        print(f"Ваше здоровье: {Player['Здоровье']}")
        print(f"Здоровье противника: {enemy['Здоровье']}")
        print("Выберите действие:\n1) Атаковать\n2) Воспользоваться аптечкой\n3) Сдаться\n4) Посмотреть сколько у вас аптечек")

        action = int(input())

        if action > 4 or action < 1:
            print("\nДействия с таким номером нет. Повторите попытку\n")

        else:
            match action:
                case 1:
                    player_attack = random.randint(10, 15)
                    enemy['Здоровье'] -= player_attack
                    print(f"\nВы нанесли противнику {player_attack} урона")

                    if enemy['Здоровье'] <= 0:
                        print(f"{enemy['Имя']} погиб")
                        print("Обыскав его труп, вы нашли 5 монет\n")
                        Equipment['Деньги'] += 5
                    else:
                        enemy_attack = random.randint(5, 10)
                        Player['Здоровье'] -= enemy_attack
                        print(f"Противник нанёс вам {enemy_attack} урона")
                        if Player['Здоровье'] <= 0:
                            print("Вас убили")
                            print(f"У противника осталось ещё {enemy['Здоровье']} здоровья")
                    continue

                case 2:
                    Equipment['Аптечки'] -= 1
                    Player['Здоровье'] = 100
                    print(f"\nВы использовали 1 аптечку, полностью восстановив своё здоровье. Сейчас ваше количество аптечек составляет: {Equipment['Аптечки']}")
                    continue

                case 3:
                    print(f"\n{enemy['Имя']} отрубил вам голову")
                    Player['Здоровье'] = 0
                    prodolzhit = "нет"

                case 4:
                    print(f"\nУ вас есть столько аптечек: {Equipment['Аптечки']}")
                    continue

def shop():
    action = 0
    print("Зайдя в магазин, вы обнаружили, что здесь продаются только аптечки.")
    while action != 3:
        print("Хорошенько подумав, вы решили:\n1) Посмотреть, сколько у вас есть аптечек и монет\n2) Купить 1 аптечку за 5 монет\n3) Уйти из магазинчика")
        action = int(input())
        match action:
            case 1:
                print(f"\nУ вас есть столько аптечек: {Equipment['Аптечки']}, и столько монет: {Equipment['Деньги']}\n")
                continue;

            case 2:
                Equipment['Аптечки'] += 1
                Equipment['Деньги'] -= 5
                print(f"\nТеперь у вас есть столько аптечек: {Equipment['Аптечки']}, и столько монет: {Equipment['Деньги']}\n")
                continue;

name = input("Введите ваше имя: ")

Equipment = {"Аптечки": 1, "Деньги": 5}
Player = {"Имя": name, "Здоровье": 100}

prodolzhit = "да"

kills = 0

battle()
if Player['Здоровье'] <= 0:
    prodolzhit = "нет"

while prodolzhit == "да":
    kills = kills + 1
    print("Решите что вы хотите сделать:\n1) Пойти в магазин\n2) Продолжить путь\n3) Сохранить игру\n4) Удалить сохранения\n5) Вспомнить кол-во поверженных врагов\n6) Выйти")
    choice = int(input())
    match choice:
        case 1:
            shop()
            continue

        case 2:
            battle()
            if Player['Здоровье'] <= 0:
                prodolzhit = "нет"
                kills = kills + 1

        case 3:
            jsonSave(kills)
            print("Сохранение прошло успешно")
            continue

        case 4:
            os.remove("C:/Users/Leefaut/PycharmProjects/pythonProject3/data.json")
            os.remove("C:/Users/Leefaut/PycharmProjects/pythonProject3/data.csv")
            print("Все сохранения удалены")
            continue

        case 5:
            print("\nВы одолели", kills, "негодяев. Так держать!\n")
            continue

        case 6:
            csvSave(kills)
            prodolzhit = "нет"