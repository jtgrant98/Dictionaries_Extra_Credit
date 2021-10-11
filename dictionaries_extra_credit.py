keywords = ['Father', 'God', 'Christ', 'Spirit', 'spirit', 'life', 'man']
dict = {}

with open('book of John text.txt', 'r') as f:
    text = f.read().split(' ') 

for word in text:
    dict[word] = dict[word]+1 if word in dict else 1

for x in keywords:
    print(x ,':', dict[x])