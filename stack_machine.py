import vm

if __name__ == "__main__":
    instructions = []
    with open("program", "r") as f:
        instructions = f.read().splitlines()

    stack_machine = vm.Machine()
    stack_machine.run_program(instructions)
