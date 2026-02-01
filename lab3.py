def randomWord(yea):
  words = {
    1: "WALKING",
    2: "PAN",
    3: "HELLO"
  }
  while yea > len(words):
    yea -=len(words)
  return words[yea]
#-----------------------------------------------
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
#-------------------------------------------------------------------------------
def main(word = "HELLO"):
  word = word.upper()
  lw = len(word)
  wordGuess = []
  blank = "_"
  guess = []
  lifes = 6

  #uhh make _ _ _ _ _
  for i in range(lw):
    guess.append(blank)

  print("---------------------------------------\ngiven secrete word.(\"close1\" to exit)\n type all the letter to win")
  
  # print hangman life
  life(lifes)

  # y for check how many word havent guess
  y = len(guess)

  
  while True:
    # basic layout
    for i in range(len(guess)):
      print(guess[i]+" ", end="")
    
    print("| words guessed: ",end="")
    for i in range(len(wordGuess)):
      print(wordGuess[i]+" ", end="")
    print("")

    if y < 1:
      print("--------- you've done it! ---------\n---------------------------------------------")
      #yea+=1
      #main(yea)
      break

    userInput = input("guess: ").upper()

    if userInput == "CLOSE1":
      return 0

      # optional
    if userInput == word:
      print("--------- you've done it! ---------\n---------------------------------------------")
      #yea+=1
      #main(yea)
      break
    
    #type check
    if len(userInput) > 1 or userInput in "12346890-=_+[]\;',./\{\}|::\"<>?!@#$%^&*()~`" or userInput == " ":
      print("hanya boleh 1 kata dan bukan angka atau simbol (\"close1\" to exit)")
    #check if guessed word is typed again
    elif userInput in wordGuess:
      print(f"kata \"{userInput}\" sudah di tebak (\"close1\" to exit)")
    # check if input in word
    elif userInput in word:
      print(f"terdapat {userInput} didalam kata tersebut. (\"close1\" to exit)")
      for i in range(lw):
        if userInput == word[i] and guess[i] == "_":
          guess[i] = userInput
          y-=1
    else:
      wordGuess.append(userInput)
      print(f"tidak ada {userInput} didalam kata tersebut. (\"close1\" to exit)")
      lifes-=1
      life(lifes)
      if lifes <= 0:
        print("--------- you lose ---------")
        break
      
main("Hari")