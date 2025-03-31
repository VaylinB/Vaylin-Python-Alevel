class Employee:
    def __init__(self,HourlyPay,EmployeeNumber,JobTitle):
        self.__HourlyPay = HourlyPay #real
        self.__EmployeeNumber = EmployeeNumber #str
        self.__JobTitle = JobTitle #str
        self.__PayYear2022= [0.00]*52 #array 52 elements of real
    
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber 
    
    def SetPay(self,WeekNum,NumofHours):
        self.__PayYear2022[WeekNum - 1]= NumofHours * self.__HourlyPay
    def GetTotalPay(self):
        Total = 0
        for i in range(len(self.__PayYear2022)):
            Total += self.__PayYear2022[i]
        return Total
            
class Manager(Employee):
    def __init__(self,HourlyPay,EmployeeNumber,JobTitle,BonusValue):
        super().__init__(HourlyPay,EmployeeNumber,JobTitle)
        self.__BonusValue = BonusValue #real

    def SetPay(self, WeekNum, NumofHours):
        NumofHours = NumofHours * (1 + self.__BonusValue /100)
        super().SetPay(WeekNum, NumofHours)

#3c
EmployeeArray = []
try:
    file = open("Employess.txt",'r')
    for x in range(8):
        Pay = float(file.readline())
        ID = file.readline().strip()
        Temp = file.readline().strip()

        try:
            Bonus = float(Temp)
            Title = file.readline().strip()
            EmployeeArray.append(Manager(ID,Pay,Title,Bonus))
        except:
            Title = Temp
            EmployeeArray.append(Employee(ID,Pay,Title,))
    file.close()
except FileNotFoundError:
    print("no file found")
        
#3d
def EnterHours():
    try:
        file = open("HoursWeek1.txt",'r')
        for i in range(8):
            EmployeeNum = file.readline().strip()
            NumofHours = float(file.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber() == EmployeeNum:
                    EmployeeArray[y].SetPay(1,NumofHours)
        file.close()

    except FileNotFoundError:
        print("no file found")

EnterHours()
for i in range(8):
   print(EmployeeArray[i].GetEmployeeNumber(), " ", EmployeeArray[i].GetTotalPay())