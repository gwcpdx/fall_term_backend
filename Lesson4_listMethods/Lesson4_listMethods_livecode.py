# Lesson 4 - List Methods living coding examples 

cities = ["Portland", "Vancouver", "Eugene", "Seattle", "Boring", "Beaverton"]

# Add one item to the list
one_state = 'Alaska'
cities.append(one_state)
print cities

# Add a LIST to an existing list!
states_list = ["Oregon", "Washington", "California", "New York", "Georgia"]

cities.append(states_list)
print cities

# Concatenating lists
all_the_cities = ["NYC", "Nashville", "Austin", "San Francisco"]

many_many_cities = all_the_cities + cities
print many_many_cities
