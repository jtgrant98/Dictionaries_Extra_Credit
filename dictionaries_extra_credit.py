keywords = ['Father', 'God', 'Christ', 'Spirit', 'spirit', 'life', 'man']
worddict = {}

with open('book of John text.txt', 'r') as f:
    text = f.read().split(' ') 

for word in text:
    worddict[word] = worddict[word]+1 if word in worddict else 1

for x in keywords:
    print(x ,':', worddict[x])