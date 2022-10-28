
class Faction():  #Here we created a parent class for factions
    def __init__(self,name="Orcs", number_of_units= 50, attack_point=30, health_point=150,unit_regeneration_number=10 ): #we created some common attributes(If not specified, the values to the right of the equation will be used.)
        self.name = name  #one of the orcs, elves, and dwarves
        self.number_of_units = number_of_units
        self.attack_points = attack_point
        self._health_points = health_point
        self.total_health_points = self._health_points * self.number_of_units #(note: don't forget to update the total health point according to the updated number of units and health points)
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
        

class Orcs(Faction): # orcs child class created,all features and functions defined in the Faction class have been made available
    def __init__(self): #We can use the features in the faction class so we don't need to add anything here
        pass
        
    def PerformAttack(self,enemy1,enemy2): #We have defined the perform attack function. Enemy1 and enemy2 refer to enemy classes. Below we have specified the attack damage that should be performed according to how many of the enemies are alive and which enemy is alive. We calculated the relevant attack damage according to these conditions.
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Elves":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.7)
            if self.enemy2.name == "Elves":
                enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.7)    
            if self.enemy1.name == "Dwarves":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.3)
            if self.enemy2.name == "Dwarves":
                enemy2.ReceiveAttack(self.name,self.attack_points*self.number_of_units*0.3)
        elif self.enemy1 or self.enemy2 ==True:
            if self.enemy1 == True:
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units)
            elif self.enemy2 == True:
                enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units)  
              
    
    def ReceiveAttack(self,name_of_attacker, total_damage): #We calculated the reduction in damage based on who the damage came from and reduced the number of units accordingly.
        if name_of_attacker == "Elves" : 
            self.number_of_units =self.number_of_units-(total_damage*0.75/ self._health_points)
        elif name_of_attacker == "Dwarves":
            self.number_of_units =self.number_of_units-(total_damage*0.80/ self._health_points)
        
    
    def PurchaseWeapons(self, number_of_weapons): #We increased the attack point according to how many weapons were bought
        self.attack_points = self.attack_points + number_of_weapons*2 

    def PurchaseArmors(self,number_of_armors): #We increased the health point according to how many armors were bought
        self._health_points = self._health_points + 3*number_of_armors
    
    def print(self):
        print("Stop running, you’ll only die tired!")

        


Faction1 = Faction()




        

