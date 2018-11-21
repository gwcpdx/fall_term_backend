## Answers to Lesson 5: Conditionals Practice Problems

#############################
## Question 1:  School's Out
#############################

# Set Integers
Temperature = int(input("Enter temperature:"))
Humidity = int(input("Enter humidity percentage:"))

### PART 2 ### -- added after doing Part 1

Temperature = (Temperature * 1.8) + 32

print("The temperature in fahrenheit is :", Temperature)

### PART 1 ###

if Temperature >= 100:
    print("Cancel School, and recommend a good movie")

elif Temperature >= 92:
  if Humidity > 75:
	print("Cancel school and sports practice!  No one deserves to be in this kind of weather!")

elif Temperature > 88:
	if Humidity >= 85:
   		print("Cancel School, but sports practice is still on!")

elif Temperature == 75:
	if Humidity <= 65:
   		print("Tell Students to enjoy the day off!  The weather is too nice to be in school!")

elif Temperature <= -25:
    print ("Stay HOME and stay WARM!")

elif Temperature < 0:
   		print("Cancel school!")

else:
	print("School is in session.")


### PART 1 can also be this:

if Temperature >= 100:
    print("Cancel School, and recommend a good movie")

elif Temperature >= 92 and Humidity > 75:
	print("Cancel school and sports practice!  No one deserves to be in this kind of weather!")

elif Temperature > 88 and Humidity >= 85:
   		print("Cancel School, but sports practice is still on!")

elif Temperature == 75 and Humidity <= 65:
   		print("Tell Students to enjoy the day off!  The weather is too nice to be in school!")

elif Temperature <= -25:
    print ("Stay HOME and stay WARM!")

elif Temperature < 0:
   		print("Cancel school!")

else:
	print("School is in session.")


#############################
## Question 2:  Dog Years!
#############################

age = int(raw_input("Age of the dog: "))

## WRITE YOUR CODE HERE:
if (age == 1):
  print ("Roughly 14 years old")
elif (age == 2):
    print ("Roughly 22 years old")
elif (age > 2):
    print ((age - 2)* 5 + 22)
elif (age <= 0 ):
    print ("Less than 14 years old")
