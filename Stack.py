import random
from itertools import permutations
from typing import List, Union
from enum import Enum
from enum import unique
from collections import Counter

STACK_MAX = 10


@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    PINK = 5
    ORANGE = 6
    PURPLE = 7
    CYAN = 8
    BROWN = 9
    MAGENTA = 10
    LIME = 11
    TEAL = 12
    INDIGO = 13
    VIOLET = 14
    PEACH = 15
    WHITE = 16
    BLACK = 17
    SILVER = 18
    GOLD = 19
    GRAY = 20
    NAVY = 21
    OLIVE = 22
    MAROON = 23
    AQUA = 24
    LAVENDER = 25


class ChipStack:
    stack_max: int
    stack: List[Color]

    def __init__(self, stack=None, stack_max=STACK_MAX, ) -> None:
        self.stack_max = stack_max
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def __str__(self):
        result = []
        for color in self.stack:
            result.append(color.name)
        if len(self.stack) == self.stack_max:
            return str(result) + ' MAX'
        return str(result) + f' {self.stack_max - len(self.stack)} slot(s)'

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, index):
        return self.stack[index]

    def is_full(self):
        return len(self.stack) >= self.stack_max

    def is_same(self):
        return len(set(self.stack)) == 1

    def is_empty(self):
        return len(self.stack) == 0

    def add_item(self, item: Union[Color, List[Color]]):
        if isinstance(item, Color):
            self.stack.append(item)
        else:
            self.stack.extend(item)

    def get_movables(self):
        count = 1
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i] == self.stack[i - 1]:
                count += 1
            else:
                break
        return count

    def pop_items(self, n):
        movable = self.stack[-n:]
        self.stack = self.stack[:-n]
        return movable

    def find_most_common(self):
        if self.stack:
            counter = Counter(self.stack)
            return counter.most_common(1)[0][1]
        return 1


class Game:
    stack_num: int
    color_num: int
    stacks: List[ChipStack]
    empty: int

    def __init__(self, stack_num, color_num, empty=1):
        self.stack_num = stack_num
        self.color_num = color_num
        self.empty = empty
        self.stacks = []
        total_color = self.color_num - self.empty
        selected_color = random.sample(list(Color), total_color)
        color_lists = []
        for i in range(self.stack_num - self.empty):
            color_lists.append([random.choice(selected_color)] * STACK_MAX)
        merged_list = [color for sublist in color_lists for color in sublist]
        random.shuffle(merged_list)

        for i in range(0, len(merged_list), STACK_MAX):
            stack_slice = merged_list[i:i + STACK_MAX]
            stack = ChipStack(stack=stack_slice)
            self.stacks.append(stack)
        for i in range(self.empty):
            self.stacks.append(ChipStack())
        print(self)

    def __str__(self):
        result = ''
        count = 0
        for stack in self.stacks:
            result += f"Stack #{count}: " + str(stack) + '\n'
            count += 1
        return result

    def is_done(self):
        empty = self.empty
        for stack in self.stacks:
            if not (stack.is_same() and stack.is_full()):
                if stack.is_empty():
                    empty -= 1
                    if empty < 0:
                        return False
                else:
                    return False
        return True

    def is_movable(self, source_index: int, destination_index: int):
        if source_index == destination_index:
            return False
        source, destination = self.stacks[source_index], self.stacks[destination_index]
        if source.is_empty():
            return False
        if not destination.is_empty() and source[-1] != destination[-1]:
            return False
        if len(destination) + source.get_movables() > destination.stack_max:
            return False
        return True

    def move(self, source_index: int, destination_index: int):
        source, destination = self.stacks[source_index], self.stacks[destination_index]
        if self.is_movable(source_index, destination_index):
            destination.add_item(source.pop_items(source.get_movables()))
            print(f"MOVE #{source_index} to #{destination_index}")
        else:
            print(f"CANNOT MOVE #{source_index} to #{destination_index}")
        print(self)

    def apply_move(self, source_index: int, destination_index: int):
        source, destination = self.stacks[source_index], self.stacks[destination_index]
        if self.is_movable(source_index, destination_index):
            destination.add_item(source.pop_items(source.get_movables()))

    def add_stack(self):
        self.stacks.append(ChipStack())
        self.empty += 1

    def run(self):
        if input("Need more Stack? y/n ") == 'y':
            self.empty += 1
            self.add_stack()
            print(self)
        while True:
            try:
                self.move(int(input("from stack number: ")), int(input("to stack number: ")))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def possible_moves(self):
        moves = list(permutations(list(range(len(self.stacks))), 2))
        possibles = []
        for move in moves:
            if self.is_movable(*move):
                possibles.append(move)
        if possibles:
            return possibles
        else:
            # print("ADD A STACK")
            self.add_stack()
            return self.possible_moves()


    def purity(self) -> float:
        occupied = sum(len(stack) > 0 for stack in self.stacks)
        purities = 0
        for stack in self.stacks:
            if stack:
                purities += stack.find_most_common() / len(stack)
        return purities / occupied



if __name__ == '__main__':
    random.seed(2)
    game = Game(4)
    while not game.is_done():
        game.run()
    print("You win!")
