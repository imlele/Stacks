import copy
from typing import Tuple, List

from Stack import Game


def minimax(game: Game, depth, maximizing_player):
    # current_hash = state_hash(game)

    # if depth == 0 or game.is_done() or current_hash in visited_states:
    #     return game.purity()
    if depth == 0 or game.is_done():
        return game.purity()
    # visited_states.add(current_hash)

    if maximizing_player:
        max_eval = float('-inf')
        for move in game.possible_moves():
            child_game = copy.deepcopy(game)
            child_game.apply_move(*move)
            eval = minimax(child_game, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.possible_moves():
            child_game = copy.deepcopy(game)
            child_game.apply_move(*move)
            eval = minimax(child_game, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def best_move(game, depth, visited_states):
    best_eval = float('-inf')
    best_move = None
    for move in game.possible_moves():
        child_game = copy.deepcopy(game)
        child_game.apply_move(*move)
        current_state = state_hash(child_game)
        if current_state in visited_states:
            continue
        else:
            eval = minimax(child_game, depth - 1, False)  # Assuming AI is the maximizing player
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move


def state_hash(game):
    # Convert the game state to a string or another data structure
    # that can be uniquely hashed.
    return hash(str(game))


if __name__ == '__main__':
    myGame = Game(8, 4)
    visited_states = set()
    count = 0
    while not myGame.is_done():
        count +=1
        next_move = best_move(myGame, 3, visited_states)
        # print(next_move)
        # print(myGame)
        myGame.apply_move(*next_move)
        visited_states.add(state_hash(myGame))
    print(myGame)
    print(f"SOLVED IN {count} STEPS WITH {myGame.empty - 1} STACK ADDED" )
