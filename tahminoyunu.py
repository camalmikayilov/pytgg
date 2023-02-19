print("Rəqəm təxmin etmə oyununa xoş gəlmisiniz!")

number = 30

playerNumbers = int(input("0 ilə 50 arasında bir rəqəm təxmin edin: "))

change = 3

while True:
    if change != 0:
        if playerNumbers > number:
            change -= 1
            playerNumbers = int(input("Daha kiçik bir rəqəm təxmin edin: "))
        elif playerNumbers < number:
            change -= 1
            print(change, "hakkiniz kaldi")
            playerNumbers = int(input("Daha böyük bir rəqəm daxil edin: "))

        if  playerNumbers == number: 
            print("Təbriklər oyunu qazandınız!")
            break

    if change == 0:
        print("Təəssüf oyunu uduzdunuz: ")
        break