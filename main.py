import datetime

from kakuro_simple import Kakuro
from kakuro_plus import KakuroPlus
from maps import custom_version, easy_puzzle, medium_puzzle, hard_puzzle, expert_puzzle


if __name__ == '__main__':
    for difficulty, map in {"custom": custom_version,"easy": easy_puzzle, "medium": medium_puzzle, "hard": hard_puzzle, "expert": expert_puzzle}.items():
        print(f"solving {difficulty} map")
        print(f"with simple version...")
        game = Kakuro(**map)
        game_plus = KakuroPlus(**map)

        cur_time = datetime.datetime.now()
        game.solve()
        game.show()
        new_time = datetime.datetime.now()
        print(f"{difficulty}: Time for simple version:", new_time - cur_time)

        print(f"with plus version...")
        cur_time = datetime.datetime.now()
        game_plus.solve()
        game_plus.show()

        new_time = datetime.datetime.now()
        print(f"{difficulty}:Time for plus version:", new_time - cur_time)
