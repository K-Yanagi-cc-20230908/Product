import numpy as np
#変数クラスを作成
class Variable:
    def __init__(self, data):
        #ndarrayのみを使用するのでそれ以外の型の場合エラーが出るようにする
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{} is not supported'.format(type(data)))
        self.data = data
        self.grad = None #微分したデータを格納する
        self.creator = None #出力元の関数を記録
    def set_creator(self, func):
        self.creator = func
    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data) #self.dataと同一形式で各要素を1のインスタンスを生成し代入
        funcs = [self.creator] #自身のもとになった関数を配列に入れる
        while funcs:
            f = funcs.pop() #1.関数を取得
            if f is not None:
                x, y = f.input, f.output #2.入、出力を取得
                x.grad = f.backward(y.grad) #3.関数のバックワードメソッドを呼ぶ
                if x.creator is not None:
                    funcs.append(x.creator) #4.に一つ前の関数を追加
#ndarrayの形を保つ
def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x
#関数の元を作成
#以下これを継承して様々な関数を作成する
class Function:
    def __call__(self, inputs):
        xs = [x.data for x in inputs] #入力データを取り出す
        ys = self.forward(xs) #具体的な計算はforward関数で行う
        outputs  = [Variable(as_array(y)) for y in ys]
        for output in outputs:
            output.set_creator(self) #Valiableのset_creatorメソッドを使って関数を記録
        self.inputs = inputs #入力データを保持
        self.outputs = outputs #出力も記録
        return outputs 
    def forward(self, xs):
        return NotImplementedError()
    def backward(self, gys):
        return NotImplementedError()
#成分の総和
class Add(Function):
    def forward(self, xs):
        x0, x1 = xs
        y = x0 + x1
        return (y,)
#テスト↓
xs = [Variable(np.array(2)), Variable(np.array(3))]
f = Add()
ys = f(xs)
y = ys[0]
print(y.data)
