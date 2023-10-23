import random
from typing import List, Union

STACK_MAX = 10
COLOR_MAP = {
    0: 'RED',
    1: 'GREEN',
    2: 'YELLOW',
    3: 'BLUE',
    4: 'PINK'
}


class ChipStack:
    stack_max: int
    stack: List[int]

    def __init__(self, stack_max: int) -> None:
        self.stack_max = stack_max
        self.stack = []

    def __str__(self):
        result = []
        for i in self.stack:
            result.append(COLOR_MAP[i])
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

    def add_item(self, item: Union[int, List[int]]):
        if isinstance(item, int):
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


class Game:
    stack_num: int
    stacks: List[ChipStack]
    empty: int

    def __init__(self, stack_num):
        self.stack_num = stack_num
        self.empty = 1
        self.stacks = []
        for i in range(stack_num):
            self.stacks.append(ChipStack(STACK_MAX))
        self.start()

    def __str__(self):
        result = ''
        count = 0
        for stack in self.stacks:
            result += f"Stack #{count}: " + str(stack) + '\n'
            count += 1
        return result

    def start(self):
        total_color = self.stack_num - 1
        colors = random.sample(list(COLOR_MAP.keys()), total_color)
        lst = []
        for color in colors:
            lst.extend([color] * STACK_MAX)
        random.shuffle(lst)
        for stack in self.stacks[:-1]:
            while not stack.is_full():
                stack.add_item(lst.pop())

    def is_done(self):
        empty = self.empty
        for stack in self.stacks:
            if not (stack.is_same() and stack.is_full()):
                if stack.is_empty():
                    empty -= 1
                    if empty < 0: return False
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

    def add_stack(self):
        self.stacks.append(ChipStack(STACK_MAX))

    def run(self):
        print("Start")
        print(self)
        while not self.is_done():
            if input("Need more Stack? y/n ") == 'y':
                self.empty += 1
                self.add_stack()
                print(self)
            self.move(int(input("from stack number: ")), int(input("to stack number: ")))
        print('You Win!')


if __name__ == '__main__':
    random.seed(2)
    game = Game(4)
    game.run()
