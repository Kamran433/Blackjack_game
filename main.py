# import logo_BJ
# import random
# A=["1","11"]
# z=random.choice(A)
# cards=[z,"2","3","4","5","6","7","8","9","10","10","10","10"]
# comp=random.choice(cards)
# play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# c1=random.choice(cards)
# c2=random.choice(cards)
# c3=random.choice(cards)
# c4=random.choice(cards)
# c5=random.choice(cards)
# cond=True
# hum=[]
# comp=[]
# cond=True
# if play=="y":
#   print(logo_BJ.logo)
#   hum.append(c1)
#   hum.append(c2)
#   ok=int(c1)+int(c2)
#   co=int(c3)
#   print(f"Your cards: {hum}, current score: {ok}")
#   comp.append(c3)
#   print(f"Computer's first card: {comp}")
#   while cond is True:  
#       ask=input(f"Type 'y' to get another card,type 'n' to pass: ")
#       if ask=="y":
#         hum.append(c4)
#         comp.append(c5)
#         final=ok+int(c4)
#         ko=co+int(c5)
#         print(f"Your final hand: {hum}, final score: {final}")
#         print(f"Computer's final hand: {comp}, final score: {ko}")
#         ok=final
#         co=ko
#         if ok>=21:
#           print("You went over. You lose 😭")
#           cond=False
#         elif co>=21:
#           print("Opponent went over. You win 🥳")
#           cond=False
#         elif ok==co:
#           print("Draw 🙃")
#           cond=False
#         elif ok>co:
#           print("You win 🥳")
#           cond=False 
#         elif ok<co:
#           print("You lose 😤")
#           cond=False
#         elif ok==0:
#           print("Win with a Blackjack 😎")
#           cond=False
#         elif ok==0:
#           print("Lose, opponent has a Blackjack 😱")
#           cond=False
#       elif ask=="n":
#         print(f"Your final hand: {hum}, final score: {ok}")
#         z=[1,2]
#         d=random.choice(z)
#         if d==1:
#          final=ok
#          comp.append(c5)
#          ko=co+int(c5)
#          print(f"Computer's final hand: {comp}, final score: {ko}")
#          ok=final
#          co=ko
#          if ok>=21:
#            print("You went over. You lose 😭")
#            cond=False
#          elif co>=21:
#            print("Opponent went over. You win 🥳")
#            cond=True
#          elif ok==co:
#             print("Draw 🙃")
#             cond=False
#          elif ok>co:
#             print("You win 🥳")
#             cond=False 
#          elif ok<co:
#             print("You lose 😤")
#             cond=False
#          elif ok==0:
#             print("Win with a Blackjack 😎")
#             cond=False
#          elif ok==0:
#             print("Lose, opponent has a Blackjack 😱")
#             cond=False
#         elif d==2:
#           final=ok
#           ko=co
#           print(f"Computer's final hand: {comp}, final score: {ko}")
#           ok=final
#           co=ko
#           if ok>=21:
#             print("You went over. You lose 😭")
#             cond=False
#           elif co>=21:
#             print("Opponent went over. You win 🥳")
#             cond=True
#           elif ok==co:
#             print("Draw 🙃")
#             cond=False
#           elif ok>co:
#             print("You win 🥳")
#             cond=False 
#           elif ok<co:
#             print("You lose 😤")
#             cond=False
#           elif ok==0:
#             print("Win with a Blackjack 😎")
#             cond=False
#           elif ok==0:
#             print("Lose, opponent has a Blackjack 😱")
#             cond=False
# elif play=="n":
#   print("The End! 🖕🏻")
#   cond=False
# print("Thanks For Playing! 🫠")
