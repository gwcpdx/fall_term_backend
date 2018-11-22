## Answers to Lesson 6: For Loops Practice Problems

#### Question 1: Printing months
```python
# list of months
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# For loop to print each month
for i in MONTHS:
  #print month
	print( i )
```

#### Question 2: Printing numbers

```python
# Initiate empty list
myList = []

#For loop to iterate through
for x in range(0, 11):
  if (x != 3 and x != 6 ):
    myList.append(x)

print( myList )


"""
ANSWER TO BONUS QUESTION 1: (type it out below)

Because the range function accepts the
following parameters of range(start,stop),
but the stop argument doesn't include that
number so we have to set range(0,11) if we
want to go to 10.
"""
```

#### Question 3: The Famous Fizz Buzz Problem!

```python
for i in range(51):

  if (i % 3 == 0 and i % 5 == 0):
    print( “FizzBuzz” )
    continue

  elif (i % 3 == 0):
    print( “Fizz”)
    continue

  elif (i % 5 == 0):
    print(“Buzz”)
    continue

  print(i)
```

#### Question 4: Finding even numbers

```python
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
even_numbers = []

# Write your for loop below!
# Hint: you'll need to use conditional statements too!
for n in all_numbers:

    if n == 237:
        break

    if n % 2 == 0:
        even_numbers.append(n)

	## NOTE FOR INSTRUCTOR: ELSE STATEMENT IS OPTIONAL
    else:
      continue

#Answer Bonus Question 1 here:

print(len(all_numbers))
print(len(even_numbers))


# Answer Bonus Question 2 here:

print(all_numbers.index(237))

```

#### Question 5: Star flag (Nested Loops)

```python
n=5
star = '* '
newline = ''

# Let’s do the first half here:

# Write the first for loop statement: HINT: What is your range?
#   Remember that the syntax for range:   range(start, stop, step)
#
for i in range(0, n, 1 ):

    # Write your nested loop here:  HINT: Now What is your range?

    for j in range(0, i, 1):

      #What do you want to print

        print(star),

    #What do you want to print so you can go to the next line?
    print(newline)

#Now we need to step down to do the bottom half of the play button.  Try it out!
#  HINT, the code is pretty similar to what we did
for i in range(n,0,-1):
    for j in range(0, i, 1):
        print(star),
    print(newline)
```
