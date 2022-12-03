def valid_password(path):
    with open(path, 'r') as file:
        count = 0
        for string in file:
            [pattern, password] = string.split(': ')
            [min_rep, max_rep], char = pattern[:-2].split('-'), pattern[-1]
            if int(min_rep) <= password.count(char) <= int(max_rep):
                count += 1
        return count



if __name__ == '__main__':
    print(valid_password('./input'))
    print(valid_password_2('./input'))
