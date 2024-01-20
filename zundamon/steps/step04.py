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
#数値微分を実行
def numerical_diff(f, x, eps = 0.0001):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps) 
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)   
#テスト↓
def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))
x = Variable(np.array(0.5))
dy = numerical_diff(f, x)
print(dy)
