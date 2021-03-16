import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
program = []
if len(sys.argv) < 2:
    print("Usage: fileio.py <filename>")
else:
    try:
        file_name = sys.argv[1]
        with open(file_name) as f:
                for line in f:
                    num_string = line.split("#")[0].strip()

                    if num_string == '':
                        continue

                    int_of_bin = int(num_string, 2)

                    # # print(f"{int_of_bin:08b}: {int_of_bin}")
                    # if int_of_bin == LDI:
                    #     print("LDI")
                    # elif int_of_bin == LDI:
                    #     print("LDI")
                    # elif int_of_bin == PRN:
                    #     print("PRN")
                    # elif int_of_bin == HLT:
                    #     print("HLT")
                    program.append(int_of_bin)
    except FileNotFoundError:
        print("I can not find the file!!!!!!!!")
        
print(program)