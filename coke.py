print("Amount Due: 50")

amount_due = 50
coins_add = 0

while True:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
        coins_add += insert_coin



    if insert_coin >=50:
        amount_due = insert_coin - amount_due
        coins_add = insert_coin - coins_add
        print(f"Amount Due: {amount_due}")
        print(f"change owed: {coins_add - 50}")
        break
    else:
        print(f"Amount Due: {amount_due}")
