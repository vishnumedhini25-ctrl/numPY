# Handling Missing Values in Data
import numpy as np

a = np.array([10, 20, np.nan, 40, 50])

print(a)
print(np.isnan(a))
print(np.mean(a))

# counting missing values
b=np.array([10,20,np.nan,40,np.nan,np.nan])
print("Sum:",np.sum(np.isnan(b)))
print("Mean:",np.nanmean(b))
print("Standard Deviation:",np.nanstd(b))
print("Minimum:",np.nanmin(b))
print("Maximum:",np.nanmax(b))

# positive and negative infinity
c=np.array([10,np.inf,30,40])
print(c)
print("Infinity:",np.isinf(c))
c=np.array([10,-np.inf,30,40])
print(c)

c=np.array([10,np.inf,30,40,np.nan,-np.inf])
print("Finite:",np.isfinite(c))
