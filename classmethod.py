good_employees=[]
bad_employees=[]
for i in range (4):
    class Employee:
        __id=0
        __name=""
        __gender=""
        __city=""
        __salary=0
        def setData(self): 
            self.__id=int(input("Enter Id\t:"))
            self.__name = input("Enter Name\t:")
            self.__gender = input("Enter Gender:")
            self.__city = input("Enter City\t:")
            self.__salary = int(input("Enter Salary:"))
            if (self.__salary<29):
                good_employees.append(self.__name)
                print("Employee Added in Good")
            else:
                bad_employees.append(self.__name)
                print("Employee Added in bad")
        def showData(self):
                print("Id\t\t:",self.__id)
                print("Name\t:", self.__name)
                print("Gender\t:", self.__gender)
                print("City\t:", self.__city)
                print("Salary\t:", self.__salary)
    def main():
        #Employee Object
        emp=Employee()
        emp.setData()
    if __name__=="__main__":
        main()
print("Employee is GOOD", good_employees)
print("Employee is BAD", bad_employees)
