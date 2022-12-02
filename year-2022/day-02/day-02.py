def rpc(path):
    with open(path, 'r') as file:
        score = 0
        for game in file:
            game = game[:-1]
            score += 1 if game[-1] == 'X' else 2 if game[-1] == 'Y' else 3
            if game == 'A Y' or game == 'B Z' or game == 'C X':
                score += 6
            elif game == 'A X' or game == 'B Y' or game == 'C Z':
                score += 3
        return score

def play_rpc(path):
    with open(path, 'r') as file:
        score = 0
        for game in file:
            game = game[:-1]
            result = 0 if game[-1] == 'X' else 3 if game[-1] == 'Y' else 6
            opp = 1 if game[0] == 'A' else 2 if game[0] == 'B' else 3
            you = opp if result == 3 else opp - 1 if result == 0 else opp + 1
            score += result + (3 if you % 3 == 0 else you%3)
        return score


if __name__ == '__main__':
    print(rpc('input'))
    print(play_rpc('input'))
