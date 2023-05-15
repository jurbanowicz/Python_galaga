from stat_saver import save_game_result

def save_test():
    save_game_result(100, "JACEK")
    save_game_result(125, "ANDRZEJ")
    save_game_result(50, "JACEK")
    save_game_result(250, "JACEK")

if __name__ == "__main__":
    save_test()