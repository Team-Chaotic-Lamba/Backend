import random
class Generator():
    def __init__(self):
        self.dimensions = 30
        self.total_rooms = 100
        self.max_length = 8
    def createArray(self, num, dimensions):
        array = []
        for i in range(dimensions):
            array.append([])
            for j in range(dimensions):
                array[i].append(num)
        return array
    def createMap(self):
        map = self.createArray(1, self.dimensions) # create a 2d array full of 1's
        currentRow = random.randint(0, self.dimensions) # our current row - start at a random spot
        currentColumn = random.randint(0, self.dimensions) #  our current column - start at a random spot
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # array to get a random direction from (west,east,north,south)
        randomDirection = [] # next turn/direction - holds a value from directions
        lastDirection = None # save the last direction we went

        # lets create some tunnels - while maxTunnels, dimentions, and maxLength  is greater than 0.
        while self.total_rooms and self.dimensions and self.max_length:
            # lets get a random direction - until it is a perpendicular to our lastDirection
            # while randomDirection[0] == -lastDirection[0] and randomDirection[1] == -lastDirection[1] or randomDirection[0] == lastDirection[0] and randomDirection[1] == lastDirection[1]:
            randomDirection = directions[random.randint(0, len(directions)-1)]
                # if the last direction = left or right,
                # then our new direction has to be up or down,
                # and vice versa
            random_length = random.randint(0, self.max_length) # length the next tunnel will be (max of maxLength)
            tunnelLength = 0 # current length of tunnel being created

        # lets loop until our tunnel is long enough or until we hit an edge
        # break the loop if it is going out of the map
            while tunnelLength < random_length:
                if currentRow == 0 and randomDirection[0] == -1 or currentColumn == 0 and randomDirection[1] == -1 or currentRow == self.dimensions - 1 and randomDirection[0] == 1 or currentColumn == self.dimensions - 1 and randomDirection[1] == 1:
                    break
                else:
                    map[currentRow][currentColumn] = 0 # set the value of the index in map to 0 (a tunnel, making it one longer)
                    currentRow += randomDirection[0] # add the value from randomDirection to row and col (-1, 0, or 1) to update our location
                    currentColumn += randomDirection[1]
                    tunnelLength += 1 # the tunnel is now one longer, so lets increment that variable
            # update our variables unless our last loop broke before we made any part of a tunnel
            if tunnelLength:
                lastDirection = randomDirection # set lastDirection, so we can remember what way we went
                self.total_rooms -= 1 # we created a whole tunnel so lets decrement how many we have left to create
        return map # all our tunnels have been created and our map is complete, so lets return it to our render()
grid = Generator()

# print(grid.createMap())
count = 0
total = 0
for i in grid.createMap():
    for j in i:
        total += 1
        if j == 0:
            count += 1
print(count)
print("total", total)
# directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # array to get a random direction from (west,east,north,south)
# randomDirection = directions[random.randint(0, len(directions)-1)] # next turn/direction - holds a value from directions
# lastDirection = randomDirection
# print(-lastDirection[0])