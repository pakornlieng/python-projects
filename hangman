from random import randint as r

hangman = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']
#word list
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

class main:
   def __init__(self):
      H.game()
      



class H:
   def game():
      while True:
         ans = input("Would you like to play hangman? (y/n) \n")
         ans.lower()
         if ans == "yes" or ans == "y":
            H.hangman()
            break
         elif ans == "no" or ans == "n":
            print("Thank you for stopping by!!!")
            break
         else:
            print("Invalid Input >:( \n \n \n \n \n . . . try again -_-")
            
      

   

   def hangman():
      #variables such as what word is being played and having that be joined with " " to create a less cluttered feel in the terminal 
      word = r(0, len(words)- 1)
      game_word = words[word]
      #check = " ".join(game_word)
      answer = " ".join("_" * len(game_word))
      output = list(answer)
      used = []
      
      #output = list(" ".join(answer))
      pool = list(" ".join(game_word))
      wrong = 0
      checked = False 

      #print variables to check output
      #print(game_word)

      #gives out what the prompt is
      print("Your word is {}".format(answer))
      

      #this is the main game
      while True:  
         letter = input("Guess a letter: \n")
         letter.lower()
         
         checked = H.letterUsed(letter, used, wrong)
         
         if checked == True:
            if letter in pool:
               i = 0
               #supposed to change the letters in the output to the ones that are guessed
               #checks if the letter guessed is equal to which character at what index in the correct answer 
               while i < len(pool):
                  if pool[i] == letter:
                     output[i] = letter
                     output2 = "".join(output)
                  i += 1
               #prints the hangman and current output onto the terminal
               print(hangman[wrong])
               print(output2)
            
            else:
               #if the guessed letter is wrong this displays the same thing except hangman moves up a stage 
               wrong += 1
               output2 = "".join(output)
               print("\nWRONGGGG\nGuess again :DD")
               print(hangman[wrong])
               print(output2, "\n")
         
         #checks if the game is lost
         if wrong == 6:
            print("Game over :(( \nYour word was {} \n".format(game_word))
            break

         win = output2.replace(" ", "")
         if win == game_word:
            
            print("VICTORY!!!!")
            print("Your word was {}".format(game_word))
            print("\n\nHope you come play again :DDD")
            break
        
   def letterUsed(guess, used, wrong):
         #contains a list of used letters called used
         
         #checks if the guess has been used
         if guess in used:
            
            #if so should print the following and return false
            print("HEY! You alrady used that letter guess again -_-")
            
            return False
         elif guess == " " or guess.isdigit() == True or len(guess) > 1:
            #if it's an invalid entry then the following should print and return false 
            print("HEY! That's not a letter!!\n\n\nIt's still wrong -_-\nGuess Again :D ")
            wrong += 1
            return False
         
         #print("i am adding a character to the list ")
         #used.append(guess)
         used.append(guess)
         return True
         


main()
      
   
