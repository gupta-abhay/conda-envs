import tensorflow as tf

print ("Tensorflow version is: " + str(tf.__version__))
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
