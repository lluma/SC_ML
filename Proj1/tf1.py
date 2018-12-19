import tensorflow as tf
hi = tf.constant('Hi TensorFlow')
sess = tf.Session()
print(sess.run(hi))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))