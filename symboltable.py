#!/usr/bin/python


class Symbol(object):
    pass

class VariableSymbol(Symbol):

    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.name = name
        self.parent = parent
        self.symbols = {}

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if self.symbols.__contains__(name):
            return self.symbols[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        new_scope = SymbolTable(self, name)
        new_scope.name = name
        new_scope.parent = self
        new_scope.symbols = deepcopy(self.symbols)
        return new_scope

    def popScope(self):
        parent_scope = self.get_parent_scope()
        if parent_scope is None:
            print('No higher scopes')
        return parent_scope
