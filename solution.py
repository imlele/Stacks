import copy
import random
from Stack import Game
from tqdm import tqdm
from typing import Tuple, List

STACK_NUM = 100
COLOR_NUM = 15


def best_move(game, visited_states):
    best_purity = float('-inf')
    next_move = None
    for move in game.possible_moves():
        child_game = copy.deepcopy(game)
        child_game.apply_move(*move)
        current_state = state_hash(child_game)
        if current_state in visited_states:
            continue
        else:
            current_purity = child_game.purity()
            if current_purity > best_purity:
                best_purity = current_purity
                next_move = move
    return next_move


def state_hash(game):
    return hash(str(game))


def AI_run(game):
    states = set()
    count = 0
    total_iterations = 1

    progress_bar = tqdm(total=total_iterations, desc="Processing", ncols=100)
    last_progress = 0
    while not game.is_done():
        count += 1
        move = best_move(game, states)
        if not move:
            game.add_stack()
            move = best_move(game, states)
        game.apply_move(*move)
        states.add(state_hash(game))
        current_progress = game.purity()
        if current_progress != last_progress:
            progress_bar.update(current_progress - last_progress)
            last_progress = current_progress
    progress_bar.close()
    return count


if __name__ == '__main__':
    # random.seed(2)
    game = Game(STACK_NUM, COLOR_NUM)
    round_num = AI_run(game)
    print(game)
    print(f"SOLVED IN {round_num} STEPS WITH {game.empty - 1} STACK ADDED")
