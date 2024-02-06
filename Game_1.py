import random
import sys

points = 100
bet = int(0)
print("Количество очков ", points)
while True:

    if points == 0 and bet == 0:
        print("У вас не осталось очков")
        x = input("Для выхода введите х")
        if x == 'x':
            sys.exit()
    else:
        bet = input("Введите ставку: ")
        bet = int(bet)
        if bet > points:
            print("У вас не осталось очков, понизьте ставку")
            bet = 0
        elif bet == 0:
            print("Введите ставку: ")
            bet = int(bet)
        else:
            a = int(input("Введите число от 2 до 12: "))
            roll1 = random.randrange(1, 6)
            roll2 = random.randrange(1, 6)
            sum = roll1 + roll2
            print("Сумма очков броска компьютера равна: ", sum)

            if sum == a:
                bet = bet * 4
                points = points + bet
                print("Вы выйграли +", bet)

            elif sum < 7 and a < 7:
                points = points + bet
                print("Вы выйграли +", bet)

            elif sum > 7 and a > 7:
                points = points + bet
                print("Вы выйграли +", bet)

            else:
                points = points - bet
                print("Вы проиграли -", bet)

            print("Количество очков ", points)
            print("Хотите продолжить игру?")
            x = input("Для продолжения введите 'Да', для выхода введите 'Нет' ")
            if x == 'Да':
                print("Играем дальше")
            else:
                sys.exit()


















