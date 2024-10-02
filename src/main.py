from core import deposit, spin
import os, time

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press Enter to play / Press Q to quit.\n")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()