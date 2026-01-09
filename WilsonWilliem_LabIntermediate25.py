import random

def randomWord():
  words = {
    1: "WALKING",
    2: "TIME",
    3: "FRIEND",
    4: "HELLO",
  }

  randomNum = random.randint(1,4)
  randomWord = words[randomNum]
  return randomWord

def life(lifes):
  theMan = {
    5: '''
  ____
 /  
 |
/-\\
''',
    4: '''
  ____
 /   O
 |
/-\\
''',
3: '''
  ____
 /   O
 |   |
/-\\
''',

2: '''
  ____
 /   O
 |  /|\\
/-\\
''',
1: '''
  ____
 /   O
 |  /|\\
/-\\ /
''',
0: '''
  ____
 /   O
 |  /|\\
/-\\ / \\
''',
  }
  print(theMan[lifes])

def main():
  word = randomWord()
  lengthWord = len(word)
  blank = "_"
  guess = []

  for i in range(lengthWord):
    guess.append(blank)

  print("given secrete word.(\"close1\" to exit)\n type all the letter to win")
  
  lifes = 5
  life(lifes)

  while True:
    for i in range(len(guess)):
      print(guess[i]+" ", end="")
    
    print("\n")
    userInput = input("guess: ").upper()

    if userInput == "CLOSE1":
      break

    if userInput == word:
      print("you've done it")
      break
    
    if len(userInput) > 1 or userInput in "12346890":
      print("hanya boleh 1 kata dan bukan angka")
    elif userInput in word and userInput != "" and userInput != " ":
      print(f"terdapat {userInput} didalam kata tersebut. (\"close1\" to exit)")
      for i in range(lengthWord):
        if userInput == word[i]:
          guess[i] = userInput
    else:
      print(f"tidak ada {userInput} didalam kata tersebut. (\"close1\" to exit)")
      lifes-=1
      life(lifes)
      if lifes == 0:
        print("you lose")
        break
    
    


main()


