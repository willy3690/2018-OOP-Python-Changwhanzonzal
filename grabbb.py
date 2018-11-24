import random
fp = open('pyprowords.txt', 'r')
wordlist=[]
for line in fp:
    wordlist.append(line.strip())
random.shuffle(wordlist)
print(wordlist[0])