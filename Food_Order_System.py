import openpyxl

itemsAvailable = ["Crunch Burger","Hot Wings Bucket","Mighty Zinger","Krunch Combo","Zinger Stacker Combo","Biryani Mid Box", "Biryani Large Box"]
itemsQuantity = [10,10,10,0,10,10,10]
itemTotalOrders = [0,0,0,0,0,0,0]
itemAvailability = ["Y","Y","Y","N","Y","Y","Y"]
itemsPricesOrigional = ["250 PKR","550 PKR","680 PKR","490 PKR","810 PKR","410 PKR","910 PKR"]


itemsPrices = [250,550,680,490,810,410,910]
itemsOrdered = []
userAddress = []
userAmountFood = []
userTotalPrice = []
userReviews = []
userPaymentMethod = []
userNames  = []
userNoReviews = ["None"]
rating = 0

userSecurityCard = [123456789]

print("-----------------------------------------\n")
print("____Welcome__To__Hoories__Resturant______\n")
print("-----------------------------------------\n")

repeat = 1
while(repeat):
    print("1) Order a food\n2) Rate a food\n3) Exit <--\n")
    ask0  = int(input("Select: "))
    if(ask0 == 1):
        print("--------------------------------\n")
        print("Welcome to order a food section.\n")
        print("--------------------------------\n")
        print("Wanna See Menu of Hoories Resturant ? (press 1 for yes OR press 0 for no)\n")
        ask1 = int(input("Select: "))

        if(ask1== 1):
            print("Here We have available items:\n")
            index = 1
            for i in range(len(itemsAvailable)):
                print(f"{index}     {itemsAvailable[i]}    Price: {itemsPrices[i]}")
                index = 1 + index
        elif(ask1 == 0):
            print("Ok Sir..\n")
        else:
            print("Enter Valid Command Please.\n")
            break
            
        print("What would you like to order sir ?\n")
        askOrder=input("Reply : ")
        if(askOrder in itemsAvailable):
            for i in range(len(itemAvailability)):
                if(askOrder in itemsAvailable[i] and itemAvailability[i] == "Y" ):
                    itemsOrdered.append(askOrder)
                    print("Food added to your cart successfully..\n")
                    for i in range(len(itemTotalOrders)):
                        if(askOrder in itemsAvailable[i]):
                            itemTotalOrders[i] += 1
                elif(askOrder in itemsAvailable[i] and itemAvailability[i] == "N"):
                    print("Sorry Sir, This Food Is not Available right now.!\n")
                    break
            amountFood = int(input("Enter Amount Of Your Food: "))
            userAmountFood.append(amountFood)
            amountFood = amountFood
            for i in range(len(itemsAvailable)):
                if(askOrder == itemsAvailable[i]):
                    totalPrice = itemsPrices[i] * amountFood 
                    userTotalPrice.append(f"{totalPrice} PKR")
            for i in range(len(itemsAvailable)):
                if(askOrder == itemsAvailable[i]):
                    itemsQuantity[i] -= 1
                    
            print("Now kindly Enter your Address.\n")
            addressUser = input("Address: ")
            
            userAddress.append(addressUser)
            
            userName = input("Enter Your Full Name: ")
            
            userNames.append(userName)
            
            print("Which Payment method you want to select ? ")
            print("\n1) Online Payment (Card)\n2) Door Payment\nNOTE: select 1 for online payment OR press 2 for door payment.\n")
            userMethod = int(input("Select: "))
            print(userMethod)
            if(userMethod == 1 ):
                userMethod = "Online Payment(Card)"
                userCard = int(input("Enter Credit Card Number: "))
                
                if(userCard in userSecurityCard):
                    print("SuccessFull...\n")
                    userPaymentMethod.append(userMethod)
                else:
                    print("Invalid Credit Card Number")
            elif (userMethod == 2):
                userMethod = "Door Payment(gate)"
                print("Ok, As you say :).\n")
                userPaymentMethod.append(userMethod)            
        else:
            print("Sorry sir , this food is not available.\n")
    elif(ask0 == 2):
        print("Give Ratings: *  *  *  *  *\n")
        rating1 = int(input("Reply: "))
        
        if(rating1 == 1):
            rating = rating + 1
            userReviews.append(rating)
            print("Review Added Successfully.\n")
            break
        elif(rating1 == 2):
            rating = rating + 2
            userReviews.append(rating)
            print("Review Added Successfully.\n")
            break
        elif(rating1 == 3):
            rating = rating + 3
            userReviews.append(rating)
            print("Review Added Successfully.\n")
            break
        elif(rating1 == 4):
            rating = rating + 4
            userReviews.append(rating)
            print("Review Added Successfully.\n")
            break
        elif(rating1 == 5):
            rating = rating + 5
            userReviews.append(rating)
            print("Review Added Successfully.\n")
            break
        elif(rating > 5):
            print("Sorry, greater than 5 are not allowed.\n")
    elif(ask0==3):
        print("Ba Bayeee.!\n")
        break
    else:
        break
    

# MAKING USERS DATA FILE EXCEL 

UserFile = openpyxl.Workbook()
UserS = UserFile.active
UserS.title = "Customers Data"


UserS["A1"] = "Customer's Name"
UserS["B1"] = "Customer's Item Name"
UserS["C1"] = "Customer's Item Amount"
UserS["D1"] = "Customer's Item's Total Price"
UserS["E1"] = "Customer's Address"
UserS["F1"] = "Customer's Payment Method"
UserS["G1"] = "Customer's Reviews"


for i in range(len(itemsOrdered)):

    UserS["A" + str(i + 2)] = userNames[i]
    UserS["B" + str(i + 2)] = itemsOrdered[i]
    UserS["C" + str(i + 2)] = userAmountFood[i]
    UserS["D" + str(i + 2)] = userTotalPrice[i]
    UserS["E" + str(i + 2)] = userAddress[i]
    UserS["F" + str(i + 2)] = userPaymentMethod[i]
    if(rating!=0):
        UserS["G" + str(i + 2)] = userReviews[i]
    elif(rating==0):
        UserS["G" + str(i + 2)] = userNoReviews[i]

# Save the Excel spreadsheet
    UserFile.save("Customer's Data.xlsx")

# MAKING FILE For Admin EXCEL 

AdminFile = openpyxl.Workbook()
AdminS = AdminFile.active
AdminS.title = "Resturant's Data"


AdminS["A1"] = "Item Available"
AdminS["B1"] = "Item Price"
AdminS["C1"] = "Item Quantity"
AdminS["D1"] = "Item Availability"
AdminS["E1"] = "Item Total Orders"



for i in range(len(itemsAvailable)):
    AdminS["A" + str(i + 2)] = itemsAvailable[i]
    AdminS["B" + str(i + 2)] = itemsPricesOrigional[i]
    AdminS["C" + str(i + 2)] = itemsQuantity[i]
    AdminS["D" + str(i + 2)] = itemAvailability[i]
    AdminS["E" + str(i + 2)] = itemTotalOrders[i]

# Save the Excel spreadsheet
    AdminFile.save("Resturant's Data.xlsx")
 
