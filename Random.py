import numpy as np

rng = np.random.default_rng()
print(rng.integers(1,31))

print(rng.integers(low=1, high=31))
print(rng.integers(low=1, high=31, size =(3,2)))

rng = np.random.default_rng(seed=12)
print(rng.integers(1,41))

print(np.random.uniform(low=-1,high=1,size=(3,2)))

Arr =np.array(["Vishnu","Ravi","Suresh","Ramesh"])
rng.shuffle(Arr)
print(Arr)

print(rng.choice(Arr))