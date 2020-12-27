class MinStack:
    stack = None
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        node = {'val': x}
        minimum = x
        if len(self.stack) > 0:
            lastMin = self.getMin()
            minimum = min(lastMin, minimum)
        node['min'] = minimum
        self.stack.append(node)

    def pop(self) -> None:
        if len(self.stack) > 0:
            return self.stack.pop()['val']

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]['val']
    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]['min'];

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();  # --> Returns -3.
    minStack.pop();
    minStack.top();    #  --> Returns 0.
    minStack.getMin(); #  --> Returns -2.