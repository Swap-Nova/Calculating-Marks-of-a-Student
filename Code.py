class student:
    admno=0
    sname=""
    eng=0.0
    math=0.0
    science=0.0
    total=0.0
    
    def takeData(self):
        self.admno=int(input("Enter admission no."))
        self.sname=input("Enter your last name")
        self.eng=float(input("Enter your English marks"))
        self.math=float(input("Enter your Math marks"))
        self.science=float(input("Enter your Science marks"))
    
    def ctotal(self):
        self.total=self.eng+self.math+self.science
        return self.total
    
    def showData(self):
        print("Admission no", self.admno)
        print("Last name", self.sname)
        print("English marks", self.eng)
        print("Math marks", self.math)
        print("Science marks", self.science)
        print("Total marks", self.ctotal())

s=student()
s.takeData()
s.showData()
