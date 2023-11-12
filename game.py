from random import randint
from time import sleep


# информация о персонаже игрока
player = {
    'name': '',
    'armor': 0.95,
    'base_hp': 100,
    'buff_hp': 0,
    'attack': 5,
    'luck': 10,
    'money': 10000,
    'inventory': []
}
total_pl_hp = int(player['base_hp']) + int(player['buff_hp'])


enemies = [
    {
        'name': 'Волк',
        'hp': 50,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 250,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },

    {
        'name': 'Доминик Торетто',
        'hp': 500,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты меня убил, но я точно появлюсь в следующей части',
        'loss': 'Прощай..'
    }
]

shop = {
    'расходники': {
        'леч. зелье': {'цена': 100, 'описание':'Восстанавливает 50 единиц здоровья'},
        'зелье урона': {'цена': 1000, 'описание':'Увеличивает силу атаки на 20%'},
        'зелье защиты': {'цена': 900, 'описание':'Увеличивает защиту на 30%'}
    },
    'оружие': {
        'обычный меч': {'цена': 1000, 'описание': 'Обычный меч из железа. Добавляет 10 ед. урона и 5% увелечения урона от критического удара'},
        'кинжал': {'цена': 1000, 'описание': 'Обычный кинжал из железа. Добавляет 5 ед. урона и на 15% увелечения урона от критического удара'},
    },
    'броня': {
        'шлем': {'цена': 750, 'описание': 'Шлем повышающий защиту. Увеличивает параметр брони на 2'},
        'нагрудник': {'цена': 1500, 'описание': 'Нагрудниу повышающий защиту. Увеличивает параметр брони на 7'},
        'наручи': {'цена': 750, 'описание': 'Шлем повышающий защиту. Увеличивает параметр брони на 3'},
        'поножи': {'цена': 1000, 'описание': 'Шлем повышающий защиту. Увеличивает параметр брони на 4'}
    }
}


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0
while True:
    action = input('Выберите действие(атака/тренировка/магазин/инвентарь/кошелёк/прекратить): ')
    if action == 'прекратить':
        break
    elif action == 'кошелёк':
        print('У вас в кошельке', player['money'])
    elif action == 'инвентарь':
        print('Вот список предметов в вашем инвентаре:')
        for index, item in enumerate(player['inventory'], start=1):
            print(f'{index}. {item}')
        choice = input('Введите числовое значение предмета, чтобы выбрать его: ')
        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(player['inventory']):
                selected_item = player['inventory'][index]
                print(f'Вы выбрали предмет {selected_item}. Что вы хотите сделать?')
                action = input('Введите команду (использовать/выкинуть/отмена: ')
                if action == 'использовать':
                    print(f'Вы использовали предмет {selected_item}.')
                elif action == 'выкинуть':
                    print(f'Вы выбросили предмет {selected_item}.')
                elif action == 'отмена':
                    print('Инвентарь закрыт.')
                else:
                    print('Неверная команда.')
            else:
                print('Неверное числовое значение предмета.')
        else:
            print('Неверный ввод числового значения.')
    elif action == 'атака':
        print()
        round = randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()
        while total_pl_hp > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                crit = randint(1, 5)
                if crit < 3:
                    print('crit')
                    enemy_hp -= (player['attack'] * (1 + (1 / player['luck'])))
                else:
                    enemy_hp -= player['attack']
                sleep(1)
                print(f'''{player['name']} - {total_pl_hp}
{enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}.')
                total_pl_hp -= (enemy['attack'] - (enemy['attack'] * ((0.06 * player['armor'])/(1+0.06 * player['armor']))))
                sleep(1)
                print(f'''{player['name']} - {total_pl_hp}
{enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        if total_pl_hp > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            current_enemy += 1
            total_pl_hp = int(player['base_hp']) + int(player['buff_hp'])
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
            total_pl_hp = int(player['base_hp']) + int(player['buff_hp'])
    elif action == 'тренировка':
        print('Ваш персонаж начал тренироваться')
        input('Enter чтобы продолжить')
        
        up_hp = randint(1, 10)
        up_attack = randint(1, 3)
        
        player['buff_hp'] += up_hp
        player['attack'] += up_attack
        total_pl_hp = int(player['base_hp']) + int(player['buff_hp'])

        print(f'текущий показатерь атаки: {player["attack"]}\nТекущий показатель здоровья: {total_pl_hp}')
    elif action == 'магазин':
        print('Добро пожаловать в магазин!')
        while True:
            category = input('Выберите категорию товаров (расходники, оружие, броня): ')
            if category == 'выйти':
                break
            elif category in shop:
                print(f'Вот доступные товары в категории {category}:')
                for item in shop[category]:
                    print(f'{item}: Цена - {shop[category][item]["цена"]}, Описание - {shop[category][item]["описание"]}')
                while True:
                    choice = input('Введите название товара или напишите "вернуться" для выхода из категории: ')
                    if choice == 'вернуться':
                        break
                    elif choice in shop[category]:
                        confirm = input('Вы уверены, что хотите купить этот товар? (да/нет): ')
                        if confirm == 'да':
                            price = shop[category][choice]['цена']
                            if player['money'] >= price:
                                player['money'] -= price
                                player['inventory'].append(choice)
                                print(f'Вы успешно приобрели {choice}!')
                            else:
                                print('У вас недостаточно денег для покупки этого товара.')
                        elif confirm == 'нет':
                            continue
                        else:
                            print('Неверный выбор. Пожалуйста, введите "да" или "нет".')
                    else:
                        print('Такого товара нет в данной категории.')
            else:
                print('Такой категории товаров нет в магазине.')