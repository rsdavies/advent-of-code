

def meets_criteria(password: int) -> bool:
    # criteria for passwords
    # is a 6 digit number
    if type(password) is not int:
        raise TypeError("password must be an integer")

    str_pass = str(password)
    list_pass = [int(digit) for digit in str_pass]
    if len(list_pass) != 6:
        raise ValueError("password must be 6 digits long")

    # two adjacent digits are the same,
    # but must not be part of a larger group of matching digits
    # left to right, the digits never decrease, they increase or stay the same
    increasing = []
    same = []
    for i in range(0, len(list_pass) - 1):
        if list_pass[i] <= list_pass[i+1]:
            increasing.append(True)
        else:
            increasing.append(False)

        if list_pass[i] == list_pass[i+1]:
            same.append(True)
        else:
            same.append(False)

    if any(same):
        for digit in list_pass:
            if list_pass.count(digit) == 2:
                not_more_than_doubles = True
                break
            else:
                not_more_than_doubles = False
    else:
        not_more_than_doubles = False

    password_meets_criteria = all(increasing) and not_more_than_doubles

    return password_meets_criteria


if __name__ == "__main__":
    password_range = [124075, 580769]

    met_criteria = [password for password in range(password_range[0], password_range[1]+1) if meets_criteria(password)]
    print(len(met_criteria))

