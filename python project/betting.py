import random

# ------------------ CONSTANTS ------------------
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# ------------------ SLOT LOGIC ------------------
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

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


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = "|" if i != len(columns) - 1 else ""
            print(column[row], end=end_char)
        print()

# ------------------ USER INPUT ------------------
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than 0.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Enter a valid number of lines.")


def get_bet():
    while True:
        amount = input(f"What would you like to bet per line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print("Invalid bet amount.")

# ------------------ MAIN GAME ------------------
def main():
    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")
        lines = get_number_of_lines()

        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"Not enough balance. Current balance: ${balance}")
            else:
                break

        print(f"\nYou are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
        balance -= total_bet

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)

        play_again = input("\nPress Enter to play again (q to quit): ")
        if play_again.lower() == "q":
            break

    print(f"\nYou left with ${balance}. Thanks for playing!")

# ------------------ RUN ------------------
main()
