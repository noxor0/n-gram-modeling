import sys
import random

bi = {}
probs = {}
with open(sys.argv[1], 'r') as file:
    lines = ''.join(file.readlines()).lower().split()
    for i in range(len(lines)):
        if (i+2 < len(lines)):
            if (lines[i] in bi):
                if (lines[i+1] in bi[lines[i]]):
                    bi[lines[i]][lines[i+1]] += 1
                else:
                    bi[lines[i]][lines[i+1]] = 1
            else:
                bi1 = {}
                bi[lines[i]] = bi1
                bi1[lines[i+1]] = 1

for cnt in range(100):
    key = random.choice(bi.keys())
    key1 = random.choice(bi[key].keys())
    keyprint = key1 + '|' + key

    bicount = 0
    for val in bi[key].keys():
        bicount += bi[key][val]
    # print '{0:22} {1}'.format(keyprint, '{0:.5f}'.format(float(bi[key][key1])/bicount))

print "Ignoring empty lines"
# print probs
with open(sys.argv[2], 'r') as file_in:
    first_lines = file_in.readlines()[7:107]
    first_lines = "".join(first_lines).lower().split('\n')

    for line in first_lines:
        sent_word_cnt = 0
        line_words = line.split()
        sent_prob = 1
        for i in range(len(line_words)):
            sent_word_cnt += 1
            if i+1 < len(line_words):
                bicount = 0
                try:
                    for val in bi[line_words[i]].keys():
                        bicount += bi[line_words[i]][val]
                    word_prob = float(bi[line_words[i]][line_words[i+1]])/bicount
                    sent_prob *= word_prob
                except KeyError:
                    sent_prob *= 0

        if len(line_words) != 0 and sent_prob != 1:
            pass
            if sent_prob == 0:
                print 0
            else:
                print 1/pow(sent_prob, 1.0/len(line_words))
