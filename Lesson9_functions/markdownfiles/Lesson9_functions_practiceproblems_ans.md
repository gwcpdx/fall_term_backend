
# Answers to Lesson 9: Functions Practice Problems
**(Included as a repl assignment in GWC PDX Class)**

### Question 1: Absolute Values!

```python
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		num = num
	else:
		num = num * -1

  return num
```

### Question 2: Largest of two numbers

```python
def max_of_two( x, y ):
    if x > y:
        return x
    else:
    	   return y

def max_of_three( x, y, z ):
    max_XY = max_of_two( x , y )
    max_XYZ = max_of_two( max_XY, z )
    return max_XYZ
```

### Question 3: Get Unique Numbers

```python
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
```

### Question 4: Tic-Tac-Toe

```python
import sys

player1 = input("What's your name, Player 1?")
player2 = input("And your name, Player 2?")

player1_answer = input("%s, do you want to choose rock, paper or scissors?" % player1)
player2_answer = input("%s, do you want to choose rock, paper or scissors?" % player2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

```
