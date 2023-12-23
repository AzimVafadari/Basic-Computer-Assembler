def handle_error(file_name):
    with open('../inputs/' + file_name, "r") as file:
        lines = file.read().split('\n')
        for line in lines:
            if line[-1] != 'END':
                print("""Your code hasn't any END""")
            if "ORG" not in line[0]:
                print("""Your code hasn't any ORG""")
