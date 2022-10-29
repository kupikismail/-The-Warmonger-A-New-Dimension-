
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
    
    def Print(self):#print function commonly used for factions and gives the following information
        if self.name == "Orcs":
            print("Stop running, you’ll only die tired!")
        elif self.name == "Dwarves":
            print("Taste the power of our axes!")
        elif self.name == "Elves" :
            print("You cannot reach  our elegance.")            

        print("Faction Name: " , self.name)
        print("Status:", end ="")
        if self.alive == True:
            print("Alive")
        else:
            print("Defeated")
        print("Number of Units:", self.number_of_units)
        print("Attack Point:", self.attack_points)
        print("Health Point:", self._health_points)
        print("Unit Regen Number:", self.unit_regeneration_number )
        print("Total Faction Health:", self.total_health_points)
        

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
    


class Dwarves(Faction):  #The general structure is the same as the orcs class, we just edit some numbers and names.
    def __init__(self,name ="Dwarves"): 
        pass
        
    def PerformAttack(self,enemy1,enemy2):  
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Elves":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.5)
            if self.enemy2.name == "Elves":
                enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.5)    
            if self.enemy1.name == "Orcs":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.5)
            if self.enemy2.name == "Orcs":
                enemy2.ReceiveAttack(self.name,self.attack_points*self.number_of_units*0.5)
        elif self.enemy1 or self.enemy2 ==True:
            if self.enemy1 == True:
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units)
            elif self.enemy2 == True:
                enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units)  
              
    
    def ReceiveAttack(self,name_of_attacker, total_damage):  
        if name_of_attacker == "Elves" : 
            self.number_of_units =self.number_of_units-(total_damage/ self._health_points)
        elif name_of_attacker == "Orcs":
            self.number_of_units =self.number_of_units-(total_damage/ self._health_points)
        
    
    def PurchaseWeapons(self, number_of_weapons):  
        self.attack_points = self.attack_points + number_of_weapons

    def PurchaseArmors(self,number_of_armors): 
        self._health_points = self._health_points + 2*number_of_armors
    


        
class Elves(Faction):  # We just edit some numbers and names.
    def __init__(self,name ="Elves"): 
        pass
        
    def PerformAttack(self,enemy1,enemy2):  
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Dwarves":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.6) #We made it 0.4*1.5 because it attacks drawves fifty percent more
            if self.enemy2.name == "Dwarves":
                enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.6)    
            if self.enemy1.name == "Orcs":
                enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*0.6)
            if self.enemy2.name == "Orcs":
                enemy2.ReceiveAttack(self.name,self.attack_points*self.number_of_units*0.6)
        elif self.enemy1 or self.enemy2 ==True: #If there is only one living enemy and that drawves, we changed this part because the attack damage has changed. We have identified who the living enemy is.
            if self.enemy1 == True:
                if self.enemy1.name == "Orcs":
                    enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units)
                else:
                    enemy1.ReceiveAttack(self.name, self.attack_points*self.number_of_units*1.5)
            elif self.enemy2 == True:
                if self.enemy2.name == "Orcs":
                    enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units)  
                else:
                    enemy2.ReceiveAttack(self.name, self.attack_points*self.number_of_units*1.5)  
                
    
    def ReceiveAttack(self,name_of_attacker, total_damage):  
        if name_of_attacker == "Elves" : 
            self.number_of_units =self.number_of_units-(total_damage/ self._health_points*1.25)
        elif name_of_attacker == "Dwarves":
            self.number_of_units =self.number_of_units-(total_damage/ self._health_points*0.75)
        
    
    def PurchaseWeapons(self, number_of_weapons):  
        self.attack_points = self.attack_points + number_of_weapons*2

    def PurchaseArmors(self,number_of_armors): 
        self._health_points = self._health_points + 4*number_of_armors
    
 

class Merchant():  #Merchant class has been created and the following features (some of them are offered to the user as options) are specified.
    def __init__(self,starting_weapon_point =10, starting_armor_point= 10):
        self.starting_weapon_point = starting_weapon_point
        self.starting_armor_point = starting_armor_point
        self.revenue = 0 
        self.weapon_point_left= self.starting_weapon_point
        self.armor_point_left = self. starting_armor_point
        self.faction_Orcs = None  
        self.faction_Dwarves = None
        self.faction_Elves = None 
    
    def AssignFactions(self): #The factions in the game are assigned for Merchant to use.
        self.faction_Orcs= Orcs
        self.faction_Dwarves = Dwarves
        self.faction_Elves = Elves
    def SellWeapons(self,who, how_many): #Function that allows Merchant to sell weapons to factions
        if who.alive == True:
            if self.weapon_point_left >= how_many:
                print("Weapons sold!")
                return True
            else:
                print("You try to sell more weapons than you have in possession.")
                return False
                
        else: 
            print("The faction you want to sell weapons is dead!")
        
    def SellArmors(self,who, how_many): #Function that allows Merchant to sell armors to factions
        if who.alive == True:
            if self.armor_point_left >= how_many:
                print("Armors sold!")
                return True
            else:
                print("You try to sell more armors than you have in possession.")
                return False
                
        else: 
            print("The faction you want to sell armors is dead!")    
        
    def EndTurn(self):
        self.weapon_point_left= self.starting_weapon_point
        self.armor_point_left = self. starting_armor_point


    
    









        

