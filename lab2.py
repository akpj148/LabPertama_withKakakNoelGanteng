def randomWord(yea):
  words = {
    1: "WALKING",
    2: "TIME",
    3: "FRIEND",
    4: "HELLO",
  }
  return words[yea]

def life(lifes):
  theMan = {
    6: '''
  ____
 /  
 |
/-\\
''',
    5: '''
  ____
 /   O
 |
/-\\
''',
4: '''
  ____
 /   O
 |   |
/-\\
''',

3: '''
  ____
 /   O
 |  /|
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
  yea = 1
  word = randomWord(yea)
  lengthWord = len(word)
  wordGuess = []
  blank = "_"
  guess = []
  lifes = 6

  for i in range(lengthWord):
    guess.append(blank)

  print("given secrete word.(\"close1\" to exit)\n type all the letter to win")
  
  life(lifes)

  y = len(guess)
  while True:
    for i in range(len(guess)):
      print(guess[i]+" ", end="")
    
    print("| words guessed: ",end="")
    for i in range(len(wordGuess)):
      print(wordGuess[i]+" ", end="")
    print("\n")

    if y < 1:
      print("you've done it!")
      break

    userInput = input("guess: ").upper()

    if userInput == "CLOSE1":
      break

    if userInput == word:
      print("you've done it!")
      break
    
    if len(userInput) > 1 or userInput in "12346890":
      print("hanya boleh 1 kata dan bukan angka")
    elif userInput in wordGuess:
      print(f"kata \"{userInput}\" sudah di tebak")
    elif userInput in word and userInput != "" and userInput != " ":
      print(f"terdapat {userInput} didalam kata tersebut. (\"close1\" to exit)")
      for i in range(lengthWord):
        if userInput == word[i]:
          guess[i] = userInput
          y-=1
    else:
      wordGuess.append(userInput)
      print(f"tidak ada {userInput} didalam kata tersebut. (\"close1\" to exit)")
      lifes-=1
      life(lifes)
      if lifes == 0:
        print("you lose")
        break
      
main()