

#day 1 hesap makinesi

class HesapMakinesi():
    def __init__(self,sayı1,sayı2,Hangiİşlem):
        
        self.sayı1=sayı1
        self.sayı2=sayı2
        self.Hangiİşlem=Hangiİşlem
    def hesaplama(self):
        if self.Hangiİşlem=="+":
            return self.sayı1+self.sayı2
        elif self.Hangiİşlem=="-":
            return self.sayı1-self.sayı2
        elif self.Hangiİşlem=="*":
            return self.sayı1*self.sayı2
        elif self.Hangiİşlem=="/":
            return self.sayı1/self.sayı2
        else :
            return print("hatalı işlem")
        
islem=HesapMakinesi(3, 7,'*')
result=islem.hesaplama()
print(result)
