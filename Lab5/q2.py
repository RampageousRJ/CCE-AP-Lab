class Vehicle():
    def __init__(self):
        self.vid=int(input('Enter VID: '))
        self.name=input("Enter name: ")
        self.owner=input("Enter owner name: ")
    def display(self):
        print(f'VEHICLE\nID: {self.vid}\nName: {self.name}\nOwner: {self.owner}\n\n')
        
class Passenger(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_of_passengers=int(input('Enter number of passengers: '))
    def display(self):
        print(f'PASSENGER\nID: {self.vid}\nName: {self.name}\nOwner: {self.owner}\nNumber of Passengers: {self.num_of_passengers}') 

if __name__=='__main__':
    v = Vehicle()
    v.display()
    p = Passenger()
    p.display()