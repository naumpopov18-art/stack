class Stack():
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
    
    def check_staples(self, string):
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in string:
            if char in '({[':
                self.push(char)
            elif char in ')}]':
                if self.pop() != pairs[char]:
                    return 'Несбалансированно'
        
        return 'Сбалансированно' if self.is_empty() else 'Несбалансированно'
    
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    # s.push(1)
    print(s.peek())
    print(s.check_staples("()"))

    
