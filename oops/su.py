class Stack:
    def __init__(self):
      self.queue = [];

    def push(self,x):
        self.queue.append(x)

    def pop(self):
        self.queue.pop()1


    def display(self):
        print(self.queue)
try:
  while 1:
   print("1-Create Stack \n 2-Push \n 3-Pop \n 4-display\n 5-exit \nenter choice\n")
   case = int(input("Enter NUmber"))

   m=Stack()
   print("Stack created")
   if case == 1:
    print("Enter Element to push")
    x=int(input("Enter to push"))
    m.push(x)
   elif case == 2:
      n=m.pop()
      print("Ele poped ",n)
   elif case == 3:
      m.display()
   else:
      exit()
except ValueError:
    print("Invalid number")


