# Created offically and truly by Abigblueworld
print ("Welcome to make an ice cream!")
print ("Let's start with the flavors")
flavors = ['chocolate', 'vanilla', 'strawberry', 'mint', 'cookies and cream']
toppings = ['sprinkers', 'hot fudge', 'whipped cream', 'a cherry', 'm&ms', 'chocolate chips']
print ("Menu:")
print ("")
print (flavors)
icecreamflavor = input("what is the ice cream flavor you want? ")
if icecreamflavor not in flavors:
    print ("That's not an available flavor, Please reset the program and try again")
else:
    print (icecreamflavor +"? alright!")
    yesorno1 = input("Do you want a second flavor? ")
    if yesorno1 == "yes":
      icecream2 = input ("What is your second flavor? ")
      if icecream2 not in flavors:
        icecream = icecreamflavor
        print ("That's not an available flavor, so we will not add a second flavor. Let's move on!")
      else:
        icecream = icecreamflavor + " and " + icecream2
        print ("So you have order a " + icecream + " ice cream? yum!")
    if yesorno1 == "no":
      icecream = icecreamflavor
      print ("Alright, just a " + icecream + " ice cream it is!")
    final = icecream + " ice cream"
    resultw = input("Do you want toppings on your " + icecream + " ice cream? ")
    if resultw == "yes":
      print ("Toppings:")
      print (toppings)
      topping = input("What topping do you want on your ice cream? ")
      if topping not in toppings:
        print ("That's not a topping on the list, let's not add a topping to this ice cream.")
      else:
        final = icecream + " ice cream with " + topping
        yesorno2 = input ("Do you want a second topping? ")
      if yesorno2 == "yes":
        topping2 = input("What is your second flavor? ")
      if topping2 not in toppings:
        print ("That's not an available topping, keeping only one.")
      else:
        final = icecream + " ice cream with" + topping + "and" + topping2
print ("Your ice cream is a " + final + "! That's so delish!")