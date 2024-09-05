def reverse_words(file_name):


  with open(file_name, "r") as f:
    text = f.read()


  words = text.split()


  reversed_words = words[::-1]


  reversed_text = " ".join(reversed_words)
 
  with open(file_name, "w") as f:
    f.write(reversed_text)

if __name__ == "__main__":


  reverse_words("sample.txt")