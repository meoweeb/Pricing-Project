"""
    This tool is designed to take user input of cost and determine the range of
    pricing needed to make a profit greater than their desired value.
"""
def installpricetool():

# ask user for cost
    price_cost = float(input("What is our cost? "))

    has_shipping = "False"
    our_cost = price_cost

    # shipping script
    # if shipping is true, our_cost increases by 12 dollars
    def shipping_yesno():
        has_shipping = input("Do we pay shipping on this? Y/N? ")
        if has_shipping == "Y" or has_shipping == "y":
            shipping_cost = 12.
        elif has_shipping == "N" or has_shipping == "n":
            shipping_cost = 0.
        else:
            print("Please enter only Y or N. ")
            shipping_yesno()

        # shipping costs are added if yes
        our_cost = price_cost + shipping_cost
        print(our_cost)

    shipping_yesno()

    # ask user for desired profit
    desired_profit = float(input("What is the minimum profit desired? "))
    print(desired_profit)

    commission_percent = .40

    modifying_percent = (desired_profit + our_cost) / ((1. - commission_percent) * our_cost)
    print(modifying_percent)

    minimum_pricing = our_cost * modifying_percent
    maximum_pricing = our_cost * (modifying_percent + 1.)

    # print values for user
    print("With a cost of " + str(our_cost) + " including shipping,")
    print("your desired profit (after commission) of " + str(desired_profit) + ",")
    print("we recommend a pricing range between $" + str(minimum_pricing) + "-$" + str(maximum_pricing) + ".")



installpricetool()
