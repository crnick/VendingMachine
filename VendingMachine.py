"""To run the file just type filename.py if running from the terminal"""

#This class defines the blueprint for vending machine
class VendingMachine:

    items=["drink","chips","mint","chocolate"]      #list of items to be purchased
    item_price=[0.75,1.00,1.30,1.50]                #the price of the item
    item_code=[1,2,3,4]                             #the code of item
    Coins=[0.10,0.25,0.50,1.0]                      #acceptable currency
    user_input=""                                   #variable defined for storing user input
    currentBalance=0                                #variable for tracking the current balance
    user_coins=0                                    #variable for the number of coins user has inserted


    #this method shows the menu to the user
    def menu(self):
        print("************Welcome to the vending machine**************** \n")
        print("Following are the items available: \n")
        print("item code:->",VendingMachine.item_code[0],"\t item name ->",VendingMachine.items[0],"\t price ->",VendingMachine.item_price[0],"\n") #Accessing the values directly using the class itself
        print("item code:->", VendingMachine.item_code[1], "\t item name ->", VendingMachine.items[1], "\t price ->",
              VendingMachine.item_price[1], "\n")
        print("item code:->", VendingMachine.item_code[2], "\t item name ->", VendingMachine.items[2], "\t price ->",
              VendingMachine.item_price[2], "\n")
        print("item code:->", VendingMachine.item_code[3], "\t item name ->", VendingMachine.items[3], "\t price ->",
              VendingMachine.item_price[3], "\n")

    #this method describes the user choice i.e  the input of the user and then goes through various checks to purchase the item
    def userChoice(self):

        self.user_input=int(input("Please enter a valid item code: \n"))

        if(self.user_input not in self.item_code):      #checking whether item code matches the code mentioned in the list at the top
            print("The item code you selected is not currently available..!!! \n")
            self.user_input = input("Please select the correct item code: \n")

        if(self.user_input==self.item_code[0]):         #if the input code mathces the first item in the items list
                print("You are purchasing -> {}, which has a price of -> {}".format(VendingMachine.items[0],
                                                                                    VendingMachine.item_price[0]))

                self.user_coins = float(input("Enter a Coin :\n")) #asks for user to enter coins for purchase

                if (self.user_coins not in self.Coins):  # if the currency doesn't match the eligible currency in the list menntioned at the top
                    print("The machine accepts only nickel -> {}, dime -> {}, quarter -> {}, dollar -> {} ".format(
                        self.Coins[0], self.Coins[1], self.Coins[2], self.Coins[3]))
                    self.user_coins = float(input("Enter a Coin :\n"))

                else:
                    self.currentBalance += self.user_coins   #adding the coins user inserted in to the currenct balance

                    if(self.currentBalance > self.item_price[0]):   #checking whether the balance is greated than the item price
                       print("The current balance has exceeded the price of item:-> {}\n".format(self.currentBalance))

                     #asking one final time for user to clarify whether to continue with the transaction or get the deposited money back
                       self.user_input=input("Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                       if(self.user_input=="return"):
                          print(self.returnMoney(),"\n")
                          print("Thank you!")

                       elif(self.user_input=="continue"):
                           self.user_coins=self.currentBalance-self.item_price[0]  #subtracting the balance from the actual price and returning remaining balance to the user
                           print("The balance has exceeded the price of item, here's your change back:->{} \n".format(self.user_coins))
                           print("The price of item has been met! \n")
                           print("Thank you, Here's the item you purchased: -> {} -> {}".format(self.items[0]))
                           exit()


                    #if the balance is less than the actual price of the item the while loop will keep on running unless the price is matched
                    while(self.currentBalance < self.item_price[0]):
                        print("The current balance is:-> {}\n".format(self.currentBalance))

                        self.user_coins = float(input("Not enough coins to purchase the item, enter more coins :\n"))
                        self.currentBalance+=self.user_coins

                        # if the balance equals the price ofthe item ask the user whether to proceed with the transaction or get deposited money back
                        if(self.currentBalance == self.item_price[0]):
                            print("The price of item has been met! \n")
                            self.user_input = input(
                            "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")

                            #if check whether user wants the deposited money back
                            if (self.user_input == "return"):
                                 print(self.returnMoney(),"\n")
                                 print("Thank you!")
                                 break
                            elif(self.user_input=="continue"): #elif clause if it want to continue with the purchase
                                print("Thank you, Here's the item you purchased: -> {}".format(self.items[0]))
                                break

                        # if the balance exceesds the price of the item return the remaining amount
                        elif(self.currentBalance > self.item_price[0]):
                            print("The current balance is:-> {}\n".format(self.currentBalance))
                            self.user_coins = self.currentBalance - self.item_price[0]
                            print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                                self.user_coins))
                            print("The price of item has been met! \n")
                            print("Thank you, Here's the item you purchased: -> {}".format(self.items[0]))
                            exit()
                    exit()

        #checking whether user wants the item with code 2 the following steps are simuilar to the first if check
        elif (self.user_input == self.item_code[1]):
            print("You are purchasing -> {}, which has a price of -> {}".format(VendingMachine.items[1],
                                                                                VendingMachine.item_price[1]))
            self.user_coins = float(input("Enter a Coin :\n"))
            self.currentBalance += self.user_coins


            if (self.user_coins not in self.Coins):
                print("The machine accepts only nickel -> {}, dime -> {}, quarter -> {}, dollar -> {} ".format(
                    self.Coins[0], self.Coins[1], self.Coins[2], self.Coins[3]))
                self.user_coins = float(input("Enter a Coin :\n"))

            else:

                if (self.currentBalance == self.item_price[1]):

                    print("The price of item has been met! \n")
                    self.user_input = input(
                        "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                    if (self.user_input == "return"):
                        print(self.returnMoney(), "\n")
                        print("Thank you!")
                        exit()
                    elif (self.user_input == "continue"):
                        print("Thank you, Here's the item you purchased: -> {}".format(self.items[2]))
                        exit()

                elif(self.currentBalance > self.item_price[1]):
                    self.currentBalance += self.user_coins
                    print("The current balance has exceeded the price of item:-> {}\n".format(self.currentBalance))

                    self.user_input = input(
                        "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                    if (self.user_input == "return"):
                        print(self.returnMoney(), "\n")
                        print("Thank you!")

                    elif (self.user_input == "continue"):
                        self.user_coins = self.currentBalance - self.item_price[1]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {} -> {}".format(self.items[1]))
                        exit()



                while (self.currentBalance < self.item_price[1]):
                    print("The current balance is:-> {}\n".format(self.currentBalance))

                    self.user_coins = float(input("Not enough coins to purchase the item, enter more coins :\n"))
                    self.currentBalance += self.user_coins

                    if (self.currentBalance == self.item_price[1]):
                        print("The price of item has been met! \n")
                        self.user_input = input(
                            "Type 'return' to get all deposited money or type 'continue' to purchase the item:\n")
                        if (self.user_input == "return"):
                            print(self.returnMoney(), "\n")
                            print("Thank you!")
                            break
                        elif (self.user_input == "continue"):
                            print("Thank you, Here's the item you purchased: -> {}".format(self.items[1]))
                            break

                    elif (self.currentBalance > self.item_price[1]):
                        print("The current balance is:-> {}\n".format(self.currentBalance))
                        self.user_coins = self.currentBalance - self.item_price[1]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {}".format(self.items[1]))
                        exit()
                exit()

        # checking whether user wants the item with code 3 the following steps are simuilar to the first if check
        elif (self.user_input == self.item_code[2]):
            print("You are purchasing -> {}, which has a price of -> {}".format(VendingMachine.items[2],
                                                                                VendingMachine.item_price[2]))
            self.user_coins = float(input("Enter a Coin :\n"))

            if (self.user_coins not in self.Coins):
                print("The machine accepts only nickel -> {}, dime -> {}, quarter -> {}, dollar -> {} ".format(
                    self.Coins[0], self.Coins[1], self.Coins[2], self.Coins[3]))
                self.user_coins = float(input("Enter a Coin :\n"))

            else:
                self.currentBalance += self.user_coins

                if (self.currentBalance > self.item_price[2]):
                    print("The current balance has exceeded the price of item:-> {}\n".format(self.currentBalance))

                    self.user_input = input(
                        "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                    if (self.user_input == "return"):
                        print(self.returnMoney(), "\n")
                        print("Thank you!")

                    elif (self.user_input == "continue"):
                        self.user_coins = self.currentBalance - self.item_price[2]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {} -> {}".format(self.items[2]))
                        exit()

                while (self.currentBalance < self.item_price[2]):
                    print("The current balance is:-> {}\n".format(self.currentBalance))

                    self.user_coins = float(input("Not enough coins to purchase the item, enter more coins :\n"))
                    self.currentBalance += self.user_coins

                    if (self.currentBalance == self.item_price[2]):
                        print("The price of item has been met! \n")
                        self.user_input = input(
                            "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                        if (self.user_input == "return"):
                            print(self.returnMoney(), "\n")
                            print("Thank you!")
                            break
                        elif (self.user_input == "continue"):
                            print("Thank you, Here's the item you purchased: -> {}".format(self.items[2]))
                            break

                    elif (self.currentBalance > self.item_price[2]):
                        print("The current balance is:-> {}\n".format(self.currentBalance))
                        self.user_coins = self.currentBalance - self.item_price[2]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {}".format(self.items[2]))
                        exit()
                exit()

        # checking whether user wants the item with code 4 the following steps are simuilar to the first if check
        elif (self.user_input == self.item_code[3]):
            print("You are purchasing -> {}, which has a price of -> {}".format(VendingMachine.items[3],
                                                                                VendingMachine.item_price[3]))
            self.user_coins = float(input("Enter a Coin :\n"))

            if (self.user_coins not in self.Coins):
                print("The machine accepts only nickel -> {}, dime -> {}, quarter -> {}, dollar -> {} ".format(
                    self.Coins[0], self.Coins[1], self.Coins[2], self.Coins[3]))
                self.user_coins = float(input("Enter a Coin :\n"))

            else:
                self.currentBalance += self.user_coins

                if (self.currentBalance > self.item_price[3]):
                    print("The current balance has exceeded the price of item:-> {}\n".format(self.currentBalance))

                    self.user_input = input(
                        "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                    if (self.user_input == "return"):
                        print(self.returnMoney(), "\n")
                        print("Thank you!")

                    elif (self.user_input == "continue"):
                        self.user_coins = self.currentBalance - self.item_price[3]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {} -> {}".format(self.items[3]))
                        exit()

                while (self.currentBalance < self.item_price[3]):
                    print("The current balance is:-> {}\n".format(self.currentBalance))

                    self.user_coins = float(input("Not enough coins to purchase the item, enter more coins :\n"))
                    self.currentBalance += self.user_coins

                    if (self.currentBalance == self.item_price[3]):
                        print("The price of item has been met! \n")
                        self.user_input = input(
                            "Type 'return' to get all deposited money back or type 'continue' to purchase the item:\n")
                        if (self.user_input == "return"):
                            print(self.returnMoney(), "\n")
                            print("Thank you!")
                            break
                        elif (self.user_input == "continue"):
                            print("Thank you, Here's the item you purchased: -> {}".format(self.items[3]))
                            break

                    elif (self.currentBalance > self.item_price[3]):
                        print("The current balance is:-> {}\n".format(self.currentBalance))
                        self.user_coins = self.currentBalance - self.item_price[3]
                        print("The balance has exceeded the price of item, here's your change back:->{} \n".format(
                            self.user_coins))
                        print("The price of item has been met! \n")
                        print("Thank you, Here's the item you purchased: -> {}".format(self.items[3]))
                        exit()
                exit()

        #the else clause is run if the code which user entered doesn't match with any code present in the list at the top
        else:
            print("The code you entered does not match any item! Try again...!!")

    #method for priting the returned deposit to the user
    def returnMoney(self):
       return "Here's your money back: -> {}".format(self.currentBalance)

if __name__ == '__main__':
    vm=VendingMachine() #isntantiating the VendingMachine class
    vm.menu()   #calling menu method with the object created
    vm.userChoice()  #calling the userChoice method for calculation and purchasing the item
