txt=str(input("\nType a string:"))
#i = ''
count = 0
for i in txt:
    if i == 'a':
        count= count+1
    elif i == 'e':
        count = count+1
    elif i == 'i':
        count = count +1
    elif i == 'o':
        count = count +1
    elif i == 'u':
        count = count +1

print("\nThe amount of vowels on that string is:")
print(count)
