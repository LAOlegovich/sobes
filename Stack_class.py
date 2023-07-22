class Stack():

    def __init__(self, data: list) -> None:
        self.data = data

    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> None:
        if self.size() == 0:
            return True
        else: False

    def push(self,element) -> None:
        self.data.append(element)

    def pop(self) -> str:
        if self.is_empty():
            return None
        s = self.data[-1]
        del self.data[-1]
        return s
    
    def peek(self) -> str:
        if self.is_empty():
            return None
        return self.data[-1]
    

if __name__ == "__main__":


    St = Stack([])

    print(St.size())

    print(St.peek())

