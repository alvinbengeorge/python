import torch

x = torch.rand(1000, 1000, requires_grad=True)
y = torch.rand_like(x)

z = torch.matmul(x, y)/1000
print(z)