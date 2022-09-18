#Multiple inheritance
#A-->C<--B
class Mark:
    def getdata(self):
        self.m=int(input("Enter the mark"))
    def printdata(self):
        print("Mark is",self.m)
class Garcemark:
    def getmark(self):
        self.gm=int(input("Enter the gracemark"))
    def printmark(self):
        print("Grace mark is",self.gm)
class Grade(Mark,Garcemark):
    def calculate(self):
        if(self.m>500 or self.gm>100):
            print("Wrong data")
        else:
            Total=self.m+self.gm
            print("Total mark is",Total)
            p=Total/500*100
            print("Percentage is",p)
            if (p >= 80):
                print("Grade A")
            elif (p >= 70):
                print("Grade B")
            elif (p >= 60):
                print("Grade C")
            elif (p >= 50):
                print("Grade D")
            else:
                print("Failed")

std1=Grade()
std1.getdata()
std1.getmark()
std1.printdata()
std1.printmark()
std1.calculate()
