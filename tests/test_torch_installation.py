import torch

print ("Number of available CUDA Devices is: " + str(torch.cuda.device_count()))
print ("Is CUDA available: " + str(torch.cuda.is_available()))
