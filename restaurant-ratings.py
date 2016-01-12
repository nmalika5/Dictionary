# your code goes here
import sys
import random

file_name = open(sys.argv[1])

restaurant_dict = {}


for line in file_name:
    name, rating = line.strip().split(":")
    restaurant_dict[name] = rating

greeting = raw_input("Hi! What's your name: ")
print "Hello %s, " % greeting


while True:
    rand_rest = random.choice(restaurant_dict.keys())
    print "%s has the following %s" % (rand_rest, restaurant_dict[rand_rest])
    try:
        new_rest_score = int(raw_input("Enter a new score for this restaurant from 1 to 5: "))
        if new_rest_score > 5 or new_rest_score < 1:
            print "Out of range, select the valid score"
            break
        restaurant_dict[rand_rest] = new_rest_score
    except ValueError:

def print_restaurants():
    for name, rating in sorted(restaurant_dict.iteritems()):
        print "%s is rated at %s." % (name, rating)   
        break

print_restaurants()
# new_rest_name = raw_input("Enter a new restaurant: ")

# restaurant_dict[new_rest_name] = new_rest_score