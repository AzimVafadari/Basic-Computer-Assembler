import struct

from src.io import output_writer
from tables.tables import *

ADDRESS_SYMBOL = dict()


def run(input_file_name):
    first_pass(input_file_name)


def first_pass(input_file_name):
    with open("./inputs/" + input_file_name, "r") as file:
        lines = file.read().split('\n')
        lc = 0
        for line in lines:
            parts = line.split()
            # شناسایی سمبل بودن در خط
            if parts[0][-1] == ',':
                label = parts[0][:-1]
                # ذخیره کردن سمبل در جدول سمبل ها
                ADDRESS_SYMBOL[label] = str(lc)
            elif parts[0] == 'ORG':
                lc = int(parts[1]) - 1
            elif parts[0] == 'END':
                second_pass(input_file_name)
            lc += 1


def second_pass(input_file_name: str):
    with open("./inputs/" + input_file_name, "r") as file:
        lines = file.read().split('\n')
        lc = 0
        output = dict()
        for line in lines:
            parts = line.split()
            word = parts[0]
            length = len(parts)
            # دستور ما یا END هست یا ثباتی است
            if length == 1:
                # END
                if word == "END":
                    header_list = list(output.keys())
                    header_list.sort()
                    for memory_location in header_list:
                        integer = int(output[memory_location], 16)
                        output[memory_location] = struct.pack('>i', integer)
                    output_writer('./outputs/out.asm', header_list, output, 't')
                elif word in NON_MRI:
                    output[lc] = hex(NON_MRI[word])
                else:
                    print("Your code has an error in line " + lc)
            elif length == 2:
                if word == "ORG":
                    lc = int(parts[1]) - 1
                else:
                    #دستور مربوط به بخش MRI است
                    if word in MRI:
                        hex_code = hex(int(MRI[word][0] + ADDRESS_SYMBOL[parts[1]], 16))
                        output[lc] = hex_code
                        #دستور از این قالب پیروی میکند -> HEX 0000 و یا DEC -20
                    else:
                        output[lc] = convert_number_to_hex(word, parts[1])
            elif length == 3:
                indirect = True
                #دستور ما از این نوع است -> ABC, LDA DIF
                if word[-1] == ',':
                    index1 = 1
                    index2 = 0
                    # دستور ما از این نوع است -> ABC, HEX 0110
                    if parts[1] in PREUDOMSTRUCTION[1:3]:
                        indirect = False
                # دستور ما از این نوع است -> LDA DIF I
                else:
                    index1 = 0
                    index2 = 1
                if indirect:
                    hex_code = hex(int(MRI[parts[index1]][index2] + ADDRESS_SYMBOL[parts[1 + index1]], 16))
                else:
                    hex_code = convert_number_to_hex(parts[1], parts[2])
                output[lc] = hex_code
            # دستور ما از این نوع است -> ABC, LDA DIF I
            elif length == 4:
                hex_code = hex(int(MRI[parts[1]][1] + ADDRESS_SYMBOL[parts[2]], 16))
                output[lc] = hex_code
            lc += 1


def convert_number_to_hex(word: str, number: str):
    if word == PREUDOMSTRUCTION[1]:  # word == HEX
        return hex(int(number, 16))
    else:  # word == DEC
        return hex(int(number))
