
class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.memory = {}

    def has_key(self, name):  # variable name
        return name in self.memory.keys()

    def get(self, name):         # gets from memory current value of variable <name>
        return self.memory.get(name)

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.memory[name] = value

    def __repr__(self):
        return self.name

class MemoryStack:

    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        self.stack = [memory] if memory else [Memory("Top Level")]

    def get(self, name):             # gets from memory stack current value of variable <name>
        indices = reversed(range(0, len(self.stack)))
        for i in indices:
            if self.stack[i].has_key(name):
                return self.stack[i].get(name)
        raise KeyError

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stack[-1].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        indices = reversed(range(0, len(self.stack)))
        for i in indices:
            if self.stack[i].has_key(name):
                self.stack[i].put(name,value)
        raise KeyError

    def push(self, memory): # pushes memory <memory> onto the stack
        self.stack.append(memory)

    def pop(self):          # pops the top memory from the stack
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
