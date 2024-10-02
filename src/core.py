from utils import get_number_lines, get_bet, generate_spin, print_spin, check_winnings
from constants import MAX_LINES, ROWS, COLS, MIN_BET, MAX_BET, SYMBOL_COUNT, SYMBOL_VALUES
import os, time

def deposit():
    while True:
        try:
            amount = int(input("How much would you like to deposit? $"))
        except ValueError:
            print("Please, enter a valid amount.")
            continue

        if amount > 0:
            break
        else:
            print("Amount must be greater than 0.")
            
    return amount


def spin(balance):
    lines = get_number_lines(MAX_LINES)
    while True:
        bet = get_bet(MIN_BET, MAX_BET)
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have have enough to bet ${total_bet}. Current balance is: ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.")
            sure = input("Are you sure? (y/n)\n")
            if sure.lower() == "y":
                break

    time.sleep(2)
    os.system("cls")
    slots = generate_spin(ROWS, COLS, SYMBOL_COUNT)
    print_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, values=SYMBOL_VALUES)

    if winnings > 0:
        print(f"You won on line/s:", *winning_lines)
        print(f"You won ${winnings}.")
    else:
        print("You lost... Better luck next time!")

    time.sleep(4)
    os.system("cls")

    return winnings - total_bet
