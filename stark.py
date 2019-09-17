# Points of PointA=Arya and PointS=Sansa       


def check(tup,P,R):                 #check for Each Tuple combination 
    global pointA                    #follow Given Condition for Win
    global pointS
    for string in tup:
            if string=='A':            # points Counted End Of Each Round i.e; PREVIOUS ROUND POINTS + CURRENT ROUND POINTS
                pointA=pointA+1
            elif string=='S':
                 pointS=pointS+1
            if not pointA>=P*pointS and sum([pointA,pointS])<=R:
                return False
    else:
        return True




T=int(input())
from itertools import product
for T_count in range(T):                #number of TestCase
    final=[]                    #finalResult List
    R,P=map(int,input().split())        #INPUT round and P Value
    T_comb=list(product('AS',repeat=R))  # Total Combination Possible
    for ways in T_comb:         #fetching Each Combination..i.e; Ways
        pointA=0  
        pointS=0
        if ways.count('A')>ways.count('S') and ways[0]=='A':    # for winning By Arya It Must Have To Win
            if check(ways,P,R):                                                     # Atleast Two First Round -->> |A|A|*|*|..|
                final.append(ways)
                

    print(len(final))
