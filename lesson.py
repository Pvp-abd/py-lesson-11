class Sport:
    def __init__(self,player,score):
        self.player=player
        self.__score=0
        self.set_score(score)

    def get_score(self):
        return self.__score

    def set_score(self,new_score):
        valid=type(new_score) is int and  new_score >=0
        if valid:
            self.__score=new_score

        else:
            print (f"rejected {new_score!r}")
        return valid
class Baseball(Sport):
    def play(self):
        print("hits the home run")
        
class Football(Sport):
    def play(self):
        print("scores a goal!")

baseball=Baseball("john",47)
football=Football("marco",2)
for sport in [baseball,football]:
    sport.play()
baseball.__score=100
print("direct:",baseball.get_score())
baseball.set_score(100)
print("through set score:",baseball.get_score())