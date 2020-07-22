# not sure if I understood this task correctly
class mysample:
    def __init__(self):
        self.L = []
        i=0
        while(i<10):
            p=int(input("type a number for the list:"))
            self.L.append(p)
            i+=1
    def show(self):
        print(self.L)
        print("The largest number you typed: ", max(self.L), " and the lowest: ",  min(self.L))  

obj = mysample()
obj.show()