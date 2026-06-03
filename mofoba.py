import time
import random

store_items = {
    "chocoberry ice cream": 38.00,
    "blueberry chocolate pancakes": 17.00,
    "sesame kaiser bun": 17.00,
    "pain au chocolat": 31.00,
    "milk bread loaf": 25.00,
    "brown sourdough bread": 7.00,
}

def calculate_total_price(items):
    total_price = 0.0
    for item in items:
        if item in store_items:
            total_price += store_items[item]
        else:
            print(f"Item '{item}' not found in the store.")
    return total_price

money = 100.00

while True:
    print(f"good morning, human! you have ${money:.2f} in your wallet.")
    choice = input("work or bakery? (or 'quit' to exit) ")

    if choice.lower() == "bakery":
        items = [items.strip() for item in input("which pastry will we buy today?").split(",")]
        total_price = calculate_total_price(items)
        time.sleep(0.5)
        jadibeliga = input("are you sure you want to purchase these items?")
        if jadibeliga.lower() == "yes" or jadibeliga.lower() == "Yes":
            if money < total_price:
                print("you don't have enough money to proceed with the transaction!")
            elif money >= total_price:
                print(f"transaction successful! You now have ${final_money:.2f}")
                final_money = money - total_price
            elif total_price == 0:
                print("no items selected to purchase.")
        if jadibeliga.lower() == "no" or jadibeliga.lower() == "No":
            print("purchase cancelled")
            break
        time.sleep(0.5)
        print(f"total price: {total_price}")

    elif choice.lower() == "work":
        print("You chose to work. Have a productive day!\n")
        time.sleep(0.5)
        print("You work as a maths problem solver. You still have an entry level job.\n")
        print("Your job is to answer math questions about addition as you move on!")
        print('You will have 10 seconds to answer each question, and you will earn money for each correct answer. If you run out of time, you will lose money.\n')
        time.sleep(1)
        money_addition = [10.00, 15.00, 5.00, 1.00, 2.00, 20.00, 1.00, 3.00, 4.00, 6.00, 2.00, 8.00, 3.00]
        try:
            seconds = 10
            while True:
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                answer = input(f"What is {a} + {b}? (type 'quit' to stop) ")
                while seconds > 0 and not answer:
                    print(f"Time remaining: {seconds} second{'s' if seconds != 1 else ''}...")
                    time.sleep(1)
                    seconds -= 1
                if not answer:
                    print("Time's up!")
                    money -= 1.00
                    seconds = 10
                    continue
                if answer.lower() in ("quit", "exit"):
                    break
                try:
                    if int(answer) == a + b:
                        reward = random.choice(money_addition)
                        money += reward
                        print(f"Correct! You earned ${reward:.2f}. Total money: ${money:.2f}\n")
                    else:
                        print("Wrong answer. Try the next one.\n")
                except ValueError:
                    print("Please enter a number or 'quit'.\n")
        except KeyboardInterrupt:
            print("\nStopped working.")

    elif choice.lower() == 'quit':
        print('Goodbye. Go to sleep!')
        break

    else:
        print("Invalid choice. Please enter 'work', 'bakery', or 'quit'.")