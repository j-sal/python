# Print a count of all the different "words" in a text file

# Open the file in read mode 
text = open("sample.txt", "r") 

# For local testing without a file
#text = "mango","apple", "mango", "the mango" 

d = dict() 
  
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    for word in words: 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
for key in list(d.keys()): 
    print(d[key], key)