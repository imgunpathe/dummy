import pandas as pd
import numpy as np

np.random.seed(42)

# 1 day of data (24 hours, every 10 minutes)
timestamps = pd.date_range(
    start="2024-01-01 00:00:00",
    periods=144,          # 24 hrs × 6 cycles/hr
    freq="10min"
)

machine_status = np.random.choice(
    ["RUN", "STOP"],
    size=144,
    p=[0.9, 0.1]           # 90% running, 10% stopped
)

loss_reasons = [
    "No Loss",
    "Material Issue",
    "Mechanical Issue",
    "Operator Delay",
    "Power Fluctuation"
]

rows = []

for ts, status in zip(timestamps, machine_status):
    if status == "RUN":
        cycle_time = np.random.normal(10, 1)  # around 10 min
        tyre = 1 if cycle_time <= 12 else 0   # slow cycle → loss
        reason = "No Loss" if tyre == 1 else "Performance Loss"
    else:
        cycle_time = 0
        tyre = 0
        reason = np.random.choice(loss_reasons[1:])

    rows.append([
        ts,
        status,
        tyre,
        round(cycle_time, 2),
        10,
        reason
    ])

df = pd.DataFrame(rows, columns=[
    "timestamp",
    "machine_status",
    "tyre_produced",
    "cycle_time_min",
    "ideal_cycle_time_min",
    "loss_reason"
])

df.to_csv("tyre_production_data.csv", index=False)

print("Tyre production dataset generated successfully")
