""" Given an infinite number line, you would like to build few blocks and obstacles on it. Specifically, 
you have to implement code which supports two types of operations:
[1, x] - builds an obstacle at coordinate x along the number line. 
It is guaranteed that coordinate x does not contain any obstacles when the operation is performed.
[2, x, size] - checks whether it's possible to build a block of size size beginning at position x. 
For example, for size = 2 and x = 0, it will check 0 and 1 on the number line for obstacles. 
Returns 1 if it is possible, i.e. there are no obstacles at the occupied coordinates, and return 0 otherwise. 
Please note that this operation does not actually build the block, it only checks whether a block can be built.
Given an array of operations containing both types of operations above, 
your task is to return a binary string representing the outputs for all [2, x, size] operations. """

def obstacle_build(operations):
    obstacles = set()
    result = []

    for op in operations:
        if op[0]==1:
            x = op[1]
            obstacles.add(x)
        elif op[0]==2:
            x,size = op[1],op[2]
            can_build = all(x+i not in obstacles for i in range(size))
            result.append('1' if can_build else '0')
    return ''.join(result)

operations = [
    [1, 3],
    [2, 0, 2],
    [2, 2, 2],
    [2, 3, 2]
]

print(obstacle_build(operations))

#============================================================================== 

""" Given the two arrays a2b and b2a, representing travel times from A to B and B to A, 
respectively, the goal is to find the minimum time required to travel from A to B 
and back to A, considering that you cannot take a flight back that arrives earlier 
than your arrival time plus the travel time.

The Two arrays given are 
a2b = [100, 200, 350]
b2a = [99, 210, 500] """

def min_round_trip_time(a2b,b2a):
    min_time = float('inf')
    for i in range(len(a2b)):
        departure_a2b = a2b[i]
        for j in range(len(b2a)):
            if b2a[j]>departure_a2b:
                round_trip_time = departure_a2b+b2a[j]
                min_time = min(min_time,round_trip_time)
                break
    return min_time
a2b = [100, 200, 350]
b2a = [99, 210, 500]

min_time = min_round_trip_time(a2b, b2a)
print(f"Minimum Round-Trip Time: {min_time}")

#============================================================================= 


""" Given the following 
"chicago,food,bacon",
"miami,clothing,shoes",
"miami,food,bread",
"chicago,clothing,shoes",
"atlanta,food,peppers",
"miami,food,bread",
"chicago,food,bacon",
"atlanta,electronics,camera",
"miami,clothing,shoes",
"chicago,food,peppers",
"miami,food,bread"
please parse the data and return it in the following format.
you can set it to whatever you want i.e. a list, a string etc.

# {
#     "chicago": {
#         "food": {
#             "bacon": 2,
#             "peppers": 1
#         },
#         "clothing": {
#             "shoes": 1
#         }
#     },
#     "miami": {
#         "clothing": {
#             "shoes": 2
#         },
#         "food": {
#             "bread": 3
#         }
#     },
#     "atlanta": {
#         "food": {
#             "peppers": 1
#         },
#         "electronics": {
#             "camera": 1
#         }
#     }
# } """
info = ["chicago,food,bacon",
"miami,clothing,shoes",
"miami,food,bread",
"chicago,clothing,shoes",
"atlanta,food,peppers",
"miami,food,bread",
"chicago,food,bacon",
"atlanta,electronics,camera",
"miami,clothing,shoes",
"chicago,food,peppers",
"miami,food,bread"]

def parse_data(info):
    city = {}
    for i in info:
        arr = i.split(",")
        if arr[0] not in city:
            city[arr[0]] = {} 
        if arr[1] not in city[arr[0]]:
            city[arr[0]][arr[1]] = {} 
        if arr[2] not in city[arr[0]][arr[1]]:
            city[arr[0]][arr[1]][arr[2]] = 0
        city[arr[0]][arr[1]][arr[2]]+=1
    return city
        

print(parse_data(info))

#============================================================================= 
""" The problem was to take in either a string or a tree and convert it to the opposite 
so taking in a string would create a tree and vice versa. But to make the tree should be done in a binary way """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s: str) -> TreeNode:
    if not s:
        return None

    mid = len(s) // 2
    root = TreeNode(s[mid])
    root.left = buildTree(s[:mid])
    root.right = buildTree(s[mid + 1:])
    
    return root

def treeToString(root: TreeNode) -> str:
    if not root:
        return ""
    
    return treeToString(root.left) + root.val + treeToString(root.right)

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=' ')
        printInOrder(root.right)
# Example usage
s = "puzzle"
tree = buildTree(s)
printInOrder(tree)
result = treeToString(tree)
print(result)  # Output should be "abcdefg"
#============================================================================= 
