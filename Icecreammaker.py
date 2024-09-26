print("Welcome to make an ice cream!")
print("Let's start with the flavors")
flavors = ['chocolate', 'vanilla', 'strawberry', 'mint', 'cookies and cream']
toppings = ['sprinkles', 'hot fudge', 'whipped cream', 'a cherry', 'm&ms', 'chocolate chips']

print("Menu:")
print("")
print(flavors)
icecreamflavor = input("What is the ice cream flavor you want? ").lower()

if icecreamflavor not in flavors:
    print("That's not an available flavor, please reset the program and try again.")
else:
    print(icecreamflavor + "? Alright!")
    yesorno1 = input("Do you want a second flavor? (yes/no) ").lower()
    
    if yesorno1 == "yes":
        icecream2 = input("What is your second flavor? ").lower()
        if icecream2 not in flavors:
            print("That's not an available flavor, so we will not add a second flavor. Let's move on!")
            icecream = icecreamflavor
        else:
            icecream = icecreamflavor + " and " + icecream2
            print("So you have ordered a " + icecream + " ice cream? Yum!")
    else:
        icecream = icecreamflavor
        print("Alright, just a " + icecream + " ice cream it is!")

    final = icecream + " ice cream"
    resultw = input("Do you want toppings on your " + icecream + " ice cream? (yes/no) ").lower()
    
    if resultw == "yes":
        print("Toppings:")
        print(toppings)
        topping = input("What topping do you want on your ice cream? ").lower()
        
        if topping not in toppings:
            print("That's not a topping on the list, let's not add a topping to this ice cream.")
        else:
            final += " with " + topping
            yesorno2 = input("Do you want a second topping? (yes/no) ").lower()
            
            if yesorno2 == "yes":
                topping2 = input("What is your second topping? ").lower()
                if topping2 in toppings:
                    final += " and " + topping2
                else:
                    print("That's not an available topping, keeping only one.")

    print("Your ice cream is a " + final + "! That's so delish!")
