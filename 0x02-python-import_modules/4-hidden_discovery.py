#!/usr/bin/python3

import dis


def main():
    with open('hidden_4.pyc', 'rb') as file:
        bytecode = file.read()

    instructions = dis.get_instructions(bytecode)
    for instruction in instructions:
        if instruction.opname == 'LOAD_NAME' and not instruction.argval.startswith('__'):
            print(instruction.argval)


if __name__ == "__main__":
    main()
