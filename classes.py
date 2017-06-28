import random as rnd
import os
import msvcrt


class Gamestart:

    def startgame(self):
        print("Добро пожаловать в игру \"Быки и коровы!\"\n")
        print("Нажмите любую клавишу ")
        key = input()
        os.system('cls')


class Randomnumber:

    def generate_random_number(self):
        digits = [x for x in range(10)]
        rnd.shuffle(digits)
        num = digits[:4]
        number = [0, 0, 0, 0]
        number[0] = num[0]
        number[1] = num[1]
        number[2] = num[2]
        number[3] = num[3]
        return number


class Enternumber:

    def guess_number(self):
        correct = 0
        while correct == 0:
            inputnumber = input("Введите четырёхзначное число: ")
            guessnumber = [0, 0, 0, 0]
            try:
                if len(inputnumber) == 4:
                    guessnumber[0] = int(inputnumber[0])
                    guessnumber[1] = int(inputnumber[1])
                    guessnumber[2] = int(inputnumber[2])
                    guessnumber[3] = int(inputnumber[3])
                    correct = 1
                    os.system('cls')
                    print(guessnumber, "\n")
                else:
                    print("Число должно быть четырёхзначным\n\n")
            except ValueError:
                print("Вы должны ввести целое число\n\n")
        return guessnumber


class Bullscows:

    def __init__(self, number):
        self.number = number

    def bulls_cows(self):
        bulls = 0
        cows = 0
        score = 105
        i = 0
        j = 0
        while bulls < 4:
            enternumber = Enternumber()
            guessnumber = enternumber.guess_number()
            while i < 4:
                if self.number[i] == guessnumber[i]:
                    bulls += 1
                else:
                    while j<4:
                        if self.number[i] == guessnumber[j]:
                            cows += 1
                        j += 1
                i += 1
            print("быки - ", bulls, "коровы - ", cows, "\n\n")
            score -= 5
        os.system('cls')
        print("Вы угадали число!\nВаш счёт: ", score, "\n")
        return score


class Highscore:

    def __init__(self, score):
        self.score = score

    def high_score(self):
        file = open("highscore.txt", "r")
        highscore = file.readlines()
        file.close()
        i = 0
        k = 0
        scorearray = [[], [], [], [], [], [], [], [], [], []]
        while i<10:
            for line in highscore:
                scoreline = line.split("\n")
                scoreline = scoreline[0].split(" ")
                scorearray[i] = scoreline
                i += 1
        i = 0
        highscoreachieved=0
        while i < 10:
            if self.score > int(scorearray[i][1]):
                if highscoreachieved == 0:
                    j=9
                    while j > i:
                        scorearray[j] = scorearray[j-1]
                        j -= 1
                    scorearray[i][0] = str(input("Вы попали в таблицу лучших! Введите ваше имя: "))
                    scorearray[i][1] = self.score
                    highscoreachieved = 1
            print("\t", scorearray[i][0], "\t", scorearray[i][1])
            i += 1
        print("Нажмите любую клавишу ")
        key = input()
        os.system('cls')


class Runapp:

    def runapp(self):
        gamestart = Gamestart()
        randomnumber = Randomnumber()
        first = gamestart.startgame()
        second = randomnumber.generate_random_number()
        bullscows = Bullscows(second)
        third = bullscows.bulls_cows()
        highscore = Highscore(third)
        fourth = highscore.high_score()
