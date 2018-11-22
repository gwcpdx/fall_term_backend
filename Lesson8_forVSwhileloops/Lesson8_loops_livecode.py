## Lesson 8 - for loops vs while loops live code examples 

num_list = [10, 20, 30]
num_list_2 = []

# For loop
for number in num_list:
  num_list_2.append(number + 5)

print num_list_2

#While loop
length_num_list = len(num_list)
number_index = 0

while number_index < length_num_list:
  
  temp_number = num_list[number_index]
  num_list_2.append(temp_number + 5)
  number_index = number_index + 1
  
print num_list_2
