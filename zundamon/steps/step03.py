import numpy as np
#変数クラスを作成
class Variable:
    def __init__(self, data):
        self.data = data
#関数の元を作成
#以下これを継承して様々な関数を作成する
class Function:
    def __call__(self, input):
        x = input.data #入力データを取り出す
        y = self.forward(x) #具体的な計算はforward関数で行う
        output = Variable(y)
        return output 
    def forward(self, x):
        return NotImplementedError()
#二乗する関数
class Square(Function):
    def forward(self, x):
        return x ** 2
#指数関数
class Exp(Function):
    def forward(self, x):
        return np.exp(x)
#テスト↓
A = Square()
B = Exp()
C = Square()
x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)
print(y)
print(y.data)
