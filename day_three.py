direction = input ("You are are crossroads, would you like to turn Left or Right ?\n").lower()
if direction == "left":

    action = input ("Would you like to swim or wait for a boat?\n").lower()
    if action == "wait":
        door = input("Would you like to go through the red, blue or yellow door?\n").lower()
        if door == "yellow":
            print("Congratulations ! ; you win :* ")

        else:
            print ("You entered a room of fire and burnt to death; you lose")
             
    else:
        print ("You drowned in the Atlantic Ocean; you lose")
            
else:
    print ("You got into an accident, unfortunately ; you lose")