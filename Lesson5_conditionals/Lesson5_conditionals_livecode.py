# Lesson 5 Conditionals - live code examples
snack = "pretzels"

if snack == "pretzels":
  print "I LOVE PRETZELS"
else:
  print "Hmmmm, I really wish I just had pretzels!"

snack = "oranges"

if snack == "pretzels":
  print "I LOVE PRETZELS"
else:
  print "Hmmmm, I really wish I just had pretzels!"


# snack = "pretzels"
# snack = "oranges"
# snack = "jelly beans"
# snack = "orange"
# snack = "chocolate"

if snack == "pretzels":
  print "I LOVE PRETZELS"
elif snack == "oranges" or snack == "orange":
  print "ORANGES ARE GREAT! Vitamin C? Yes, please."
elif snack == "chocolate":
  print("Jenn loves " + snack + "!")
else:
  print "Hmmmm, I really wish I just had pretzels and oranges."
