import colorama
from simple_game import SimpleGame
print(colorama.Fore.RESET, colorama.Back.RESET)
print(colorama.Back.RED, "")
print(colorama.Fore.BLUE, "")
game1 = SimpleGame("game 1")
game1.show_board()
while True:
    move = input("Move? ")
    game1.make_move("X", move)
    game1.show_board()
print("")
print("")