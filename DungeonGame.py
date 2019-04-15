import random
import time

def displayIntro():
  print(
    """
You awake to find yourself in a strange forest.
It's night time, and you're not sure how you got here.

The forest behind you is full of dangerous creatures. 
You can see glowing hungry eyes looking out at you. 

In front of you are 2 doors. Door number 1 has a large heart 
carved on the outside. Door number 2 has what looks to be a 
strange skull carved into it. 

    """
  )
def choose(thing):
  choice = ""
  while choice != '1' and choice != '2':
    print("Which " + thing + " will you choose?")
    choice = input()
  return choice

def checkDoor(chosenDoor):
  print("You approach the door...")
  time.sleep(2)
  print("You slowly open the door to see...")
  time.sleep(2)
  if chosenDoor == '1':
    print(
      """
A witch looks up at you from her plate. 

She appears to be eating dinner....

She smiles up at you....

You notice the food on her plate is actually a still-beating
heart. 

=======
THE END
=======
      """
    )

  else:
    print(
      """
A large man with an apron covered in flour. 

He says,

    "Welcome to my muffin shop! Did you recognize the muffin 
  on my door? My wife isn't much of an artist, but she does her best. 
  She lives next door, but leave her be, as she doesnt't like 
  strangers the way I do. 

  Here have one of my muffins for free as a welcome gift.

  I must warn you though, my wife likes to slip potions into 
  some of my muffins."

      """
    )
    time.sleep(8)
    print(
      """
In front of you are 2 muffins. 

Muffin 1 has translucent icing, and purple cake underneath. 

Muffin 2 has a creme cake, bright red top,and white dots.

      """
    )
  
    muffinNumber = choose("muffin")
    checkMuffin(muffinNumber)

def checkMuffin(chosenMuffin):
  if chosenMuffin == '1':
    print("""
The muffin doesn't seem to have much flavor, but you enjoy it anyway.
You notice the baker seems to be looking at you with a worried stare.

You turn to look in a mirror on the wall. 
You see all of your clothes still sitting at the table,
but there doesn't seem to be a person in the clothes.

""")
    time.sleep(8)
    print("Looks like you're invisible. Life is going to be a lot weirder now.")
    print()
    time.sleep(3)
    print("===THE END===")
  else:
    print("""
You feel your hands and feet begin to swell, 
and you can feel a tingling sensation all over your body.
""")
    time.sleep(3)
    print("You feel a bump on your head as you grow through the roof.")
    print("You're still growing as your head is beginning to touch the clouds.")
    print()
    time.sleep(2)
    print("As your head reaches space you notice it's becoming harder to breathe.")
    time.sleep(2)
    print("""
You suffocate due to lack of oxygen outside the atmosphere.

===THE END===
""")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  displayIntro()
  doorNumber = choose("door")
  checkDoor(doorNumber)
  print('Do you want to play again?')
  playAgain = input()