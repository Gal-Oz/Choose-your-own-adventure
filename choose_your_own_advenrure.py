name = input("type your name: ")
print("Welcome", name , "to this adventrure!")

answer = input (
    "You are on a dird road, it has come to an end you can go left or right. which way do you like to go? ").lower()
if answer == "left":
    answer = input ("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()
    if answer == "swim":
        print("You swim accross and eaten by an alligator.")
    elif answer == "walk":
       print("You walk for many miles, ran out of water and you lost the game.") 
    else:
        print("Not a vlid option. You lose.")   


elif answer == "right":
    answer = input ("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross / back) ").lower()
    if answer == "back":
        print("You go back to the main road. ran out of water and you lost the game.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
           print("You ignor the strangerr and they are affended and you lose.")
        else:
            print("Not a vlid option. You lose.")

    else:
        print("Not a vlid option. You lose.")
else:
    print("Not a vlid option. You lose.")

print ("Thank you for trying", name)