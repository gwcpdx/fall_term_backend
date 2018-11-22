## Answers to Lesson 7: While Loops Practice Problems

#### Question 1: Counting
```python
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"
```

#### Question 2: Converting input to lowercase

```python
while True:
    reply = raw_input('Enter text, [type "stop" to quit]: ')
		reply_lowercase = reply.lower()
    print reply_lowercase
    if reply == 'stop':
        break
```

#### Question 3: Guessing Game

```python
import random

number = random.randint(1, 25)
number_of_guesses = 0

while number_of_guesses < 5:
    print('Guess a number between 1 and 25:')
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')

else:
    print('You did not guess the number. The number was ' + str(number))
```
