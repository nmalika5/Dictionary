# put your code here.
import sys

input_file = open(sys.argv[1])

word_dict = {}
count = 0

for line in input_file:
    for each_word in (line.rstrip().split()):
        each_word = each_word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~').lower()
        count = word_dict.get(each_word, 0) + 1
        word_dict[each_word] = count

# for each_word, count in sorted(word_dict.iteritems(), key = count):
# mini_dict = {}
# for each_word, count in sorted(word_dict.iteritems(), key = lambda x: (x[1], x[0]), reverse = True):
# # for each_word, count in sorted(word_dict.iteritems(), key = lambda x: x[1], reverse = True):
#     # mini_dict[count].append(each_word)

#     print  each_word, count 

new_dict = {}
new_set = set(word_dict.values()) 

for item in new_set:
    new_list = sorted([word for word, count in word_dict.items() if count == item])
    new_dict[item] = new_list
    
for key, list_of_values in sorted(new_dict.iteritems(), reverse = True):
    for value in list_of_values:
        print key, value

    #print each_word, count

