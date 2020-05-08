import tensorflow as tf

print ("Tensorflow version is: " + str(tf.__version__))
print ("Is CUDA Available: ", tf.test.is_gpu_available(cuda_only=True))
print ("Num of physical devices are: ", len(tf.config.list_physical_devices('GPU')))
