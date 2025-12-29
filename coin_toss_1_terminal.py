import os
from game_logic import coin_toss

def clear_1 ():
    os.system('cls' if os.name == 'nt' else 'clear')

def structure():
    while True :
        clear_1()
        print('Coin Toss')
        print('-' * 20)

        guess = input("Pick a side (heads/tails): ").strip().lower()

        if guess not in ['heads', 'tails']:
            print('Please type', 'heads', 'or', 'tails''.')
            input("\nPress Enter to try again...")
            continue

        result = coin_toss()
        print(f'\nThe coin landed on: {result}')
        
        if guess == result:
            print('YOU WON')
        else:
            print('whoops, Good Luck Next Time')
        
        play_again = input('\nPlay again? (yes/no): ').strip().lower()

        if play_again not in ['y', 'Y', 'Yes', 'yes']:
                print('\nThank you for using coin toss')
                break

        if guess not in ['heads', 'tails']:
            print("Please type 'heads' or 'tails'.")
            input('\nPress Enter to try again...')
            continue
        
        result =coin_toss()
        print(f"\nThe coin landed on: {result}")

        if guess == result:
            print('YOU WON')
        else:
            print('whoops, Good Luck Next Time')

        play_again = input('\nPlay again? (yes/no): ').strip().lower()
        if play_again not in ['y', 'yes', 'Yes', 'Y', 'n', 'N', 'No', 'no']:
            print('please write either heads or tails')
        if play_again not in ['y', 'Y', 'Yes', 'yes']:
            print('\nThank you for using coin toss')
            break

if __name__ == "__main__":
    structure()