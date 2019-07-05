# Conda Enviroments for Deep Learning

This repository is for replicating conda environments for deep learning. There are two primary libraries for which I am providing base environment files

* [PyTorch](https://pytorch.org/)
* [TensorFlow](https://www.tensorflow.org/)

Here is a more detailed view of the files:

| File         	| Package    	| Package Version 	| CUDA Version 	| Python Version 	|
|:--------------	|:------------	|:-----------------:	|:--------------:	|:----------------:|
| tf_cuda9     	| Tensorflow 	| 12.0            	| 9.2          	| 3.6.8          	|
| tf_cuda10    	| Tensorflow 	| 13.0            	| 10.1         	| 3.7.3          	|
| torch_cuda9  	| Pytorch    	| 1.1             	| 9.2          	| 3.7.3          	|
| torch_cuda10 	| Pytorch    	| 1.1             	| 10.1         	| 3.6.8          	|

The environment files can be found in the `envs` folder. There are also two files to test successful installation in the `tests` folder.