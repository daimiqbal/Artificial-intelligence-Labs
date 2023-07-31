import copy
import math


childlist = []


class Node:
    row = 0
    col = 0
    value = 0




def pathfollow(root_node, temp_grid):
    total_Cost = 0
    endpoint = (reach1, reach2)
    startpoint = (start1, start2)
    while startpoint != endpoint:
        row = root_node[endpoint].row
        col = root_node[endpoint].col
        temp_grid[row][col] = '*'
        if (endpoint[0] - 1 == row) and (endpoint[1] - 1 == col):
            total_Cost = total_Cost + 3
        else:
            total_Cost = total_Cost + 2
        endpoint = (row, col)
    print("total_Cost After the followed path is: ", total_Cost)



def emptychild():
    for i in range(len(childlist)):
        childlist.pop()




def huristic(node):
    v1 = (reach1 - node.row) * (reach1 - node.row)
    v2 = (reach2 - node.col) * (reach2 - node.col)
    v3 = v1 + v2
    dist = math.sqrt(v3)
    return dist


def sort_list(listsort):
    lst = len(listsort)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if listsort[j].value > listsort[j + 1].value:
                temp = listsort[j]
                listsort[j] = listsort[j + 1]
                listsort[j + 1] = temp
    return listsort

def print_grid(temp_grid, route):
    for i in range(len(route)):
        print("Rows Followed => ", route[i].row);
        print("Cols Followed => ", route[i].col)
def getchild(row, col):
    rowt = 0
    colt = 0
    if row != 14 and grid[row + 1][col] == '0':
        node = Node()
        rowt = row + 1
        node.row = rowt
        node.col = col
        childlist.append(node)
    if row != 14 and col != 14 and grid[row + 1][col + 1] == '0':
        node = Node()
        rowt = row + 1
        colt = col + 1
        node.row = rowt
        node.col = colt
        childlist.append(node)
    if col != 14 and grid[row][col + 1] == '0':
        node = Node()
        colt = col + 1
        node.row = row
        node.col = colt
        childlist.append(node)
    return list

class PriorityQueue:
    q = []

    def is_empty(self):
        if len(self.q) == 0:
            return True

    def insert(self,node):
        self.q.append(node)
        self.q = sort_list(self.q)

    def remove(self):
        temp_node = self.q[0]
        self.q.pop(0)
        return temp_node

    def best_first_search(self):
        grid2 = copy.deepcopy(grid)
        start_node = Node()
        start_node.row = start1
        start_node.col = start2
        q = PriorityQueue()
        q.insert(start_node)
        is_visited = []
        for i in range(15):
            is_visited.append([False] * 15)
        is_visited[start1][start2] = True
        global flag
        flag = False
        route = []
        root_node = {}
        while not q.is_empty():
            node = q.remove()
            route.append(node)
            grid2[node.row][node.col] = '#'
            emptychild()
            getchild(node.row, node.col)
            for i in childlist:
                row = i.row
                col = i.col
                tuple = (row, col)
                if row == reach1 and col == reach2:
                    print("Goal Found")
                    root_node[tuple] = node
                    pathfollow(root_node, grid2)
                    flag = True
                    break
                if not is_visited[row][col]:
                    is_visited[row][col] = True
                    child = Node()
                    child.row = row
                    child.col = col
                    child.value = huristic(child)
                    q.insert(child)
                    root_node[tuple] = node
            if flag:
                break
        print_grid(grid2, route)

    def a_star_search(self):
        grid2 = copy.deepcopy(grid)
        start_node = Node()
        start_node.row = start1
        start_node.col = start2
        start_node.value = huristic(start_node)
        q = PriorityQueue()
        q.insert(start_node)
        visitlist = []
        for i in range(15):
            visitlist.append([False] * 15)
        visitlist[start1][start2] = True
        global flag
        flag = False
        route = []
        root_node = {}
        while not q.is_empty():
            node = q.remove()
            route.append(node)
            grid2[node.row][node.col] = '#'
            emptychild()
            getchild(node.row, node.col)
            for i in childlist:
                row = i.row
                col = i.col
                tuple = (row, col)
                if row == reach1 and col == reach2:
                    print("Goal Found")
                    root_node[tuple] = node
                    pathfollow(root_node, grid2)
                    flag = True
                    break
                if not visitlist[row][col]:
                    visitlist[row][col] = True
                    child = Node()
                    child.row = row
                    child.col = col
                    edge_total_Cost = 0
                    if (node.row + 1 == row) and (node.col + 1 == col):
                        edge_total_Cost = 3
                    else:
                        edge_total_Cost = 2
                    child.value = node.value - huristic(node) + huristic(child) + edge_total_Cost
                    q.insert(child)
                    root_node[tuple] = node
            if flag:
                break
        print_grid(grid2, route)






def inputvalue(rowstart, colstart, goalrow, goalcol):
    if rowstart < 0 or rowstart > 14 or colstart < 0 or colstart > 14 or goalrow < 0 or goalrow > 14 or goalcol < 0 or goalcol > 14:
        print("Input Exceeds the bpard limit! Please give correct value: ")
        return False
    elif (grid[rowstart][colstart] == '1') or (grid[goalrow][goalcol] == '1'):
        print("Start and Goal can't be at hurdle position!Please give a Correct Value:")
        return False
    elif (rowstart == goalrow) and (colstart == goalcol):
        print("Robot is already on Goal position")
        return False
    else:
        return True

robot = PriorityQueue()
grid = []
for i in range(15):
    grid.append([0] * 15)
file = open("grid.txt")
for i in range(15):
    line = file.readline()
    for j in range(15):
        grid[i][j] = line[j]
flag = True
while flag:
    start1 = int(input("Row => "))
    start2 = int(input("Col => "))
    reach1 = int(input("Goal Row => "))
    reach2 = int(input("Goal Col => "))
    start1 = start1 - 1
    start2 = start2 - 1
    reach1 = reach1 - 1
    reach2 = reach2 - 1
    if not (inputvalue(start1, start2, reach1, reach2)):
        print("Input Again")
        continue
    print("1. Best First Search")
    print("2. A star Search")
    print("3. Exit Programm")
    choice = input("Enter Your Choice => ")
    if choice == '1':
        robot.best_first_search()
    elif choice == '2':
        robot.a_star_search()
    elif choice =='3':
        exit(0);
    else:
        continue
