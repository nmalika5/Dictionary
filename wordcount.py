# put your code here.
input_file = open('test.txt')

word_dict = {}
count = 0

for line in input_file:
    for each_word in (line.rstrip().split()):
        count = word_dict.get(each_word, 0) + 1
        word_dict[each_word] = count
for each_word, count in word_dict:
    print count, each_word  
