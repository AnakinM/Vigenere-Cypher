def convert_to_string(array): 
    string = ""
    for c in array: 
        string += c    
    return string 

# Open a file with text to encode
f = open("input.txt", "r")

# Read file. delete spaces, new lines and change all letters to lowercase
text = f.read().lower().replace(" ", "").replace('\n', '').replace('\r', '')
f.close()

# Set key
key = "yes"

# Change input text to ascii
text_as_numbers = []
for i in range(len(text)):
    text_as_numbers.append(ord(text[i])-97)

# Change key to ascii
k = []
for i in range(len(key)):
    k.append(ord(key[i])-97)

# Sum text as ascii with key as ascii
i=0
for j in range(len(text_as_numbers)):
    text_as_numbers[j] += k[i]
    if text_as_numbers[j] > 25:
        text_as_numbers[j] -= 26
    i += 1
    if i == len(k):
        i=0

# Change ascii numbers back to letters
numbers_to_text = []
for i in range(len(text_as_numbers)):
    numbers_to_text.append(chr(text_as_numbers[i]+97))

# Convert array of characters to sting
encoded = convert_to_string(numbers_to_text)

# Write encoded text to output file
f = open("output.txt", "w")
f.write(encoded)
f.close()