# -*- coding:utf-8 -*-
import sys, os

sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)


print(x_train.shape)
print(x_train[[1,2,3]])