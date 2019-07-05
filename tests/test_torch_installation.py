import torch

print ("Number of available CUDA Devices is: " + torch.cuda.device_count())
print ("Is CUDA available - "torch.cuda.is_available())