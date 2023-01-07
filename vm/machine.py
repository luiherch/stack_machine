import vm
import sys


class Machine:
    def __init__(self) -> None:
        self.pc = 0
        self.d_stack = vm.Stack()
        self.i_stack = vm.Stack()

        self.d_map = {
            "%": self.mod,
            "*": self.mul,
            "+": self.plus,
            "-": self.minus,
            "print": self.print,
            "/": self.div,
            "==": self.eq,
        }

    def cast_numbers(a):
        # cast string numerics into numbers
        foo = []
        for i in a:
            try:
                foo.append(int(i) if float(i).is_integer() else float(i))
            except ValueError:
                foo.append(i)
        return foo

    def run_program(self, inst_list: list):
        inst_list = Machine.cast_numbers(inst_list)
        # Load instructions
        for inst in reversed(inst_list):
            # ignore comments
            if str(inst).startswith("#"):
                continue
            self.i_stack.push(inst)

        while len(self.i_stack.queue) > 0:
            self.pc = self.pc + 1
            inst = self.i_stack.pop()
            if inst in self.d_map:
                self.d_map[inst]()
            elif isinstance(inst, int):
                self.d_stack.push(inst)
            else:
                raise RuntimeError(f"Unknown instruction: {inst}")

    def mod(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a % b)

    def mul(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a * b)

    def plus(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a + b)

    def minus(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a - b)

    def div(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a / b)

    def eq(self):
        a = self.d_stack.pop()
        b = self.d_stack.pop()
        self.d_stack.push(a == b)

    def print(self):
        sys.stdout.write(str(self.d_stack.pop()) + "\n")
        sys.stdout.flush()
