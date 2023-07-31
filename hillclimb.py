#from intertools import pemutations
def findcost(newcity):
    list = []
    i = 0
    cost = 0
    for i in range(len(newcity)-1):
        a = str(newcity[i])
        b = str(newcity[i+1])
        cost = cost + actualvalues.get(a+b)
    cost += actualvalues.get(str(newcity[-1]) + str(newcity[0]))
    return cost

def generatesol():
    cities = list(['A', 'B', 'C', 'D'])
    currentsol = []
    nextsol = []
    old = 100
    oldsolution = []
    oldsolution = cities
    old = findcost(cities)
    for i in range(0,3):
        for j in range(0,2):
            temp = cities[3-j]
            cities[3-j] = cities[3-j-1]
            cities[3-j-1] = temp
            nextcost = findcost(cities)
            nextsolution = cities
            print(nextsolution)
            print(nextcost)
            if(nextcost>old):
                nextsolution = oldsolution
                break
            else:
                return nextsolution



def hillclimbing():
    solution = generatesol()
    print(solution)
    print("Cost will be = ", findcost(solution))

actualvalues = {
    'AB': 25,
    'AD': 15,
    'BD': 45,
    'BC': 10,
    'CD': 5,
    'AC': 10,
    'BA': 25,
    'DA': 15,
    'DB': 45,
    'CB': 10,
    'DC': 5,
    'CA': 10,

}
