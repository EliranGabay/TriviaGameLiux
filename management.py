


class questions(object):

    def __init__(self,pid,quest,ans,op1,op2,op3,op4):
        self.pid = pid
        self.quest = quest
        self.ans = ans 
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4




class leaderboard(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def setFinalScore(self,newScore):
        self.score = newScore

  

       
