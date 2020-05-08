# Conda Enviroments for Deep Learning

This repository is for replicating conda environments for deep learning. There are two primary libraries for which I am providing base environment files

* [PyTorch](https://pytorch.org/)
* [TensorFlow](https://www.tensorflow.org/)

## Environments

Here is a more detailed view of the files:

| File         	| Package    	| Package Version 	| CUDA Version 	| Python Version 	|
|:--------------	|:------------	|:-----------------:	|:--------------:	|:----------------:|
| tf_cuda9     	| Tensorflow 	| 1.12.0            	| 9.2          	| 3.6.8          	|
| tf_cuda10    	| Tensorflow 	| 1.13.1            	| 10.1         	| 3.7.3          	|
| torch_cuda9  	| Pytorch    	| 1.5             	| 9.2          	| 3.8.2          	|
| torch_cuda10 	| Pytorch    	| 1.5             	| 10.2         	| 3.8.2          	|

The environment files can be found in the `envs` folder.


## Tests

To test the installation, you can run the corresponding tests in the `tests` folder.

* For PyTorch
```
python test_torch_installation.py
```

* For TensorFlow
```
python test_tf_installation.py
```

__Note__: The test for tensorflow starts a session, so run it on a GPU card which has some free GPU memory.
