
blind_auction = {}
power = False

while power :
    bidder_name = input("What is your name?\n")
    bidder_price = input("What is your price?\n$")
    blind_auction[bidder_name]=bidder_price
    
    should_continue = input("Are there any other bidders? 'yes' or 'no'. ")
    if should_continue == "no":
        power = True
    elif should_continue = "yes":
        clear()




        