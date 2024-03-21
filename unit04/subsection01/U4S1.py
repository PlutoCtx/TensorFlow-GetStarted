# @Version: python3.10
# @Time: 2024/3/22 0:18
# @Description: 
# @File: U1S1.py
# @Software: PyCharm
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @User: chent

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')  #定义一个常量
sess = tf.Session()                             #建立一个session
print (sess.run(hello))                        #通过session里面的run来运行结果
sess.close()                                     #关闭session


