import random
from game_data import data
from art import logo
from art import vs
#from replit import clear
score = 0
onGame = True
print(logo)


def genNumber():
  num1 = 0
  num2 = 0
  while num1 == num2:
    num1 = random.randrange(0, len(data))
    num2 = random.randrange(0, len(data))
  return [num1, num2]

def printData(dat, l):
  print(f"Compare {l}: {dat['name']}, {dat['description']}, {dat['country']} ")

def printCompare(a,b):
  printData(a, "A")
  print(vs)
  printData(b, "B")

def checkAnswer(answer, a, b):
  if a > b and answer == "a":
    return True
  elif a < b and answer == "b":
    return True
  else:
    return False

while onGame:
  vsus = genNumber()
  printCompare(data[vsus[0]], data[vsus[1]])
  answer = input("Who has more followers? A or B: ")
  print(data[vsus[0]]['follower_count'])
  print(data[vsus[1]]['follower_count'])
  if checkAnswer(answer ,data[vsus[0]]['follower_count'], data[vsus[1]]['follower_count']):
    score += 1
    #clear()
    print(f"You are right, current score: {score}")
    print(logo)
  else:
    #clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    onGame = False
