import random
IMAGE=["rock","paper","scissor"]
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""





choice=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor  "))
print(choice)
comp=random.randint(0,2)

game=[rock,paper,scissor]
print(game[choice])
print(game[comp])




if choice==comp:
    print("Its a draw")
elif choice==0 and comp==1:
    print("You lose!")

elif choice==0 and comp==2:
    print("you Win!")
elif choice==1 and comp==0:
    print("you Win!")
elif choice==1 and comp==2:
    print("You Lose!")
elif choice==2 and comp==0:
    print("You Lose")
elif choice==2 and comp==1:
    print("you win")
elif choice>2:
    print("invalid choicem you lose")
                         



