#coding=utf-8

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
"""

class MinStack:
    """
    不同步的方法
    只有当data的栈顶元素等于helper的栈顶元素，helper才pop，也只有当x比栈顶元素小的时候helper才入栈

    同步方式
    保证data和helper的元素数量一样，data入栈元素比helper小，那么x也在helper中入栈，比helper大，那么就又入栈一个helper的栈顶元素
    """
    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        if self.data:
            if self.data[-1] == self.helper[-1]:
                self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

if __name__ == "__main__":
    m = MinStack()
    m.push(2)
    m.push(1)
    m.push(3)
    print(m.getMin())
    m.pop()
    print(m.getMin())