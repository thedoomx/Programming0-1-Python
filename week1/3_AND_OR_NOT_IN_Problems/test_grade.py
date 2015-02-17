from random import randint

points = randint(0, 100)

if points > 0 and points <= 50:
    print("Слаб 2")
elif points > 50 and points <= 60:
    print("Среден 3")
elif points > 60 and points <= 70:
    print("Добър 4")
elif points > 70 and points <= 80:
    print("Много добър 5")
elif points > 80 and points < 100:
    print("Отличен 6")
else:
    print("Отличен 7")
