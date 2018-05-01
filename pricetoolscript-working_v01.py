"""
    This tool is designed to take user input of cost and determine the range of
    pricing needed to make a profit greater than their desired value.
"""

def ship_true(shipping_bool):
    has_shipping = input("Do we pay shipping on this? Y/N? ")
    if has_shipping == "Y" or has_shipping == "y":
        shipping_bool = True
    elif has_shipping == "N" or has_shipping == "n":
        shipping_bool = False
    else:
        print("Please enter only Y or N. ")
        ship_true(shipping_bool)
    return shipping_bool

def installpricetool():

# ask user for cost
    price_cost = float(input("What is our cost? "))

    our_cost = price_cost



    shipping_yesno = True
    shipping_yesno = ship_true(shipping_yesno)
    if shipping_yesno == False:
        shipping_cost = 0.
    else:
        shipping_cost = input("What is shipping cost? If unknown, type U. ")
        if shipping_cost == "U" or shipping_cost == "u":
            shipping_cost = 12.
            print("Shipping cost default is $" + str(shipping_cost) + ".")
        else:
            float(shipping_cost)

    print("Shipping cost: $" + str(shipping_cost))


    # shipping costs are added
    our_cost = float(price_cost) + float(shipping_cost)

    print("Our total cost with shipping is $" + str(our_cost) + ".")




    # ask user for desired profit
    desired_profit = float(input("What is the minimum profit desired? "))
    print(desired_profit)

    commission_percent = .40

    modifying_percent = (desired_profit + our_cost) / ((1. - commission_percent) * our_cost)
    print(modifying_percent)

    minimum_pricing = round(our_cost * modifying_percent)
    maximum_pricing = round(our_cost * (modifying_percent + 1.))

    # print values for user
    print("With a cost of $" + str(our_cost) + " including shipping,")
    print("your desired profit (after commission) of $" + str(desired_profit) + ",")
    print("we recommend a pricing range between $" + str(minimum_pricing) + "-$" + str(maximum_pricing) + ".")

    input("Start over? ")
    installpricetool()

installpricetool()
