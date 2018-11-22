
# Answers to Lesson 8: For vs While Loops Practice Problems
**(Included as a repl assignment in GWC PDX Class)**

### Question 1: Filtering Numbers

```python
master_list = [1, 47, 2, -10, 5, 3, 8, 13, 21, 34, 55, 89]

# Create a variable called max_number can assign it to 20
max_number = 20

# Initiate your new list, called small_list
small_list = []

# FOR LOOP VERSION

for num in master_list:
	if num < 20:
		small_list.append(num)

print small_list

# WHILE LOOP VERSION
num_index = 0
while num_index < len(master_list):
	if master_list[num_index] < max_number:
		small_list.append( master_list[num_index] )
	num_index = num_index + 1
print small_list


# Create a new object of a sorted small list
sorted_small_list = sorted(small_list)
print(sorted_small_list)

# Print the sum of sorted_small_list
print(sum(sorted_small_list))
```
