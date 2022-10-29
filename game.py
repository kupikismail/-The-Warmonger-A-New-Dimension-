
class Faction():  #Here we created a parent class for factions
    def __init__(self,name="Orcs", number_of_units= 50, attack_point=30, health_point=150,unit_regeneration_number=10 ): #we created some common attributes(If not specified, the values to the right of the equation will be used.)
        self.name = name  #one of the orcs, elves, and dwarves
        self.number_of_units = number_of_units
        self.attack_points = attack_point
        self._health_points = health_point
        self.total_health_points = self._health_points * self.number_of_units 
        self.total_attack_power = self.attack_points*self.number_of_units #We created this to appropriately find the remaining number of units. Required for the endturn function to work properly 
        self.unit_regeneration_number = unit_regeneration_number
        self.alive = True
        self.AssignEnemies() #In this function we created below, we created the enemies according to the name of faction.

    def AssignEnemies(self):
        self.all_factions = ["Orcs", "Dwarves", "Elves" ]
        self.all_factions.remove(self.name)
        self.enemy1 = self.all_factions[0]
        self.enemy2 = self.all_factions[1]

    def PerformAttack(self): #these are customized for child classes
        pass
    
    def ReceiveAttack(self): #these are customized for child classes
        pass
    
    def PurchaseArmors(self): #these are customized for child classes
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
    
    def EndTurn(self): #This function updates the number of units, total health and alive status of the faction.
        self.total_attack_power = self.number_of_units* self.attack_points
        self.total_health_points = self.number_of_units*self._health_points
        if self.total_health_points <= 0 : 
            self.alive == 0 
        else: self.number_of_units = self.number_of_units + self.unit_regeneration_number
                 

