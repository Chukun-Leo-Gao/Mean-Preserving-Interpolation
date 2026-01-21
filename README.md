# Mean-preserving time-series interpolation via cumulative-mean cubic splines

This project implements a mean-preserving interpolation method for time-series data based on cubic spline interpolation of cumulative means using scipy.interpolate.CubicSpline. By performing interpolation in cumulative space and differentiating back to the original scale, the method produces higher-resolution series (e.g. 1-minute traffic flows from 15-minute averages) while exactly conserving the original interval averages.

Packages needed: numpy, scipy, matplotlib (optional, for plotting).
```
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
```

Suppose we have 6 hours of 15-minute average traffic flows.
```
q_15 = np.array([9, 11, 12, 14, 18, 26, 35, 44, 55, 65, 62, 57, 56, 54, 52, 46, 46, 46, 48, 44, 43, 43, 44, 41])
dt_15 = 15
```

First, convert averages to vehicle counts. 
```
counts_15 = q_15 * dt_15
```

Then, calculate the cumulative vehicle counts.
```
cum_counts = np.concatenate([[0], np.cumsum(counts_15)])
```

Create time axis for interpolation.
```
t_15 = np.arange(len(cum_counts)) * dt_15
t_1 = np.arange(0, t_15[-1] + 2, 1)      
```

Interpolation of cumulative vehicle count
```
cs = CubicSpline(t_15, cum_counts)
q_1_cum = cs(t_1)
```

Differentiating against interpolated cumulative vehicle counts to obtain per-minute flows
```
q_1 = np.diff(q_1_cum)
```

To verify the mean-preserving property, difference between 15-minute average of interpolated data and original data is calculated.
```
diff_mean = np.array([None]*len(q_15))
for i in range(len(q_15)):
    diff_mean[i] = 100-np.average(q_1[i*15:(i+1)*15])/q_15[i]*100
print(np.average(np.abs(diff_mean))) # Calculating and displaying MAPE, should be 0 or very close to 0
```

![Interpolation Result](https://github.com/Chukun-Leo-Gao/Average-Preserving-Interpolation/blob/main/Figure_1.png "Interpolation Result")
