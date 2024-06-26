# @Version: python3.10
# @Time: 2024/3/22 0:21
# @Description: 
# @File: U4S7.py
# @Software: PyCharm
# @Author: PlutoCtx
# @Email: ctx195467@163.com
# @User: chent


import tensorflow as tf
tf.reset_default_graph()
global_step = tf.train.get_or_create_global_step()
step = tf.assign_add(global_step, 1)

with tf.train.MonitoredTrainingSession(checkpoint_dir='log/checkpoints',save_checkpoint_secs  = 2) as sess:
    print(sess.run([global_step]))
    while not sess.should_stop():
        i = sess.run( step)
        print( i)
