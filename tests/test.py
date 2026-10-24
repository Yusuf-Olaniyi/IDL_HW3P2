import numpy as np, os
d = 'hw3_data_subset/hw3p2_data/train-clean-100/text'
t = np.load(os.path.join(d, sorted(os.listdir(d))[0]), allow_pickle=True)
t = np.load(os.path.join(d, sorted(os.listdir(d))[0]), allow_pickle=True)
print(repr(''.join(t)))
print(type(t), t.shape, t.dtype)
print(repr(t[:5]) if t.ndim > 0 else repr(t))