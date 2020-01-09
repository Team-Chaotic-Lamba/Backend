import random
import sys
from .models import Room

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
    "Damp": "wet, water drips from the ceiling, moisture fills the air.",
    "Dark": "dark, you can barely see!",
    "Crowded": 'full of discarded furniture.',
    "Evil": 'filled with an evil presence.',
    'Secret': "well hidden, unused for a long time.",
    "Cold": "freezing, a chill fills your body.",
    "Hot": "hot, you begin sweating instantly."
}

# Finished title and description of every unique room possiblity 
detailed_rooms = {}
detailed_keys = []

for r, rv in room_type.items():
    for d, dv in deco.items():
        detailed_rooms[f"{d} {r}"] = f"{rv}{dv}"
        detailed_keys.append(f"{d} {r}")
        # print(d, r)
random.shuffle(detailed_keys)
# print(detailed_rooms)


class Generator():
    def __init__(self):
        self.dimensions = 24
        self.total_rooms = 100
        self.max_length = 6
        self.count = 0
        self.saved_rooms = {}
        self.room_list = []
        self.prev = None
    def create_array(self, num, dimensions):
        array = []
        for i in range(dimensions):
            array.append([])
            for j in range(dimensions):
                array[i].append([num, None])
        return array
    def create_map(self):
        map = self.create_array(1, self.dimensions) # create a 2d array full of 1's
        current_row = random.randint(0, self.dimensions - 1) # our current row - start at a random spot
        current_column = random.randint(0, self.dimensions - 1) #  our current column - start at a random spot
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # array to get a random direction from (west,east,north,south)
        random_direction = [] # next turn/direction - holds a value from directions
        last_direction = None # save the last direction we went

        # lets create some tunnels - while maxTunnels, dimentions, and maxLength  is greater than 0.
        # while self.total_rooms and self.dimensions and self.max_length:
        while self.count < self.total_rooms:
            # lets get a random direction - until it is a perpendicular to our last_direction
            random_direction = directions[random.randint(0, len(directions)-1)]
                # if the last direction = left or right,
                # then our new direction has to be up or down,
                # and vice versa
            random_length = random.randint(1, self.max_length) # length the next tunnel will be (max of maxLength)
            tunnel_length = 0 # current length of tunnel being created

        # lets loop until our tunnel is long enough or until we hit an edge
        # break the loop if it is going out of the map
            while tunnel_length < random_length and self.count < self.total_rooms:
                if (current_row == 0 and random_direction[0] == -1) or \
                    (current_column == 0 and random_direction[1] == -1) or \
                    (current_row == self.dimensions - 1 and random_direction[0] == 1) or \
                    (current_column == self.dimensions - 1 and random_direction[1] == 1):
                    break
                else:
                    current_coord = [current_row, current_column]
                    for k in detailed_keys:
                        r = None
                        if k not in self.saved_rooms:
                            if map[current_row][current_column][1] is None:
                                self.saved_rooms[k] = detailed_rooms[k]
                                r = Room(self.count, k, self.saved_rooms[k], current_coord)
                                r.save()
                                map[current_row][current_column][1] = r
                                map[current_row][current_column][0] = 0 # set the value of the index in map to 0 (a tunnel, making it one longer)
                            else:
                                r = map[current_row][current_column][1]
                            if last_direction is not None and self.prev is not None:
                                if last_direction == [-1, 0]: # West
                                    r.e_to = self.prev.id
                                    self.prev.w_to = r.id
                                    r.save()
                                    self.prev.save()
                                elif last_direction == [1, 0]: # East
                                    r.w_to = self.prev.id
                                    self.prev.e_to = r.id
                                    r.save()
                                    self.prev.save()
                                elif last_direction == [0, -1]: # North
                                    r.s_to = self.prev.id
                                    self.prev.n_to = r.id
                                    r.save()
                                    self.prev.save()
                                elif last_direction == [0, 1]: # South
                                    r.n_to = self.prev.id
                                    self.prev.s_to = r.id
                                    r.save()
                                    self.prev.save()
                            break
                    self.prev = map[current_row][current_column][1]
                    current_row += random_direction[0] # add the value from random_direction to row and col (-1, 0, or 1) to update our location
                    current_column += random_direction[1]
                    tunnel_length += 1 # the tunnel is now one longer, so lets increment that variable
                    if map[current_row][current_column][0] == 1:
                        self.count += 1
                # update our variables unless our last loop broke before we made any part of a tunnel
                # if tunnel_length:
                last_direction = random_direction # set last_direction, so we can remember what way we went
                # self.total_rooms -= 1 # we created a whole tunnel so lets decrement how many we have left to create
        return map # all our tunnels have been created and our map is complete, so lets return it to our render()