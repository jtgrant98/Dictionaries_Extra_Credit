#get file object reference to the file
file = open("book of John text.txt", "r")
#read content of file to string
data = file.read()
#get number of occurrences of the substring in the string
Father = data.count("Father")
God = data.count("God")
Christ = data.count("Christ")
Spirit = data.count("Spirit")
spirit = data.count("spirit")
life = data.count("life")
man = data.count("man")

print('Father :', Father)
print('God :', God)
print('Christ :', Christ)
print('Spirit :', Spirit)
print('spirit :', spirit)
print('life :', life)
print('man :', man)
