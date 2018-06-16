"""Command-line battleships game by Piotr Goldys"""

from random import randint
from time import sleep

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

print
print "Your task is to touch my tralala. "
print "Try guessing it's position on a 5x5 field, by entering numbers. You have 8 turns"
print
print


def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

a = "Turn: "
turn = 0
for turn in range(0,8):
  t = turn + 1
  print
  print a + str(t)
  guess_row = input("Guess Row: ") - 1
  guess_col = input("Guess Col: ") - 1


  if guess_row == ship_row and guess_col == ship_col:
    print
    print "Uuuu... My ding ding dong!"
    print "Congratulations! You touch my tralala"
    break
  elif guess_row not in range(0,5) or \
  guess_col not in range(0,5):
    print
    print "Wtf, dude? Grid is 5x5"
    print
    print "---------------------------"
    sleep(1.5)
    import os

    os.system('cls')
  elif board[guess_row][guess_col] == "X":
    print
    print("You guessed that one already.")
    print
    print "---------------------------"
    sleep(1.5)
    import os
    os.system('cls')
  else:
     print
     print "You missed my tralala!"
     print
     print "---------------------------"
     sleep(1.5)
     import os

     os.system('cls')
     board[guess_row][guess_col] = "X"
  print
  print "Your task is to touch my tralala. "
  print "Try guessing it's position on a 5x5 field, by entering numbers. You have 8 turns"
  print
  print
  print_board(board)
  if turn == 7:
    print
    print "Game Over :("

