def my_calculate_coins(coin):
    coins = {
        "1": 0,
        "2": 0,
        "100": 0,
        "5": 0,
        "10": 0,
        "50": 0,
        "20": 0
        }

    while coin > 0.00:
        if coin >= 1.00:
            coin = coin - 1.00
            coins["100"] += 1
        elif coin >= 0.50:
            coin = coin - 0.50
            coins["50"] += 1
        elif coin >= 0.20:
            coin = coin - 0.20
            coins["20"] += 1
        elif coin >= 0.10:
            coin = coin - 0.10
            coins["10"] += 1
        elif coin >= 0.05:
            coin = coin - 0.05
            coins["5"] += 1
        elif coin >= 0.02:
            coin = coin - 0.02
            coins["2"] += 1
        else:
            coin = coin - 0.01
            coins["1"] += 1

    return coins

def calculate_coins(coin):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]

    coin = round(coin * 100)

    for i in coins:
        number = coin // i
        result[i] = number
        coin = coin - (number * i)

    return result

    
