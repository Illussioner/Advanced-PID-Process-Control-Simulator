import streamlit as st
import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import io
from datetime import datetime

st.title("PID Process Control Simulator")

# Plant Transfer Function/ Process Selection
process = st.sidebar.selectbox(
    "Process Type",
    ["Tank Level", "Heat Exchanger", "Flow Control"]
)

if process == "Tank Level":
    plant = ctrl.TransferFunction([1], [10, 1])

elif process == "Heat Exchanger":
    plant = ctrl.TransferFunction([2], [8, 1])

else:
    plant = ctrl.TransferFunction([3], [2, 1])

# setpoint 

st.sidebar.header("Setpoint")

setpoint = st.sidebar.slider(
    "Desired Setpoint",
    0.5,
    2.0,
    1.0,
    0.1
)

st.sidebar.header("PID Parameters")

kp = st.sidebar.slider("Kp", 0.0, 20.0, 2.0)
ki = st.sidebar.slider("Ki", 0.0, 20.0, 1.0)
kd = st.sidebar.slider("Kd", 0.0, 10.0, 0.5)

st.sidebar.header("Comparison PID")

kp_old = st.sidebar.number_input("Old Kp", value=1.0)
ki_old = st.sidebar.number_input("Old Ki", value=0.5)
kd_old = st.sidebar.number_input("Old Kd", value=0.2)

st.sidebar.header("Disturbance")

enable_disturbance = st.sidebar.checkbox(
    "Enable Disturbance",
    value=False
)
disturbance = st.sidebar.slider(
    "Disturbance Magnitude",
    0.0,
    0.5,
    0.2,
    0.05,
    disabled=not enable_disturbance
)
# PID Controller
controller = ctrl.TransferFunction([kd, kp, ki], [1, 0])

controller_old = ctrl.TransferFunction(
    [kd_old, kp_old, ki_old],
    [1, 0]
)

# Closed Loop System
closed_loop = ctrl.feedback(controller * plant)

closed_loop_old = ctrl.feedback(controller_old * plant)

# Step Response
t, y = ctrl.step_response(closed_loop)
t_old, y_old = ctrl.step_response(closed_loop_old)

# Scale responses according to setpoint
y *= setpoint
y_old *= setpoint

import numpy as np

if enable_disturbance:

    disturbance_signal = np.zeros_like(t)

    disturbance_signal[t >= 5] = disturbance

    y = y + disturbance_signal

# Plot
fig, ax = plt.subplots()
ax.plot(t, y, label="Current PID")
ax.plot(t_old, y_old, label="Comparison PID")
ax.legend()
ax.set_title(f"{process} - PID Response Comparison")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Output")
ax.grid(True)

ax.axhline(
    y=setpoint,
    color="green",
    linestyle=":",
    linewidth=2,
    label="Target Setpoint"
)

st.pyplot(fig)


download_choice = st.selectbox(
    "Download Option",
    [
        "Comparison Plot",
        "Current PID Only"
    ]
)

if download_choice == "Current PID Only":

    fig_download, ax_download = plt.subplots()

    ax_download.plot(t, y, label="Current PID")

    ax_download.legend()
    ax_download.grid(True)

else:

    fig_download = fig

buf = io.BytesIO()

fig_download.savefig(
    buf,
    format="png",
    bbox_inches="tight"
)

buf.seek(0)

st.download_button(
label="📥 Download Response Plot",
data=buf.getvalue(),
file_name="pid_response.png",
mime="image/png"
)

if enable_disturbance:
    st.warning(
        f"A disturbance of magnitude {disturbance:.2f} was introduced at t = 5 s."
    )
# Metrics
info = ctrl.step_info(closed_loop)
info_old = ctrl.step_info(closed_loop_old)
score = 10

if info["Overshoot"] > 20:
    score -= 2

if info["SettlingTime"] > 15:
    score -= 2

if info["RiseTime"] > 5:
    score -= 1

st.subheader("Performance Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
    "Rise Time",
    f"{info['RiseTime']:.2f} s",
    delta=f"{info_old['RiseTime'] - info['RiseTime']:.2f} s"
)

with col2:
    st.metric(
    "Settling Time",
    f"{info['SettlingTime']:.2f} s",
    delta=f"{info_old['SettlingTime'] - info['SettlingTime']:.2f} s"
)

col3, col4 = st.columns(2)

with col3:
    st.metric(
    "Overshoot",
    f"{info['Overshoot']:.2f} %",
    delta=f"{info_old['Overshoot'] - info['Overshoot']:.2f} %"
)

with col4:
    st.metric(
    "Peak Time",
    f"{info['PeakTime']:.2f} s",
    delta=f"{info_old['PeakTime'] - info['PeakTime']:.2f} s"
)

col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Steady State Value",
        f"{info['SteadyStateValue']:.3f}",
    )

with col6:
    st.metric(
        "Current Process",
        process
    )

#Recommendations
st.subheader("PID Tuning Recommendations")

if info["Overshoot"] > 20:
    st.warning(
        f"The controller overshoots the desired setpoint of {setpoint:.1f}. Consider reducing Kp or increasing Kd."
    )

if info["SettlingTime"] > 15:
    st.warning(
        "Settling time is large. Consider increasing Kp."
    )

if info["RiseTime"] > 5:
    st.info(
        "Response is slow. Increasing Kp may improve response speed."
    )

if info["Overshoot"] < 5 and info["SettlingTime"] < 10:
    st.success(
        "Controller performance looks good."
    )

# Simulation Summary
st.subheader("Simulation Summary")

summary = f"""
### Process Information

**Process:** {process}

**Target Setpoint:** {setpoint:.1f}

**Current PID**
- Kp = {kp:.2f}
- Ki = {ki:.2f}
- Kd = {kd:.2f}

**Comparison PID**
- Kp = {kp_old:.2f}
- Ki = {ki_old:.2f}
- Kd = {kd_old:.2f}

**Disturbance:** {"Enabled" if enable_disturbance else "Disabled"}
"""

st.success(summary)

# rating/score of PID controller
if score >= 9:
    rating = "Excellent"
elif score >= 7:
    rating = "Good"
elif score >= 5:
    rating = "Fair"
else:
    rating = "Needs Tuning"
st.metric("Controller Score", f"{score}/10",delta=rating)
#verdict
if info["SettlingTime"] < info_old["SettlingTime"]:

    st.success(
        "Current PID demonstrates better overall control performance."
    )

else:

    st.info(
        "Comparison PID provides better dynamic performance."
    )

st.caption(
    f"Simulation generated on {datetime.now().strftime('%d %b %Y %H:%M')}"
)