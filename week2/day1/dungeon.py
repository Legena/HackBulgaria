import hero
import orc
import entity
import fight

class Dungeon:
    def __init__(self, file_path):
        dungeon_file = open(file_path, 'r')
        self.map = dungeon_file.read().split('\n')
        self.__players = {}
        self.__player_stats = {}
        dungeon_file.close()

    def print_map(self):
        print(self.map)

    def spawn(self, player_name, entity):
        for line in range(0, len(self.map)):
            if 'S' in self.map[line]:
                self.__player_stats[player_name] = entity
                if isinstance(entity, hero.Hero):
                    self.map[line] = self.map[line].replace('S', 'H', 1)
                    self.__players[player_name] = (line,
                    self.map[line].index('H'))
                    return True
                elif isinstance(entity, orc.Orc):
                    self.map[line] = self.map[line].replace('S', 'O', 1)
                    self.__players[player_name] = (line,
                    self.map[line].index('O'))
                    return True
        return False

    def move(self, player_name, direction):
        position = self.__players[player_name]
        boundary = len(self.map[0])
        if direction == 'up':
            if position[0] > 0:
                if self.map[position[0] - 1][position[1]] == '#':
                    return False
                elif self.map[position[0] - 1][position[1]] == '.':
                    self.__swap(position[0], position[1], direction, player_name)
                    self.__players[player_name] = (position[0] - 1, position[1])
                    return True
                elif(self.map[position[0] - 1][position[1]] == 'H' or
                self.map[position[0] - 1][position[1]] == 'O'):
                    for player in self.__players:
                        if self.__players[player] == (position[0] - 1, position[1]):
                            meeted_player = player
                        return fight.Fight(self.__player_stats[player_name],
                        self.__player_stats[meeted_player]).simulate_fight()
            else:
                return False
        elif direction == 'left':
            if position[1] > 0:
                if self.map[position[0]][position[1] - 1] == '#':
                    return False
                elif self.map[position[0]][position[1] - 1] == '.':
                    self.__swap(position[0], position[1], direction, player_name)
                    self.__players[player_name] = (position[0], position[1] - 1)
                    return True
                elif(self.map[position[0]][position[1] - 1] == 'H' or
                self.map[position[0]][position[1] - 1] == 'O'):
                    for player in self.__players:
                        if self.__players[player] == (position[0], position[1] - 1):
                            meeted_player = player
                        return fight.Fight(self.__player_stats[player_name],
                        self.__player_stats[meeted_player]).simulate_fight()
            else:
                return False
        elif direction == 'down':
            if position[0] < boundary - 1:
                if self.map[position[0] + 1][position[1]] == '#':
                    return False
                elif self.map[position[0] + 1][position[1]] == '.':
                    self.__swap(position[0], position[1], direction, player_name)
                    self.__players[player_name] = (position[0] + 1, position[1])
                    return True
                elif(self.map[position[0] + 1][position[1]] == 'H' or
                self.map[position[0] + 1][position[1]] == 'O'):
                    meeted_player = entity.Entity("Goshu" , 1)
                    for player in self.__players:
                        if self.__players[player] == (position[0] + 1, position[1]):
                            meeted_player = player
                        return fight.Fight(self.__player_stats[player_name],
                        self.__player_stats[meeted_player]).simulate_fight()
            else:
                return False
        else:
            if position[1] < boundary - 1:
                if self.map[position[0]][position[1] + 1] == '#':
                    return False
                elif self.map[position[0]][position[1] + 1] == '.':
                    self.__swap(position[0], position[1], direction, player_name)
                    self.__players[player_name] = (position[0], position[1] + 1)
                    return True
                elif(self.map[position[0]][position[1] + 1] == 'H' or
                self.map[position[0]][position[1 + 1]] == 'O'):
                    for player in self.__players:
                        if self.__players[player] == (position[0], position[1] + 1):
                            meeted_player = player
                        return fight.Fight(self.__player_stats[player_name],
                        self.__player_stats[meeted_player]).simulate_fight()
            else:
                return False

    def __swap(self, line, col, direction, player_name):
        if direction == 'up':
            temp = list(self.map[line])
            up = list(self.map[line - 1])
            up[col], temp[col] = temp[col], up[col]
            self.map[line] = "".join(temp)
            self.map[line - 1] = "".join(up)
            self.__players[player_name] = (line - 1, col)
        elif direction == 'left':
            temp = list(self.map[line])
            temp[col], temp[col - 1] = temp[col - 1], temp[col]
            self.map[line] = "".join(temp)
            self.__players[player_name] = (line, col - 1)
        elif direction == 'down':
            temp = list(self.map[line])
            down = list(self.map[line + 1])
            down[col], temp[col] = temp[col], down[col]
            self.map[line] = "".join(temp)
            self.map[line + 1] = "".join(down)
            self.__players[player_name] = (line + 1, col)
        else:
            temp = list(self.map[line])
            temp[col], temp[col + 1] = temp[col + 1], temp[col]
            self.map[line] = "".join(temp)
            self.__players[player_name] = (line, col + 1)
