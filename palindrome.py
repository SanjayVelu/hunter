class Stack:
    def __init__(self):
        self.items = []
    def is.empty(self):
        return self.items = []
    def push(self, data)
        self.items.append(data)
    def pop(self,data)
        return self.items.pop()
s = stack()
text = input('enter the string:')
for character in text:
    s.push(character)
reversed text = ' '
while not s.is_empty():
    reversed_text = reversed text + s.pop()
if text == reversed_text:
    print("YES")
else:
    print("NO")

   
