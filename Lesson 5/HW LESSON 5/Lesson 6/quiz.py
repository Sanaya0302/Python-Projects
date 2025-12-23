import random
class quiz():
    def __init__(self):
        self.fruits={"apple":"red","strawberry":"red","watermelon":"green","lemon":"yellow","pineapple":"yellow","orange":"orange","banana":"yellow"}
    def quizzz(self):
        while (True):
            fruit,colour=random.choice(list(self.fruits.items()))
            print("What is the colour of ",fruit)
            ans=input()
            if(ans.lower()==colour):
                print("corect answer!!!!!")
            else:
                print("wrong answer!!!!!!")
            option=int(input("Enter 1 if you want to play again else type 0: "))
            if option==0:
                break
q=quiz()
q.quizzz()