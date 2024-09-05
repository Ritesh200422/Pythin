filename = input ("Enter file name")

try:
    fd =open(filename,"r")
    data=fd.read()
    fd.close()
except FileNotFoundError:
    print("File not exists")
else:
    freq=dict()
    for letter in data:
        if letter in freq:
            freq[letter] += 1;
        else:
            freq[letter] =1
    for key, value in freq.items():
        print(f"Char {key} Occurs :{value} times")
