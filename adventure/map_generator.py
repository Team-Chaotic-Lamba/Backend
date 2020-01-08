import random
import sys
from .models import *
print(sys.path)

room_type = {
    'Bedroom': 'This sleeping chamber is ',
    'Hall': 'This hall is ',
    "Kitchen": "This kitchen is ",
    "Study": "This study is ",
    "Laboratory": "This laboratory is ",
    "Bath": "This bathroom is ",
    "Storeroom": "This storeroom is ",
    "Cellar": "This cellar is ",
    "Shrine": "This shrine is ",
    "Library": "This library is ",
}

deco = {
    'Large': 'spacious with lots of light.',
    'Small': 'cozy!',
    "Deserted": 'dry and full of cobwebs and dust.',
    "Damp": "water drips from the ceiling, moisture fills the air.",
    "Dark": "dark, you can barely see!",
    "Crowded": 'full of discarded furniture.',
    "Evil": 'filled with an evil presence.',
    'Secret': "well hidden, unused for a long time.",
    "Cold": "freezing, a chill fills your body.",
    "Hot": "hot, you begin sweating instantly."
}

# Finished title and description of every unique room possiblity 
detailed_rooms = {}

for r, rv in room_type.items():
    for d, dv in deco.items():
        detailed_rooms[f"{d} {r}"] = f"{rv}{dv}"
        # print(d, r)

# print(detailed_rooms)


class Generator():
    def __init__(self):
        self.dimensions = 30
        self.total_rooms = 100
        self.max_length = 8
        self.count = 0
        self.saved_rooms = {}
    def createArray(self, num, dimensions):
        array = []
        for i in range(dimensions):
            array.append([])
            for j in range(dimensions):
                array[i].append(num)
        return array
    def createMap(self):
        map = self.createArray(1, self.dimensions) # create a 2d array full of 1's
        currentRow = random.randint(0, self.dimensions - 1) # our current row - start at a random spot
        currentColumn = random.randint(0, self.dimensions - 1) #  our current column - start at a random spot
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # array to get a random direction from (west,east,north,south)
        randomDirection = [] # next turn/direction - holds a value from directions
        lastDirection = None # save the last direction we went

        # lets create some tunnels - while maxTunnels, dimentions, and maxLength  is greater than 0.
        # while self.total_rooms and self.dimensions and self.max_length:
        while self.count < self.total_rooms:
            # lets get a random direction - until it is a perpendicular to our lastDirection
            # while randomDirection[0] == -lastDirection[0] and randomDirection[1] == -lastDirection[1] or randomDirection[0] == lastDirection[0] and randomDirection[1] == lastDirection[1]:
            randomDirection = directions[random.randint(0, len(directions)-1)]
                # if the last direction = left or right,
                # then our new direction has to be up or down,
                # and vice versa
            random_length = random.randint(1, self.max_length) # length the next tunnel will be (max of maxLength)
            tunnel_length = 0 # current length of tunnel being created

        # lets loop until our tunnel is long enough or until we hit an edge
        # break the loop if it is going out of the map
            while tunnel_length < random_length and self.count < self.total_rooms:
                if (currentRow == 0 and randomDirection[0] == -1) or \
                    (currentColumn == 0 and randomDirection[1] == -1) or \
                    (currentRow == self.dimensions - 1 and randomDirection[0] == 1) or \
                    (currentColumn == self.dimensions - 1 and randomDirection[1] == 1):
                    break
                else:
                    # Example Room('name', 'desc', f'{currentRow},{currentColumn}', f 'n_to: {currentRow - 1}, {currentColumn}, f's_to: {currentRow + 1}, {currentColumn}, f'w_to: {currentRow}, {currentColumn - 1}, f'e_to: {currentRow}, {currentColumn + 1})
                    for k, v in detailed_rooms.items():
                        if k not in saved_rooms:
                            r = Room(k, v, f'{currentRow},{currentColumn}')
                            r.save()
                    # self.count = random_length
                    map[currentRow][currentColumn] = 0 # set the value of the index in map to 0 (a tunnel, making it one longer)
                    currentRow += randomDirection[0] # add the value from randomDirection to row and col (-1, 0, or 1) to update our location
                    currentColumn += randomDirection[1]
                    tunnel_length += 1 # the tunnel is now one longer, so lets increment that variable
                    if map[currentRow][currentColumn] == 1:
                        self.count += 1
            # update our variables unless our last loop broke before we made any part of a tunnel
            if tunnel_length:
                lastDirection = randomDirection # set lastDirection, so we can remember what way we went
                # self.total_rooms -= 1 # we created a whole tunnel so lets decrement how many we have left to create
        return map # all our tunnels have been created and our map is complete, so lets return it to our render()
# grid = Generator()
# print(grid.saved_rooms)
# print(grid.createMap())
# count = 0
# total = 0
# for i in grid.createMap():
#     for j in i:
#         total += 1
#         if j == 0:
#             count += 1
# print(count)
# print("total", total)
# directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # array to get a random direction from (west,east,north,south)
# randomDirection = directions[random.randint(0, len(directions)-1)] # next turn/direction - holds a value from directions
# lastDirection = randomDirection
# print(-lastDirection[0])
# l1 = [-1, 0]
# l2 = [1, 0]
# something =  [l1[i] + l2[i] for i in range(2)] 
# print(something)