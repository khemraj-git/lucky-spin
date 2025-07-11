
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "⭐"]
    return [random.choice(symbols) for _ in range(3)] #list comprehension


def print_row(row):
    print("------------------")
    print(" | ".join(row))
    print("------------------")



def get_payout(row,bet):
    if row[0] == row[1] == row[2]:#this will check which symbol is matched if all
                                # three match then only it will execute
        if row[0] == '🍒':      #based on symbols it will multiply the bet
            return bet*3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 2
        elif row[0] == '⭐':
            print("*******************")
            print("you hit a jackpot")
            print("*******************")
            return bet * 10
    return 0   #if no match return 0

def main():
    balance = 100

    print("************************")
    print("welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 ⭐ ")
    print("************************")

    while balance>0:
        print(f"current balance: ${balance}")
        bet = input("place your bet amount:-")

        if not bet.isdigit():
            print("please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <=0:
            print("bet must be greater than 0")
            continue


        balance -= bet
        row = spin_row()
        print("spinning....\n")
        print_row(row)


        #checking winnings
        payout = get_payout(row,bet)

        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round")

        balance+=payout

        if balance <= 0:
            print("\nGame over! You've run out of money.")
            break


        play_again = input("do you want to spin again? y/n:").upper()
        if play_again != 'Y':
            print("\n*********************************************")
            print(f"game over! your final balance is ${balance}")
            print("*********************************************")
            break




if __name__ == '__main__':
    main()