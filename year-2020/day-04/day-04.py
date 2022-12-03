def check_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in required_fields:
        if not(field in passport):
            return False
    return True

def valid_passport(path):
    with open(path, 'r') as file:
        count = 0
        passport = []
        for line in file:
            if line == '\n':
                print(passport,  check_fields(passport))
                if check_fields(passport):
                    count += 1
                passport = []
            else:
                passport.extend(field[:3] for field in line.split(' '))

        return count



if __name__ == '__main__':
    print(valid_passport('./input'))
    print(valid_passport('./input'))
