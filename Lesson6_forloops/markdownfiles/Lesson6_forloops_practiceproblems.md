
# For Loops -- Practice Problems
**(Included as a repl assignment in GWC PDX Class)**

## Question 1: Printing months
Write a Python program that prints all the words in the list, MONTHS, by iterating through a loop.

For this problem, fill in the '____' with the correct code.

**Starting code in repl assignment:**

```python
# List of months
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# For loop to print each month
for i in MONTHS:
  #print month
	print( _____ )
```

## Question 2: Printing numbers
Write a Python program that prints all the numbers from 0 to 10 except 3 and 6 and appends each number to the new list, called myList.

**Hint:**
* Fill in the '____' with the correct code.

**Bonus Questions:**
 1. Why is the range from 0 to 11?  Why not 0 to 10?

**Starting code in repl assignment:**

```python
# Initiate empty list
myList = []

#For loop to iterate through
for x in range(0, 11):
  if (x != _______ and x != _______ ):
    myList.append( _______ )

print( _______ )

"""
ANSWER TO BONUS QUESTION 1: (type it out below)


"""
```

## Question 3: The Famous Fizz Buzz Problem!
Write a Python program that loops through integers 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

For this problem, fill in the '____' with the correct code.

**Hint:**
* i % 3 == 0 is the code to check if a number is a multiple of 3
* i % 5 == 0 is the code to check if a number is a multiple of 5

**Starting code in repl assignment:**
```python
for _______ in range( _______ ):

  if ( _______ and _______ ):
    print( _______ )
    continue

  elif ( _______ ):
    print( _______ )
    continue

  elif ( _______ ):
    print( _______ )
    continue

  else:
    print( _______ )
```


## Question 4: Finding even numbers
Loop through the 'all_numbers' list and and save all even numbers to a new list called 'even_numbers'   in the same order they are received. Don't save any numbers that come after 237 in the sequence.  At the end print 'even_numbers'

**Hint:**
* You'll need to use conditionals here too

**BONUS QUESTIONS:**

1. How many elements are in 'all_numbers'?  How many elements are in 'even_numbers' Don't count it by hand!  You know how to do this programmatically!  Also - don't forget to use the print statement so it prints to the console.

2.  So we know how to access a list if we know it's index.  But what if we want to know the index of a particular element in the list?  We can use a new list method called .index():

  ```python
  LIST_NAME.index(ELEMENT_VALUE)
  ```

  I've given you the generic form of how to use the .index() list method.  How would you use this to find the index for 237 in 'all_numbers'?

**Starting code in repl assignment:**
```Python
# My list called numbers
all_numbers = [951, 402, 984, 651, 360, 69, 408,
319, 601, 485, 980, 507, 725, 547, 544, 615,
83, 165, 141, 501, 263, 617, 865, 575, 219, 390,
984, 592, 236, 105, 942, 941,386, 462, 47, 418,
907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345,399, 162, 758, 219, 918, 237, 412, 566,
826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
843, 831, 445, 742, 717, 958, 609, 842, 451, 688,
753, 854, 685, 93, 857, 440, 380, 126, 721, 328,
753, 470, 743, 527]

# Initiate even list

# Write your for loop below!



# Answer Bonus Question 1 here:



# Answer Bonus Question 2 here:


```

## Question 5: Star flag (Nested Loops)

Make a play button of stars by using nested for loops!

**Expected Output:**
```
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
```

**Hint:**
* You will need two nested loops!
* You'll use the range function!
* You'll notice at the end of the print statement there is a ```,```.  This is **not** a typo.  Don't delete it.  Instead this is a weird python 2.7 syntax.  (If you want to see waht it does, delete it and run your code, but don't forget to put it back before you submit your answer!)

**Starting code in repl assignment:**
```python
n=5
star = '* '
newline = ''

# Let's do the first half here:

# Write the first for loop statement: HINT: What is your range?
#   Remember that the syntax for range:   range(start, stop, step)

  # Write your nested loop here:  HINT: Now What is your range?


      #What do you want to print
      print(_________),  # fill in the blank here
    # What do you want to print so you can go to the next line?



#Now we need to step down to do the bottom half of the play button.  Try it out!

#  HINT: The code is pretty similar to what we just did

```
