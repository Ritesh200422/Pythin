fname=input ("Enter filename")
try:
    fhand = open(fname)
    d1 = dict()
    for line in fhand:
        words=line.split()
        for word in words:
            if word in d1:
                d1[word]=d1[word] + 1
            else:
                d1[word] =1
    print(d1)
except:
    print("File Not Found")