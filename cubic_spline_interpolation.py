import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Example: 6 hours of 15-minute average flows (veh/min), 24 data points in total 
q_15 = np.array([9, 11, 12, 14, 18, 26, 35, 44, 55, 65, 62, 57, 56, 54, 52, 46, 46, 46, 48, 44, 43, 43, 44, 41])

dt_15 = 15  # minutes

# 1. Convert averages to vehicle counts
counts_15 = q_15 * dt_15

# 2. Cumulative vehicle count
cum_counts = np.concatenate([[0], np.cumsum(counts_15)])

# Time axes
t_15 = np.arange(len(cum_counts)) * dt_15          # 15-min boundaries
t_1 = np.arange(0, t_15[-1] + 2, 1)                 # 1-min resolution

# 3. Interpolation of cumulative vehicle count
cs = CubicSpline(t_15, cum_counts) # Cubic spline interpolation
q_1_cum = cs(t_1)

# 4. Differentiating against interpolated cumulative vehicle counts to obtain per-minute flows
q_1 = np.diff(q_1_cum)

# 4. Calculate difference between 15-minute average of interpolated data and original data 
diff_mean = np.array([None]*len(q_15))
for i in range(len(q_15)):
    diff_mean[i] = 100-np.average(q_1[i*15:(i+1)*15])/q_15[i]*100
print(np.average(np.abs(diff_mean))) # Calculating and displaying MAPE, should be 0 or very close to 0

# --- Plot ---
plt.figure(figsize=(10, 6))
plt.plot(q_1, label="1-min flow (conserved)", linewidth=2)
plt.step(np.arange(len(q_15)+1) * dt_15, np.concatenate([q_15, [q_15[-1]]]), where="post", label="15-min averages", linewidth=2)
plt.legend()
plt.xlabel("Time (minutes)")
plt.ylabel("Flow (veh/min)")
plt.xticks(np.arange(0, len(q_15) * dt_15 + 1, dt_15))
plt.xlim([0, len(q_15) * dt_15])
plt.grid()
plt.tight_layout()
plt.show()
