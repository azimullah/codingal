class vehicle:
     def __init__(self, name, max_speed, mileage):
         self.name = name
         self.max_speed = max_speed
         self.mileage = mileage

modelx=vehicle('modelx', 240,18) 
print(modelx.name,"with max speed", modelx.max_speed,"kmph and mileage", modelx.mileage,'kmpl')