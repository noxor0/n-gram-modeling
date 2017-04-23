import sys
import random
import re

bi = {}

with open(sys.argv[1], 'r') as file:
    lines = ''.join(file.readlines()).lower().split()
    for i in range(len(lines)):
        if (i+2 < len(lines)):
            if (lines[i] in bi):
                if (lines[i+1] in bi[lines[i]]):
                    bi[lines[i]][lines[i+1]] += 1
                else:
                    bi[lines[i]][lines[i+1]] = 1.1
            else:
                bi1 = {}
                bi[lines[i]] = bi1
                bi1[lines[i+1]] = 1.1

# with open(sys.argv[2], 'r') as file:
#     lines = ''.join(file.readlines()).split('\n')
#     lines = lines[:len(lines)-1]
#     for line in lines:
#         regex = re.search('(\w+)\|(\w+)', line)
#         key = regex.group(2)
#         key1 = regex.group(1)
#         keyprint = key1 + '|' + key
#         bicount = 0
#         for val in bi[key].keys():
#             bicount += bi[key][val]
#
#        print '{0:22} {1}'.format(keyprint, '{0:.5f}'.format(float(bi[key][key1])/bicount))

print "Ignoring empty lines"
with open(sys.argv[2], 'r') as file_in:
    first_lines = file_in.readlines()[7:107]
    first_lines = "".join(first_lines).lower().split('\n')

    for line in first_lines:
        sent_prob = 1
        line_words = line.split()
        for i in range(len(line_words)):
            if i+1 < len(line_words):
                bicount = 0
                if line_words[i] in bi:
                    for val in bi[line_words[i]].keys():
                        bicount += bi[line_words[i]][val]
                    if line_words[i+1] in bi[line_words[i]]:
                        word_prob = float(bi[line_words[i]][line_words[i+1]])/bicount
                        sent_prob *= word_prob
                    else:
                        sent_prob *= .1
                        break
                else:
                    sent_prob *= .1
                    break
        if len(line_words) != 0 and sent_prob != 1:
            if sent_prob == 0:
                print 0
            else:
                print 1/pow(sent_prob, 1.0/len(line_words))