class Orcs(Faction): # orcs child class created,all features and functions defined in the Faction class have been made available
    def __init__(self,name, number_of_units, attack_point, health_point,unit_regeneration_number ): #We can use the features in the faction class so we don't need to add anything here
        super().__init__(name, number_of_units, attack_point, health_point,unit_regeneration_number)
        
    def PerformAttack(self,enemy1,enemy2): #We have defined the perform attack function. Enemy1 and enemy2 refer to enemy classes. Below we have specified the attack damage that should be performed according to how many of the enemies are alive and which enemy is alive. We calculated the relevant attack damage according to these conditions.
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Elves":
                enemy1.ReceiveAttack(self.name, self.total_attack_power*0.7)
            if self.enemy2.name == "Elves":
                enemy2.ReceiveAttack(self.name,self.total_attack_power*0.7)    
            if self.enemy1.name == "Dwarves":
                enemy1.ReceiveAttack(self.name, self.total_attack_power*0.3)
            if self.enemy2.name == "Dwarves":
                enemy2.ReceiveAttack(self.name,self.total_attack_power*0.3)
        elif self.enemy1 or self.enemy2 ==True:
            if self.enemy1 == True:
                enemy1.ReceiveAttack(self.name, self.total_attack_power)
            elif self.enemy2 == True:
                enemy2.ReceiveAttack(self.name, self.total_attack_power)  
              
    
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
    def __init__(self,name, number_of_units, attack_point, health_point,unit_regeneration_number ): #We can use the features in the faction class so we don't need to add anything here
        super().__init__(name, number_of_units, attack_point, health_point,unit_regeneration_number)
        
    def PerformAttack(self,enemy1,enemy2):  
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Elves":
                enemy1.ReceiveAttack(self.name,self.total_attack_power*0.5)
            if self.enemy2.name == "Elves":
                enemy2.ReceiveAttack(self.name,self.total_attack_power*0.5)    
            if self.enemy1.name == "Orcs":
                enemy1.ReceiveAttack(self.name, self.total_attack_power*0.5)
            if self.enemy2.name == "Orcs":
                enemy2.ReceiveAttack(self.name,self.total_attack_power*0.5)
        elif self.enemy1 or self.enemy2 ==True:
            if self.enemy1 == True:
                enemy1.ReceiveAttack(self.name,self.total_attack_power)
            elif self.enemy2 == True:
                enemy2.ReceiveAttack(self.name, self.total_attack_power)  
              
    
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
    def __init__(self,name, number_of_units, attack_point, health_point,unit_regeneration_number ): #We can use the features in the faction class so we don't need to add anything here
        super().__init__(name, number_of_units, attack_point, health_point,unit_regeneration_number)

    def PerformAttack(self,enemy1,enemy2):  
        if self.enemy1 and self.enemy2 == True :
            if self.enemy1.name == "Dwarves":
                enemy1.ReceiveAttack(self.name, self.total_attack_power*0.6) #We made it 0.4*1.5 because it attacks drawves fifty percent more
            if self.enemy2.name == "Dwarves":
                enemy2.ReceiveAttack(self.name, self.total_attack_power*0.6)    
            if self.enemy1.name == "Orcs":
                enemy1.ReceiveAttack(self.name, self.total_attack_power*0.6)
            if self.enemy2.name == "Orcs":
                enemy2.ReceiveAttack(self.name,self.total_attack_power*0.6)
        elif self.enemy1 or self.enemy2 ==True: #If there is only one living enemy and that drawves, we changed this part because the attack damage has changed. We have identified who the living enemy is.
            if self.enemy1 == True:
                if self.enemy1.name == "Orcs":
                    enemy1.ReceiveAttack(self.name, self.total_attack_power)
                else:
                    enemy1.ReceiveAttack(self.name, self.total_attack_power*1.5)
            elif self.enemy2 == True:
                if self.enemy2.name == "Orcs":
                    enemy2.ReceiveAttack(self.name, self.total_attack_power)  
                else:
                    enemy2.ReceiveAttack(self.name, self.total_attack_power*1.5)  
                
    
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
        self.Orcs_unit_number = 50
        self.Orcs_attack_point = 30
        self.Orcs_health_point= 150
        self.Orcs_regeneration_number = 10

        self.faction_Dwarves = None
        self.Dwarves_unit_number = 50
        self.Dwarves_attack_point = 30
        self.Dwarves_health_point= 150
        self.Dwarves_regeneration_number = 10

        self.faction_Elves = None 
        self.Elves_unit_number = 50
        self.Elves_attack_point = 30
        self.Elves_health_point= 150
        self.Elves_regeneration_number = 10
    
    def AssignFactions(self): #The factions in the game are assigned for Merchant to use.
        self.faction_Orcs= Orcs("Orcs",self.Orcs_unit_number,self.Orcs_attack_point,self.Orcs_health_point,self.Orcs_regeneration_number)
        self.faction_Dwarves = Dwarves("Dwarves",self.Dwarves_unit_number,self.Dwarves_attack_point,self.Dwarves_health_point,self.Dwarves_regeneration_number)
        self.faction_Elves = Elves("Elves", self.Elves_unit_number,self.Elves_attack_point,self.Elves_health_point,self.Elves_regeneration_number)
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
    
    def start_game(self):
        game_status = 1  #This indicates the status of the game. When this equals 0, the game ends, if it is equal to 1, the game continues, if it is equal to 2, the new game starts
        print("Welcome to the 'The Warmonger: A New Dimension' Game ")
        print("Before starting the game, you can change some features in the game.")
        print("You can change the unit numbers, attack points, health points, unit regeneration numbers of Orcs, Dwarves and Elves. You can also change your weapon points and armor points that you will get each round.")
        print("If there is a change you want to make, write 1 in the terminal, otherwise write 0.")
        game_change_request = input()
        if int(game_change_request) == 0:
            pass
        elif int(game_change_request)== 1:
            while int(game_change_request) ==1:  #If the players want to make changes about the values and powers of the characters, they can do it thanks to this while.
                print("Specify which character you want to change. Write 1 for Merchant,  2 for Orcs, 3 for Drawres,4 for Elves, 5 for starting game.")
                selected_character = input()
                if int(selected_character) == 1:
                    print("Press 1 to change weapon point, press 2 to change armor point. The recommended amount for both is 10.")
                    decision_for_Merchant = input()
                    if int(decision_for_Merchant) == 1:
                        print("Determine the amount")
                        self.starting_weapon_point == int(input())
                    elif decision_for_Merchant == 2:
                        self.starting_armor_point == int(input())
                    else:
                        print("There is no such option, write 1 if you want to make another changes, press 0 if not")
                        user_desicion = input()  # All subsequent user inputs are named user_desicion. To avoid constantly finding new variable name.
                        if int(user_desicion) == 1:
                            pass
                        elif int(user_desicion)  == 0 :
                            game_change_request == 0 

                elif int(selected_character) == 2:
                    print("Write 1 to change the number of units, 2 to change the attack point, 3 to change the health point, and 4 to change the unit regeneration number.")
                    user_desicion = input()
                    if int(user_desicion) == 1:
                        print("Enter the amount you want. The recommended number is 50")
                        self.Orcs_unit_number = int(input())
                    elif int(user_desicion) ==2:
                        print("Enter the amount you want. The recommended number is 30")
                        self.Orcs_attack_point= int(input())
                    elif int(user_desicion)==3:
                        print("Enter the amount you want. The recommended number is 150")
                        self.Orcs_health_point= int(input())
                    elif int(user_desicion) == 4:
                        print("Enter the amount you want. The recommended number is 10")
                        self.Orcs_regeneration_number= int(input())
                    else:
                        print("There is no such option, write 1 if you want to make another changes, press 0 if not")
                        user_desicion = input()
                        if int(user_desicion) == 1:
                            pass
                        elif int(user_desicion) == 0 :
                            game_change_request == 0 

                elif int(selected_character) == 3:
                    print("Write 1 to change the number of units, 2 to change the attack point, 3 to change the health point, and 4 to change the unit regeneration number.")
                    user_desicion = input()
                    if int(user_desicion) == 1:
                        print("Enter the amount you want. The recommended number is 50")
                        self.Drawres_unit_number = int(input())
                    elif int(user_desicion) ==2:
                        print("Enter the amount you want. The recommended number is 30")
                        self.Drawres_attack_point= int(input())
                    elif int(user_desicion)==3:
                        print("Enter the amount you want. The recommended number is 150")
                        self.Drawres_health_point= int(input())
                    elif int(user_desicion) == 4:
                        print("Enter the amount you want. The recommended number is 10")
                        self.Drawres_regeneration_number= int(input())
                    else:
                        print("There is no such option, write 1 if you want to make another changes, press 0 if not")
                        user_desicion = input()
                        if int(user_desicion) == 1:
                            pass
                        elif int(user_desicion) == 0 :
                            game_change_request == 0 

                elif int(selected_character) == 4:
                    print("Write 1 to change the number of units, 2 to change the attack point, 3 to change the health point, and 4 to change the unit regeneration number.")
                    user_desicion = input()
                    if int(user_desicion) == 1:
                        print("Enter the amount you want. The recommended number is 50")
                        self.Elves_unit_number = int(input())
                    elif int(user_desicion) ==2:
                        print("Enter the amount you want. The recommended number is 30")
                        self.Elves_attack_point= int(input())
                    elif int(user_desicion)==3:
                        print("Enter the amount you want. The recommended number is 150")
                        self.Elves_health_point= int(input())
                    elif int(user_desicion) == 4:
                        print("Enter the amount you want. The recommended number is 10")
                        self.Elves_regeneration_number= int(input())
                    else:
                        print("There is no such option, write 1 if you want to make another changes, press 0 if not")
                        user_desicion = input()
                        if int(user_desicion) == 1:
                            pass
                        elif int(user_desicion) == 0 :
                            game_change_request == 0 
                
                elif int(selected_character) == 5 : 
                    game_change_request = 0 
                
                else: 
                    print("There is no such option, write 1 if you want to make another changes, press 0 if not")
                    user_desicion = int(input())
                    if user_desicion == 1:
                        pass
                    
                    elif user_desicion == 0 :
                        game_change_request == 0

        self.AssignFactions()  #we created factions according to player's options

        print("The options related to the game and how to use it are stated below. You can perform the action you want to do by writing it into the terminal.")
        
        while game_status ==1:
            print("Write 1 to see the information of the factions, 2 to sell weapons and armors, 3 to end the day, 4 to start a new game, and 5 to end the game.")
            user_desicion = int(input())

            if user_desicion == 1 :  #From here, we print the information of the factions using the common print function in the faction class.
                print("Specify which faction's information you want to see. Type 1 for Orcs, 2 for Dwarves, and 3 for Elves.")
                user_desicion = int(input())
                if user_desicion == 1:
                    self.faction_Orcs.Print()
                elif user_desicion == 2:
                    self.faction_Dwarves.Print()
                elif user_desicion == 3 : 
                    self.faction_Elves.Print()
                else:
                    print("There is no such option")
            



                

                
                
                





                        




    
    
A = Merchant()
A.start_game()








        

