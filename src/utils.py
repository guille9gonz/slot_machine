import random

# Asks player in how many rows does he want to bet
def get_number_lines(max_lines):
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1-{str(max_lines)}): "))
        except ValueError:
            print("Please, enter a number.")
            continue

        if 1 <= lines <= max_lines:
            break
        else:
            print("Please, enter a valid number of lines.")

    return lines

# Asks player for the amount to bet
def get_bet(min_bet, max_bet):
    while True:
        try:
            bet = int(input("How much would you like to bet on each line? $"))
        except ValueError:
            print("Please, enter a valid amount.")
            continue

        if min_bet <= bet <= max_bet:
            break
        else:
            print(f"Bet is out of allowed limits. Must be between ${min_bet} and ${max_bet}.")

    return bet

# Creates a matrix with the values for each column (vertical)
def generate_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

# Transposes the matrix and prints the spin
def print_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

# Checks if the three symbols of a row are the same
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines