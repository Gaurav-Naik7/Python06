class Numbers:
    def __init__(self,no):
        self.Value=no

    def ChkPrime(self):
        for i in range(2,self.Value):
            if self.Value%i==0:
                print("False")
                break
        else:
            print("True")

    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if self.Value%i==0:
                sum=sum+i
        return sum

    def ChkPerfect(self):
        if self.Value==self.SumFactors():
            print("True")
        else:
            print("False")

    def Factors(self):
        elist=[]
        for i in range(1,self.Value):
            if self.Value%i==0:
                elist.append(i)
        print(elist)


def main():
    x=int(input("Enter a number: "))
    obj1=Numbers(x)
    obj1.ChkPrime()
    ret=obj1.SumFactors()
    print(ret)
    obj1.ChkPerfect()
    obj1.Factors()

    x=int(input("Enter a number: "))
    obj2=Numbers(x)
    obj2.ChkPrime()
    ret=obj2.SumFactors()
    print(ret)
    obj2.ChkPerfect()
    obj2.Factors()


if __name__=="__main__":
    main()
