from random import randint

maria_score = 1001
ivan_score = 1001

maria_dice = 0
ivan_dice = 0

counter = 5

while maria_score != 0 or ivan_score != 0: # while True:
    if maria_score == 0 and ivan_score == 0:
        print("Omg, it's a tie!!!")
        break
    elif maria_score == 0:
        print("Maria WINS!")
        break
    elif ivan_score == 0:
        print("Ivan WINS!")
        break
    else:
        while counter > 0:
            dice = randint(1, 6)
            maria_dice += dice
            counter -= 1
        if maria_score > 0:
            maria_score -= maria_dice
        else:
            maria_score += maria_dice
        print("Maria rolled: " + str(maria_dice))
        print("Maria's score: " + str(maria_score))
        counter = 5
        maria_dice = 0

        while counter > 0:
            dice = randint(1, 6)
            ivan_dice += dice
            counter -= 1
        if ivan_score > 0:
            ivan_score -= ivan_dice
        else:
            ivan_score += ivan_dice
        print("Ivan rolled: " + str(ivan_dice))
        print("Ivan's score: " + str(ivan_score))
        counter = 5
        ivan_dice = 0
