# Conditionals -- Practice Problems
**(Included as a repl assignment in GWC PDX Class)**

## Question 1: School's out!

Global Warming has caused the weather in Portland to go CRAZY! The principal at your school doesn't know when to cancel school for the day. Luckily, she has you to thank! You're about to build a program that allows your principal to input a temperature and a humidity percentage (both numbers) and tells her if she should cancel school for the day!  Hint: Use conditional statements!

#### PART 1:  Write this program based on the information below!

* If the temperature is 100 degrees or greater, tell the principal to "Cancel School and recommend a good movie". It doesn't matter what the humidity percentage is, 100 degrees is WAY too hot for anyone to be in school!

* else if the temperature is 92 degrees or greater and the humidity percentage is greater than 75, tell the principal to "Cancel school and sports practice! No one deserves to be in this kind of weather!"

* else if the temperature is greater than 88 degrees and the humidity percentage is greater than or equal to 85, tell the principal to "Cancel School, but sports practice is still on!"

* else if the temperature is 75 degrees and the humidity is less than or equal to 65, tell the principal to "Tell Students to enjoy the day off! The weather is too nice to be in school!"

* else if the temperature is less than -25 degrees, tell the principal to "Stay HOME and stay WARM!"

* else if the temperature is less than 0 degrees, "Cancel school!"

* else tell the principal "School is in session"

**Starting code in repl assignment:**

```python
#Set Integers
Temperature = int(input("Enter temperature:"))
Humidity = int(input("Enter humidity percentage:"))

# DO PART 1 ..
```

#### PART 2: Converting to celsius


Awesome! You created a very helpful program for your principal. However, the principal's son gave her chicken pox so she's at home sick for a few weeks. The Vice Principal has to step in. Unfortunately, the vice principal grew up in France and only understands weather in celsius. We need to add in some functionality so she can input a temperature in celsius and find out what it is in fahrenheit, and THEN tell her what if she should cancel school for the day.

Here's the formula for changing degrees from celsius to fahrenheit:

**degrees_fahrenheit = degrees_celsius × 1.8 + 32**

Here's some hints on how to do this:

* We know that the vice principal's input is in celsius. That means the Temperature variable is in degrees celsius. How would we use the formula above to change to degrees_fahrenheit?

## Question 2:  Dog years

Let's calculate how old a dog is in human years!

Take in any dog age from the user and print out to the user how old the dog is in human years!

Here's some information you need to account for:
* A dog who is 1 year old is roughly 14 human years old
* A dog who is 2 years old is roughly 22 human years old
* Every  dog year after 2 years corresponds to five additional human years...
 * HINT: if I were to calculate every dog year after age 2 I need to subtract 2 from the input age, multiply it by 5 and add 22!)
* Don't forget a condition for age less than or equal to 0!

**Starting code in repl assignment:**

```python
age = int(raw_input("Age of the dog: "))

## WRITE YOUR CODE HERE:
```
