def handle_error(file_name):
    with open('./inputs/' + file_name, "r") as file:
        lines = file.read().split('\n')
        is_true = [True, False, True, True]
        for line in lines:
            if lines[-1] != 'END':
                if is_true[0]:
                    print("""Your code hasn't any END""")
                    is_true[0] = False
                is_true[0] = False
            if "ORG" in line.split():
                is_true[1] = True
                parts = line.split()
                if int(parts[1], 16) > int('fff', 16):
                    if is_true[2]:
                        print("Your origin address is bounded up")
                        is_true[2] = False
                if int(parts[1], 16) < 0:
                    if is_true[3]:
                        print("Your origin address is bounded down")
                        is_true[3] = False
    if not is_true[1]:
        print("""Your code hasn't any ORG""")
    return is_true[0] and is_true[1] and is_true[2] and is_true[3]


def error_in_line(message: str, line_number: int):
    print(message + "(line " + str(line_number) + ")")
