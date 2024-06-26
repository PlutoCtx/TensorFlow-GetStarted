# @Version: python3.10
# @Time: 2024/3/21 16:36
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @File: LogisticRegressionFitting.py
# @Software: PyCharm
# @User: chent


import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()

import numpy as np
import matplotlib.pyplot as plt

plotdata = {"batchsize": [], "loss": []}


def moving_average(a, w=10):
    if len(a) < w:
        return a[:]
    return [val if idx < w else sum(a[(idx - w):idx]) / w for idx, val in enumerate(a)]


# 生成模拟数据
train_X = np.linspace(-1, 1, 100)
# y=2x，但是加入了噪声
# np.random.randn(*train_X.shape)等同于np.random.randn(100)，randn返回一个或一组样本，具有标准正态分布
#
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3
# 显示模拟数据点
plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.legend()
plt.show()

# 创建模型
# 占位符

# import tensorflow as tf

tf.compat.v1.disable_v2_behavior()
X = tf.compat.v1.placeholder(shape=[None, 2], dtype=tf.float32)
# X = tf.placeholder("float")
# X = tf.placeholder("float")
Y = tf.compat.v1.placeholder(shape=[None, 2], dtype=tf.float32)

# Y = tf.placeholder("float")
# 模型参数
W = tf.Variable(tf.random.normal([1]), name="weight")
b = tf.Variable(tf.zeros([1]), name="bias")

# 前向结构
z = tf.multiply(X, W) + b

# 反向优化
cost = tf.reduce_mean(tf.square(Y - z))
learning_rate = 0.01
tf.compat.v1.disable_eager_execution()

# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)  # Gradient descent
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)


# 初始化变量
# init = tf.global_variables_initializer()
init = tf.compat.v1.global_variables_initializer()
# 训练参数
training_epochs = 20
display_step = 2

tf.compat.v1.disable_eager_execution()
# sess=tf.compat.v1.Session()
# 启动session
# with tf.Session() as sess:
with tf.compat.v1.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # 显示训练中的详细信息
        if epoch % display_step == 0:
            loss = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
            print("Epoch:", epoch + 1, "cost=", loss, "W=", sess.run(W), "b=", sess.run(b))
            if not (loss == "NA"):
                plotdata["batchsize"].append(epoch)
                plotdata["loss"].append(loss)

    print(" Finished!")
    print("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}), "W=", sess.run(W), "b=", sess.run(b))
    # print ("cost:",cost.eval({X: train_X, Y: train_Y}))

    # 图形显示
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    plotdata["avgloss"] = moving_average(plotdata["loss"])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata["batchsize"], plotdata["avgloss"], 'b--')
    plt.xlabel('Minibatch number')
    plt.ylabel('Loss')
    plt.title('Minibatch run vs. Training loss')

    plt.show()

    print("x=0.2，z=", sess.run(z, feed_dict={X: 0.2}))

# 原代码
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# plotdata = { "batchsize":[], "loss":[] }
# def moving_average(a, w=10):
#     if len(a) < w:
#         return a[:]
#     return [val if idx < w else sum(a[(idx-w):idx])/w for idx, val in enumerate(a)]
#
#
# #生成模拟数据
# train_X = np.linspace(-1, 1, 100)
# train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3 # y=2x，但是加入了噪声
# #显示模拟数据点
# plt.plot(train_X, train_Y, 'ro', label='Original data')
# plt.legend()
# plt.show()
#
#
#
#
# # 创建模型
# # 占位符
# X = tf.placeholder("float")
# Y = tf.placeholder("float")
# # 模型参数
# W = tf.Variable(tf.random_normal([1]), name="weight")
# b = tf.Variable(tf.zeros([1]), name="bias")
#
# # 前向结构
# z = tf.multiply(X, W)+ b
#
# #反向优化
# cost =tf.reduce_mean( tf.square(Y - z))
# learning_rate = 0.01
# optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) #Gradient descent
#
# # 初始化变量
# init = tf.global_variables_initializer()
# # 训练参数
# training_epochs = 20
# display_step = 2
#
# # 启动session
# with tf.Session() as sess:
#     sess.run(init)
#
#     # Fit all training data
#     for epoch in range(training_epochs):
#         for (x, y) in zip(train_X, train_Y):
#             sess.run(optimizer, feed_dict={X: x, Y: y})
#
#         #显示训练中的详细信息
#         if epoch % display_step == 0:
#             loss = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
#             print ("Epoch:", epoch+1, "cost=", loss,"W=", sess.run(W), "b=", sess.run(b))
#             if not (loss == "NA" ):
#                 plotdata["batchsize"].append(epoch)
#                 plotdata["loss"].append(loss)
#
#     print (" Finished!")
#     print ("cost=", sess.run(cost, feed_dict={X: train_X, Y: train_Y}), "W=", sess.run(W), "b=", sess.run(b))
#     #print ("cost:",cost.eval({X: train_X, Y: train_Y}))
#
#     #图形显示
#     plt.plot(train_X, train_Y, 'ro', label='Original data')
#     plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
#     plt.legend()
#     plt.show()
#
#     plotdata["avgloss"] = moving_average(plotdata["loss"])
#     plt.figure(1)
#     plt.subplot(211)
#     plt.plot(plotdata["batchsize"], plotdata["avgloss"], 'b--')
#     plt.xlabel('Minibatch number')
#     plt.ylabel('Loss')
#     plt.title('Minibatch run vs. Training loss')
#
#     plt.show()
#
#     print ("x=0.2，z=", sess.run(z, feed_dict={X: 0.2}))
