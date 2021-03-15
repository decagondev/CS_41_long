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


# Memory
# ram = [0] * 255

ram = [
    PRINT_NAME,
    PRINT_NAME,
    PRINT_NUM,
    123,
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
        pass
        pc += 1

    # decode
    elif inst == PRINT_NUM:
        # execute
        print(ram[pc + 1])
        pc += 2

    # decode
    else:
        print(f"Unknown instruction {inst}")
        running = False
