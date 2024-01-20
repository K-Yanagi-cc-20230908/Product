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
#テスト↓
x = Variable(np.array(10.0))
f = Square()
y = f(x)
print(y)
print(y.data)
