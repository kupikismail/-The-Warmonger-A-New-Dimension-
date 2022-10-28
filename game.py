
class Faction():  #Here we created a parent class for factions
    def __init__(self,name="Orcs", number_of_units= 50, attack_point=30, health_point=150,unit_regeneration_number=10 ): #we created some common attributes(If not specified, the values to the right of the equation will be used.)
        self.name = name  #one of the orcs, elves, and dwarves
        self.number_of_units = number_of_units
        self.attack_points = attack_point
        self._health_points = health_point
        self.total_health_points = self._health_points * self.number_of_units
        self.unit_regeneration_number = unit_regeneration_number
        self.alive = True
        self.AssignEnemies() #In this function we created below, we created the enemies according to the name of faction.
    def AssignEnemies(self):
        self.all_factions = ["Orcs", "Dwarves", "Elves" ]
        self.all_factions.remove(self.name)
        self.enemy1 = self.all_factions[0]
        self.enemy2 = self.all_factions[1]

    def PerformAttack(self): #we will create in the future
        pass
    
    def ReceiveAttack(self): #we will create in the future
        pass
    
    def PurchaseArmors(self): #we will create in the future
        pass
    
    def Print(self):#we will create in the future
        pass
        
        
    
        


Faction1 = Faction()




        

