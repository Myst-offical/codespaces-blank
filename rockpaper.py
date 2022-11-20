import random 
user=input("Chose one:rock paper or scissors")
action=("rock","paper","scissors")
rock="rock"
paper="paper"
scissors="scissors"
comaction=random.choice(action)
print("computer have chosen",comaction)
if user==comaction:
  print("both have chosen",user,"so draw")

elif user== rock:
   if comaction== paper:
     print("Paper cover rock You lost ")
   elif comaction== scissors:
       print("Rock smashes scissors You won")
elif user== paper:
   if comaction == rock :
     print("You won paper cover rock ")
   elif comaction == scissors:
       print("computer won")
elif user== scissors:
   if comaction == paper:
     print("user won ")
   elif comaction == rock:
       print("computer won")
else :
  print("Invalid choice")
  #byCaptian__mystery(ig)
       