import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
def deal():
  return random.choice(cards)
def deal_2():
  return random.sample(cards, 2)
def calculate_score(cards):
  score = sum(cards)
  if score > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  if score == 21 and len(cards) < 3:
    score = 0
  return score
def compare_scores_active(computer, player):
  if computer == 0 and player == 0:
    return 3
  elif computer == 0:
    return 0
  elif computer == 21:
    return 0
  elif player == 21:
    return 2
  elif player == 0:
    return 1
  elif computer > 21:
    return 2
  elif player > 21:
    return 0
  elif computer > 21 and player > 21:
    return 0
def compare_scores_final(computer, player):
  if player == computer:
    return 3
  elif computer == 21:
    return 0
  elif player == 21:
    return 1
  elif computer > 21:
    return 1
  elif player > 21:
    return 0
  elif computer > 21 and player > 21:
    return 0
  elif computer > player:
    return 0
  elif player > computer:
    return 1
def show_cards(player, score):
  print(f"Your cards: {player}, current score: {score}")
def show_computer_cards(computer, score):
  print (f"Computer cards: {computer_cards}, computer score: {computer_score}")
another_card = True
play = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
if play == 'n':
  os.system('cls')
elif play == 'y':
  end_of_game = False
  print(logo)
  player_cards += deal_2()
  computer_cards += deal_2()
  player_score = calculate_score(player_cards)
  computer_score = calculate_score(computer_cards)
  show_cards(player_cards, player_score)
  print(f"Computer's first card: {computer_cards[0]}")
  while another_card == True:
    compare_scores = compare_scores_active(computer_score, player_score)
    if compare_scores == 0:
      print("Computer wins.")
      show_cards(player_cards, player_score)
      show_computer_cards(computer_cards, computer_score)
      another_card = False
      end_of_game = True
    elif compare_scores == 1:
      print("Blackjack. You win.")
      show_cards(player_cards, player_score + 21)
      show_computer_cards(computer_cards, computer_score)
      another_card = False
      end_of_game = True
    elif compare_scores == 2:
      print("You win.")
      show_cards(player_cards, player_score)
      show_computer_cards(computer_cards, computer_score)
      another_card = False
      end_of_game = True
    elif compare_scores == 3:
      print("Draw.")
      show_cards(player_cards, player_score)
      show_computer_cards(computer_cards, computer_score)
      another_card = False
      end_of_game = True
    else:
      another = input("Do you want another card? Type 'y' or 'n': ")
      if another == 'y':
        player_cards.append(deal())
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        if player_score < 21:
          show_cards(player_cards, player_score)
        another_card = True
      elif another == 'n':
        another_card = False
  if another_card == False and end_of_game == False:
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal())
      computer_score = calculate_score(computer_cards)
    player_score = calculate_score(player_cards)
    show_cards(player_cards, player_score)
    show_computer_cards(computer_cards, computer_score)
    compare_scores = compare_scores_final(computer_score, player_score)
    if compare_scores == 0:
          print("Computer wins.")
    elif compare_scores == 1:
          print("You win.")
    elif compare_scores == 3:
          print("Draw.")