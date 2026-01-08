import random

def start():
  print("Start?")


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

def main():
  word = randomWord()
  lengthWord = len(word)
  blank = "_"
  guess = []
  for i in range(lengthWord):
    guess.append(blank)

  print("given secrete word.(\"close1\" to exit)")

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

    if userInput in word:
      print(f"terdapat {userInput} didalam kata tersebut. (\"close1\" to exit)")
      for i in range(lengthWord):
        if userInput == word[i]:
          guess[i] = userInput
    else:
      print(f"tidak ada {userInput} didalam kata tersebut. (\"close1\" to exit)")
    


main()


