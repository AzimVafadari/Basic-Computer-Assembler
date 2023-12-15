from tables.tables import *


def run(input_file_name):
    first_pass(input_file_name)


def first_pass(input_file_name):
    with open("./inputs/" + input_file_name, "r") as file:
        lines = file.read().split('\n')
        lc = 0
        for line in lines:
            parts = line.split()
            # شناسایی سمبل بودن در خط
            if parts[0][-1] == ",":
                label = line[0][:-1]
                # ذخیره کردن سمبل در جدول سمبل ها
                ADDRESS_SYMBOL_TABLE[label] = format(lc, '03X')
            elif line[0] == "ORG":
                lc = int(line[1], 16)
            elif line[0] == "END":
                second_pass(input_file_name)
            lc += 1


def second_pass(input_file_name):
    with open("./inputs/" + input_file_name, "r") as file:
        lines = file.read().split('\n')
        lc = 0
        output = dict()
        for line in lines:
            parts = line.split()
            word = parts[0]
            length = len(parts)
            if length == 1:

            elif length == 2:

            elif length == 3:

            elif length == 4: