class Stack:
    _FIRST = 0
    _LAST = -1

    def __init__(self, args: str):
        self.stack_a = self._get_args(args)
        self.stack_b = list()
        self.nbrof_mouvements = 0

    def _increment_mouvements(self):
        self.nbrof_mouvements += 1

    def mvmnts(self):
        return self.nbrof_mouvements

    def _get_args(self, args: str) -> list:
        ret = list()
        for nbr in args.split():
            ret.append(int(nbr))
        return ret
    
    def _swap(self, stack: list, i: int, j: int) -> None:
        stack[i] ^= stack[j]
        stack[j] ^= stack[i]
        stack[i] ^= stack[j]

    def _is_empty(self, stack: list):
        return len(stack) == 0

    def is_ok(self):
        return (sorted(self.stack_a) and self._is_empty(self.stack_b))

    def sa(self):
        self._swap(self.stack_a, Stack._FIRST, Stack._LAST);
        self._increment_mouvements()

    def sb(self):
        self._swap(self.stack_b, Stack._FIRST, Stack._LAST);
        self._increment_mouvements()

    def ss(self):
        self._swap(self.stack_a, Stack._FIRST, Stack._LAST);
        self._swap(self.stack_b, Stack._FIRST, Stack._LAST);
        self._increment_mouvements()

    def pa(self):
        if (self._is_empty(self.stack_b)):
            return ;
        popped_node = self.stack_b.pop(Stack._FIRST)
        self.stack_a.insert(Stack._FIRST, popped_node)
        self._increment_mouvements()

    def pb(self):
        if (self._is_empty(self.stack_a)):
            return ;
        popped_node = self.stack_a.pop(Stack._FIRST)
        self.stack_b.insert(Stack._FIRST, popped_node)
        self._increment_mouvements()

    def ra(self):
        if (len(self.stack_a) < 2):
            return ;
        head = self.stack_a.pop(Stack._FIRST)
        self.stack_a.append(head)
        self._increment_mouvements()

    def rb(self):
        if (len(self.stack_b) < 2):
            return ;
        head = self.stack_b.pop(Stack._FIRST)
        self.stack_b.append(head)
        self._increment_mouvements()

    def rr(self):
        if (len(self.stack_b) < 2) or (len(self.stack_a) < 2):
            return ;
        head_a = self.stack_a.pop(Stack._FIRST)
        self.stack_a.append(head_a)
        head_b = self.stack_b.pop(Stack._FIRST)
        self.stack_b.append(head_b)
        self._increment_mouvements()

    def rra(self):
        if (len(self.stack_a) < 2):
            return ;
        tail = self.stack_a.pop(Stack._LAST)
        self.stack_a.insert(Stack._FIRST, tail)
        self._increment_mouvements()

    def rrb(self):
        if (len(self.stack_b) < 2):
            return ;
        tail = self.stack_b.pop(Stack._LAST)
        self.stack_b.insert(Stack._FIRST, tail)
        self._increment_mouvements()

    def rrr(self):
        if (len(self.stack_b) < 2) or (len(self.stack_a) < 2):
            return ;
        tail_a = self.stack_a.pop(Stack._LAST)
        self.stack_a.insert(Stack._FIRST, tail_a)
        tail_b = self.stack_b.pop(Stack._LAST)
        self.stack_b.insert(Stack._FIRST, tail_b)
        self._increment_mouvements()

