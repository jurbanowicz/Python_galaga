RESULTS_FILE = "main/python/game/stats/game_results.csv"

'''Result file contains data save as
PLAYER_NAME, SCORE'''

def save_game_result(score: int, player_name: str = "Player"):
    data = get_stats()
    if player_name == "":
        player_name = player_name + str(len(data))
    name = player_name
    data.append((name, score))

    data.sort(key = lambda x: x[1], reverse = True)

    n = len(data)
    if n > 100:
        n = 100
    with open(RESULTS_FILE, "w") as f:
        for line in data[:n]:
            f.write(line[0] + "," + str(line[1]) + "\n")


def get_stats() -> list:
    with open(RESULTS_FILE, "r") as f:
        result_lines = f.read().splitlines()

    if len(result_lines) < 1:
        return []
    
    data = []
    for line in result_lines:
        tmp = line.split(',')
        player_name = tmp[0]
        score = int (tmp[1])
        data.append((player_name, score))

    return data
