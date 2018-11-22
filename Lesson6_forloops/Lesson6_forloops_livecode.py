# Lesson 6 - for loops live coding examples

# Let's review how to print each item one at a time in a list.
amounts = [1,2,3,4,5]

print(amounts)
print(amounts[0])
print(amounts[1])


# This takes a really long time and it's a lot of typing.  I want to print all the elements in amounts one at a time, but this time, I want the computer to do it for me.  Let's use a for loop!

for a in amounts:
  print(a)


# Now I want to multiply each amount by 2 and print it, but again, I want the computer to do it for me.

for a in amounts:
  b = a*2
  print(b)


# Now I want to multiply each amount by 2 store it in a list and then print the list!

amounts_doubled = []

for a in amounts:
  b = a*2
  amounts_doubled.append(b)

print(amounts_doubled)


# Now I want to multiply each amount by 2 and print it, except if the amount is equal to 3

for a in amounts:
  if a == 3:
    continue
  else:
    b = a * 2

  print(b)  

# or another way is...

for a in amounts:
  if (a != 3):
    b = a * 2
    print(b)


# Now I want to multiply each amount by 2 and print it until the amount is 3.  Then i'm done with looping through my list

for a in amounts:
  if a == 3:
    break
  else:
    b = a * 2
  print(b)


# Now I want to try out nested for loops!
amounts = [1,2,3,4,5493, 56927, 95616]
price = [5,10,15]

for a in amounts:
  print("a = ", a)

  for p in price:
    
    M = a * p
    print M
