class Another:
    def __init__(self):
        self.car = []
        
    def __len__(self):
        return len(self.car)
    
    def __getitem__(self,i):
        return (self.car[i])
    
ford = Another()
ford.car.append("fiesta")
ford.car.append("focus")
print(ford.car)