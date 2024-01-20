import numpy as np
#変数クラスを作成
class Variable:
    def __init__(self, data):
        self.data = data

#テスト↓
data = np.array(2.0)
x = Variable(data)
print(x)
print(x.data)
