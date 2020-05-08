import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

tf.logging.set_verbosity('ERROR')
tf.autograph.set_verbosity(0)
print ("Tensorflow version is: " + str(tf.__version__))
print ("Is CUDA Available: ", tf.test.is_gpu_available(cuda_only=True))

if str(tf.__version__) == '2.1':
    print ("Num of physical devices are: ", len(tf.config.list_physical_devices('GPU')))
elif str(tf.__version__) == '1.15.0':
    print ("Num of physical devices are: ", len(tf.config.experimental.list_physical_devices('GPU')))
else:
    raise ValueError('list_physical_devices support not available')
