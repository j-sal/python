#s = str(input("Type a string:"))
#s = "Tom", " eats and eats"
s = ["Tom eats and eats"]
d = dict()

for line in s:
    line = line.strip()
    #line = line.lower()
    words = line.split(" ")
    #words = line.split(",")
    #words = line.split(".")

    for word in words:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1

for key in list(d.keys()):
    print(d[key], key)