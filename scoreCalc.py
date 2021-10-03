class route:
    def __init__(self, name, severity, numOfAccids, distance):
        self.name = name
        self.severity = severity
        self.numOfAccids = numOfAccids
        self.distance = distance


def sev_score(severity):
    score = -1
    if(severity<0):
        print("Invalid severity level")
    elif(severity == 1):
        score = 4
    elif(severity == 2):
        score = 8
    elif(severity ==3):
        score = 12
    elif(severity ==4):
        score = 16
    elif(severity == 5):
        score = 20
    else:
        print("Invalid severity level")

    return score


def acc_score(numOfAccid):   #return score based on number of accidents
     score = -1

     if(numOfAccid == 0):
        score=0

     elif(numOfAccid >0 and numOfAccid<= 100):
        score=10

     elif(numOfAccid >100 and numOfAccid<= 200):
        score=20

     elif(numOfAccid >200 and numOfAccid<= 300):
        score=30

     elif(numOfAccid >300 and numOfAccid<= 400):
        score=40

     elif(numOfAccid >400 and numOfAccid<= 500):
        score=50

     elif(numOfAccid >500 and numOfAccid<= 600):
        score=60
    
     elif(numOfAccid >600 and numOfAccid<= 700):
        score=70

     elif(numOfAccid >700 and numOfAccid<= 800):
        score= 75

     else :
        score =80


     return score


def scoreCalc(myRoute):

    totalScore= -1
    score_acc = acc_score(myRoute.numOfAccids)
    score_sev = sev_score(myRoute.severity)
    totalScore = "{:.3f}".format(100-(score_acc + score_sev)/float(myRoute.distance))
    #total_score= "{:.3f}".format(totalScore)

    #print(totalScore)

    return totalScore


def main():
    list = []

    list.append(route("cali", 4, 600, 12))
    list.append(route("texas", 5, 700, 15))

    for x in list:
        print('The score of this route based on accidents is: '+ str(scoreCalc(x)))
    

if __name__ =="__main__":
    main()