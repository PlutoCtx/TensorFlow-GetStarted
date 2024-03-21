# @Version: python3.10
# @Time: 2024/3/21 21:02
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: TestTry.py
# @Software: PyCharm
# @User: chent

import numpy as np
train_X, step = np.linspace(-1, 1, num=9, retstep=True)
for i in range(len(train_X) - 1):
    print(i, train_X[i], train_X[i + 1] - train_X[i])
print(type(train_X))

print('\n\n\n\n\n')
print(train_X, step)
