
# While Loops -- Practice Problems
**(Included as a repl assignment in GWC PDX Class)**

## Question 1: Counting
Use a WHILE loop to count from 0 to 10.  The output should write 'The Count is: X", where X is a given number from 1 to 10.

For this problem, fill in the '____' with the correct code.

**OUTPUT SHOULD LOOK LIKE:**
```
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
The count is: 9
The count is: 10
Good bye!
```

**Starting code in repl assignment:**

```python
## Initialize counter
count = 0

## Start while loop by setting up the condution
while (count < _____):
	## Print the count
  print 'The count is:', _____
	## Update the counter!
  _____ = _____ + 1

print "Good bye!"
```

## Question 2: Converting input to lowercase
Write a WHILE LOOP that accepts input from the user and converts the text inputted by the user to all lowercase and outputs what the user typed in.  Prompt the user to 'stop' and end the program.

**Example Output:**

```
Enter text, [type "stop" to quit]: hi
hi
Enter text, [type "stop" to quit]: Minnie Mouse
minnie mouse
Enter text, [type "stop" to quit]: stop
stop
```

**Hint:**
* Fill in the '____' with the correct code.

**Bonus Question:**
1. Can you think of a problem where converting user input to a uniform format could be useful?


**Starting code in repl assignment:**

```python
while True:
    reply = raw_input('Enter text, [type "stop" to quit]: ')
    reply_lowercase = ____
    print ____
    if ____ == ____:
        break

"""
ANSWER TO BONUS QUESTION 1: (type it out below)


"""
```

## Question 3: Guessing Game
Let's make a guessing game!

Prompt a player to guess a number between 1 and 25 that is randomly generated by the computer!

* The player has only 5 tries!
* While the player is playing the game, tell him/her if their guess was too low or too high.
* If the player gets the correct number, tell the player how many guesses it took them to get the answer.
* If the player fails to guess the correct number within 5 tries, tell them they did not guess the number, and tell them what the correct number was.

**Hint:**
* You will need to use conditional statements.

**Starting code in repl assignment:**
```python

# We started you off by importing the 'random' package.
#     This package allows us to use the random.randint
#     function so the computer can generate a number
#     between two values we give it.
import random

# Using the random.randint package to generate a number
#    between 1 and 25.
# This is the number we want the player to guess!
number = random.randint(1, 25)

#Initializing our counter!  We have to set it to zero!
number_of_guesses = 0


#Start of the while loop.  It says while number_of_guesses
#    is less than 5 (the number of tries we are requiring
#    for the game) , do stuff!!  That's for you to try!
#    Go for it!

```