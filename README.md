# Mean-preserving time-series interpolation via cumulative-mean cubic splines

This project implements a mean-preserving interpolation method for time-series data based on cubic spline interpolation of cumulative means using scipy.interpolate.CubicSpline. By performing interpolation in cumulative space and differentiating back to the original scale, the method produces higher-resolution series (e.g. 1-minute traffic flows from 15-minute averages) while exactly conserving the original interval averages.

Suppose we have 6 hours of 15-minute average traffic flows.

```
q_15 = np.array([9, 11, 12, 14, 18, 26, 35, 44, 55, 65, 62, 57, 56, 54, 52, 46, 46, 46, 48, 44, 43, 43, 44, 41])
dt_15 = 15
```

![Interpolation Result](https://github.com/Chukun-Leo-Gao/Average-Preserving-Interpolation/blob/main/Figure_1.png "Interpolation Result")
