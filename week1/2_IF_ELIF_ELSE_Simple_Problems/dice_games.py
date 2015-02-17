from random import randint
n = input("N= ")
n = int(n)

player1 = input("First player's name: ")
player2 = input("Second player's name: ")

player1_rand = randint(1, n)
player2_rand = randint(1, n)

if player1_rand > player2_rand:
    print(player1 + " wins.")
elif player1_rand == player2_rand:
    print("It's a tie")
else:
    print(player2 + " wins.")
