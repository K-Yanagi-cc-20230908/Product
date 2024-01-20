import numpy as np
#変数クラスを作成
class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None #微分したデータを格納する
        self.creator = None #出力元の関数を記録
    def set_creator(self, func):
        self.creator = func
    def backward(self):
        f = self.creator #1.関数を取得
        if f is not None:
            x = f.input #2.入力を取得
            x.grad = f.backward(self.grad) #3.関数のバックワードメソッドを呼ぶ
            x.backward() #再帰的に繰り返す
#関数の元を作成
#以下これを継承して様々な関数を作成する
class Function:
    def __call__(self, input):
        x = input.data #入力データを取り出す
        y = self.forward(x) #具体的な計算はforward関数で行う
        output = Variable(y)
        output.set_creator(self) #Valiableのset_creatorメソッドを使って関数を記録
        self.input = input #入力データを保持
        self.output = output #出力も記録
        return output 
    def forward(self, x):
        return NotImplementedError()
    def backward(self, gy):
        return NotImplementedError()
#二乗する関数
class Square(Function):
    def forward(self, x):
        return x ** 2
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx
#指数関数
class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
#テスト↓
A = Square()
B = Exp()
C = Square()
x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)
#逆伝搬
y.grad = np.array(1.0)
y.backward()
print(x.grad)
