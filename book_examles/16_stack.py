class ExtendedStack(list):
    def sum(self):
        sum = self.pop() + self.pop()
        return self.append(sum)
    def sub(self):
        sub = self.pop() - self.pop()
        return self.append(sub)
    def mul(self):
        mul = self.pop() * self.pop()
        return self.append(mul)
    def div(self):
        div = self.pop() // self.pop()
        return self.append(div)
