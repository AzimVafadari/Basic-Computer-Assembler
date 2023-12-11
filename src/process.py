from tables.tables import *


def first_pass(input_file_name):
    with open("./inputs/" + input_file_name, "r") as file:
        lines = file.read().split('\n')
        lc = 0
        for line in lines:
            parts = line.split()
            if line[0] not in PREUDOMSTRUCTION:
                label = line
                ADDRESS_SYMBOL_TABLE[label] = format(lc, '03X')
            elif line[0] == "ORG":
                lc = int(line[1], 16)
            elif line[0] == "END":
                second_pass(input_file_name)
            else:
                lc += 1


def second_pass(input_file_name):
    print("Coming soon ...")
