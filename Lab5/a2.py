class Owner():
    def __init__(self,name,address,profession,license_number):
        self.name=name
        self.address=address
        self.profession=profession
        self.license_number=license_number
        
    def displayOwner(self):
        print(f"OWNER\nName: {self.name}\nAddress: {self.address}\nProfession: {self.profession}\nLicense Number: {self.license_number}")        

class Car():
    def __init__(self,engine_number,regno,regdate,color,owner,model):
        self.engine_number=engine_number
        self.regno=regno
        self.regdate=regdate
        self.color=color
        self.owner=owner
        self.model=model
    
    def displayCar(self):
        print(f"CAR DETAILS\nEngine Number: {self.engine_number}\nRegistration Number: {self.regno}\nRegistration Date: {self.regdate}\nColor: {self.color}\nModel: {self.model}\n")
        self.owner.displayOwner()
            
if __name__=='__main__':
    own = Owner('Rishabh','Delhi','Engineer','UK-129827')
    car = Car('N-93234','37429394243944','10/12/2022','Red',own,'Maruti Suzuki 800')
    car.displayCar()