# class A:
#     def __init__(self):
#         pass


# my_a = A()

# print(my_a)

# components of a computer to us.
# RAM
# CPU

# opcodes
LOAD_NUM = 0b00000000
PRINT_NUM = 0b00000001
PRINT_REG = 0b11001100
HALT = 0b00001000
PRINT_NAME = 0b10101100
ADD = 0b11101100

LDI = 0b10000010
PRN = 0b01000111

# Memory
# ram = [0] * 255

ram = [
    PRINT_NAME,
    PRINT_NAME,
    PRINT_NUM,
    123,
    LDI,
    0,
    100,
    LDI,
    1,
    20,
    ADD,
    0,
    1,
    PRINT_REG,
    0,
    HALT,
]

# program counter
pc = 0

# r0 - r7
registers = [0] * 8

# running loop
running = True

while running:
    # fetch
    inst = ram[pc]
    opa = ram[pc + 1]
    opb = ram[pc + 2]

    # decode
    if inst == PRINT_NAME:
        # execute
        print("Tom")
        pc += 1
    
    # decode
    elif inst == HALT:
        # execute
        running = False
        pc += 1
    
    # decode
    elif inst == LOAD_NUM:
        # execute
        # get the num.
        num = opa
        # get the reg index.
        reg_index = opb
        # put the number in the registers list at the index of reg_index
        registers[reg_index] = num
        pc += 3

        # decode
    elif inst == LDI:
        # execute
        # get the reg index.
        reg_index = opa
        # get the num.
        num = opb
        # put the number in the registers list at the index of reg_index
        registers[reg_index] = num
        pc += 3

    # decode
    elif inst == PRINT_NUM:
        # execute
        print(opa)
        pc += 2

    # decode
    elif inst == PRINT_REG:
        # execute
        # get reg index.
        reg_index = opa
        print(registers[reg_index])
        pc += 2

    elif inst == ADD:
        reg_index1 = opa
        reg_index2 = opb

        registers[reg_index1] += registers[reg_index2]
        pc += 3



    # decode
    else:
        print(f"Unknown instruction {inst}")
        running = False
