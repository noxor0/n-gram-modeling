import sys

uni = {}
probs = {}
with open(sys.argv[1], 'r') as file_in:
    lines = "".join(file_in.readlines()).lower().split()
    wordcnt = len(lines)
    for word in lines:
        if word not in uni:
            uni[word] = 1
        else:
            uni[word] += 1

    for key in uni:
        probs[key] = float(uni[key])/wordcnt
        # print '{0:10} {1}'.format(key, '{0:.9f}'.format(float(uni[key])/wordcnt))

print "Ignoring empty lines"
# print probs
with open(sys.argv[1], 'r') as file_in:
    first_lines = file_in.readlines()[7:107]
    first_lines = "".join(first_lines).lower().split('\n')

    for line in first_lines:
        sent_prob = 1
        sent_word_cnt = 0
        for word in line.split():
            sent_word_cnt += 1
            sent_prob *= probs[word]
        # print sent_prob
        if sent_prob != 1:
            pass
            print 1/pow(sent_prob, 1.0/len(line))
