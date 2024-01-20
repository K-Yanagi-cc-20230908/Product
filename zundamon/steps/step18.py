import weakref
import numpy as np
import contextlib #このモジュールを使うとwith文で逆伝搬法の有効/無効が実行可能になる。
#############################################################
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
        self.generation = 0 #世代を記録
    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1 #世代を記録
    def backward(self, retain_grad = False): #retain_gradは勾配を保存するかを決める
        if self.grad is None:
            self.grad = np.ones_like(self.data) #self.dataと同一形式で各要素を1のインスタンスを生成し代入
        funcs = []
        seen_set = set()
        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key = lambda x: x.generation) #世代の昇順に並べる
        add_func(self.creator)
        while funcs:
            f = funcs.pop() #1.一番世代の大きい関数を取得
            if f is not None:
                gys = [output().grad for output in f.outputs] #前の微分データ取得
                gxs = f.backward(*gys) #微分
                if not isinstance(gxs, tuple):
                    gxs = (gxs,)
                for x, gx in zip(f.inputs, gxs): #https://note.nkmk.me/python-zip-usage-for/を見れば分かる
                    if x.grad is None:
                        x.grad = gx
                    else:
                        x.grad = x.grad + gx
                    if x.creator is not None:
                        add_func(x.creator) #4.それぞれの要素の一つ前の関数を追加
                if not retain_grad:
                    for y in f.outputs:
                        y().grad = None #reatin_grad = Falseなら入力以外の勾配を削除 
    #保存されている微分値を消す
    def cleargrad(self):
        self.grad = None
#############################################################
#ndarrayの形を保つ
def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x
##################################################
@contextlib.contextmanager
def using_config(name, value):
    old_value = getattr(Config, name)
    setattr(Config, name, value)
    try:
        yield
    finally:
        setattr(Config, name, old_value)
#############################################################
#逆伝搬の有効/無効モードを切り替える
class Config:
    enable_backprop = True
##################################################
#関数の元を作成
#以下これを継承して様々な関数を作成する
class Function:
    def __call__(self, *inputs): #*をつけると可変長になる
        xs = [x.data for x in inputs] #入力データを取り出す
        ys = self.forward(*xs) #具体的な計算はforward関数で行う
        if not isinstance(ys, tuple):
            ys = (ys,) #ysがtuple出ない場合はtupleに変換
        outputs  = [Variable(as_array(y)) for y in ys]
        if Config.enable_backprop: #ここで逆伝搬法の有効/無効を切り替える
            self.generation = max([x.generation for x in inputs]) #入力されたデータのうち最大の世代のものを世代として採用
            for output in outputs:
                output.set_creator(self) #Valiableのset_creatorメソッドを使って関数を記録
            self.inputs = inputs #入力データを保持
            self.outputs = [weakref.ref(output) for output in outputs] #出力も記録
        return outputs if len(outputs) > 1 else outputs[0] #リストの要素が一つならばリストではなくその要素を返す
    def forward(self, xs):
        return NotImplementedError()
    def backward(self, gys):
        return NotImplementedError()
#############################################################
#成分の総和
class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y
    def backward(self, gy):
        return gy, gy
def add(x0, x1):
    return Add()(x0, x1)
#二乗
class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y
    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2 * x * gy
        return gx
def square(x):
    return Square()(x)
#テスト↓
with using_config('enable_backprop', False):
    x = Variable(np.array(2.0))
    y = square(x)
    print(y.data)


