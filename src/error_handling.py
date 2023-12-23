def handle_error(file_name):
    with open('./inputs/' + file_name, "r") as file:
        lines = file.read().split('\n')
        correct_format = True
        for line in lines:
            if line[-1] != 'END':
                print("""Your code hasn't any END""")
                correct_format = False
            if "ORG" not in line[0]:
                print("""Your code hasn't any ORG""")
                correct_format = False
            if int(line[1], 16) > 4095:
                print("Your origin address is bounded up")
                correct_format = False
            if int(line[1], 16) < 0:
                print("Your origin address is bounded down")
                correct_format = False
        return correct_format


def error_in_line(message: str, line_number: int):
    print(message + "(line " + str(line_number) + ")")
