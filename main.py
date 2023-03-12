import sys
import subprocess
from stack import Stack

def apply_operations(stack, operations):
    ops = {
        "sa": stack.sa,
        "sb": stack.sb,
        "ss": stack.ss,
        "pa": stack.pa,
        "pb": stack.pb,
        "ra": stack.ra,
        "rb": stack.rb,
        "rr": stack.rr,
        "rra": stack.rra,
        "rrb": stack.rrb,
        "rrr": stack.rrr,
    }

    for op in operations.split():
        if op in ops:
            ops[op]()
        else:
            sys.stderr.write(f"Error: \"{op}\" is not a valid mouvement")
            exit(1)

if __name__ == "__main__":
    args = sys.argv[1]
    process = subprocess.Popen(["./push_swap", args], stdout=subprocess.PIPE)
    output, error = process.communicate()
    operations = output.decode().strip()

    stack = Stack(args)
    apply_operations(stack, operations)

    if stack.is_ok():
        print("The list is sorted!")
    else:
        print("The list is not sorted.")

