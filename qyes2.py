import random
class rock_paper_sci:
    res=[]
    choice=["rock","paper","scissor"]
    def _init_(self,rounds=1):
        self.round=rounds
        self.wins=0
        self.round_number=1
    def play(self):
        a=random.choice(["rock","paper","scissor"])
        b=input("Enter your choice (rock, paper, or scissor): ").lower()
        if (b not in ["rock","paper","scissor"]):
            print("invalid choice,choose again:")
            self.play()
        print(f"computer choice = {a}\nuser choice = {b}")
        if b == a:
            return (f"round {self.round_number}","It's a tie!")
        elif (b == 'rock' and a == 'scissor') or (b == 'scissor' and a== 'paper') or (b == 'paper' and a == 'rock'):
            self.wins+=1
            return (f"round {self.round_number}","You win!")
        else:
            return(f"round {self.round_number}","computer wins!")
    def start(self):
        for i in range(self.round):
            print(f"round : {self.round_number}")
            self.res.append(self.play())
            self.round_number=i+2
        return self.res
player1=rock_paper_sci(int(input("number of rounds to play :")))
print(player1.start())
print(f"number of wins : {player1.wins}")