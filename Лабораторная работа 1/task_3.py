players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count = len(players) # найдём количество игроков
team_1 = players[:int(count/2)] # первую половину в team_1
team_2 = players[int(count/2):] # вторую половину в team_2

print(f'{team_1}\n{team_2}')
