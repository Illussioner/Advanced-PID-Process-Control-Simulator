# 🚀 Advanced PID Process Control Simulator

An interactive **PID (Proportional–Integral–Derivative) Process Control Simulator** developed using **Python**, **Streamlit**, and the **Python Control Systems Library**. The application enables users to analyze and compare PID controller performance across multiple industrial process models through dynamic simulation, visualization, and performance evaluation.

---

## 📌 Overview

This simulator demonstrates the dynamic behavior of industrial process control systems by allowing users to:

- Tune PID controller parameters in real time.
- Compare two different PID configurations.
- Simulate multiple first-order chemical engineering processes.
- Analyze system performance using standard control metrics.
- Study disturbance rejection and setpoint tracking.
- Download response plots for documentation and reporting.

Designed as a learning and analysis tool, the project combines **Chemical Engineering Process Control** concepts with **Python software development**.

---

## ✨ Features

- 🎛 Interactive tuning of **Kp, Ki, and Kd**
- ⚖ Compare **Current PID** vs **Comparison PID**
- 🏭 Multiple process models
  - Tank Level
  - Heat Exchanger
  - Flow Control
- 🎯 Adjustable setpoint tracking
- ⚠ Disturbance simulation with configurable magnitude
- 📈 Step response visualization
- 📊 Real-time performance dashboard
  - Rise Time
  - Settling Time
  - Overshoot
  - Peak Time
  - Steady-State Value
  - Controller Score
- 💡 Automatic PID tuning recommendations
- 📥 Download response plots as PNG
- 📋 Simulation summary

---

## 🛠 Technologies Used

- Python
- Streamlit
- Matplotlib
- NumPy
- Python Control Systems Library

---

## 📂 Project Structure

```text
Advanced-PID-Process-Control-Simulator/
│
├── app.py
├── README.md
├── requirements.txt
├── screenshots/
│   ├── dashboard.png
│   ├── comparison.png
│   └── disturbance.png
└── assets/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-PID-Process-Control-Simulator.git
```

Move into the project directory

```bash
cd Advanced-PID-Process-Control-Simulator
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### PID Comparison

![Comparison](screenshots/comparison.png)

### Disturbance Simulation

![Disturbance](screenshots/disturbance.png)

---

## 📖 Control Performance Metrics

The simulator evaluates controller performance using standard control engineering metrics:

- Rise Time
- Settling Time
- Overshoot
- Peak Time
- Steady-State Value
- Controller Score

These metrics help users compare different PID tuning strategies and evaluate overall controller effectiveness.

---

## 🎓 Learning Objectives

This project demonstrates practical implementation of:

- Transfer Functions
- PID Control
- Closed-Loop Feedback Systems
- Step Response Analysis
- Disturbance Rejection
- Setpoint Tracking
- Dynamic Process Modeling
- Interactive Scientific Visualization

---

## 🔮 Future Improvements

- Support for second-order process models
- Dead-time (FOPDT) systems
- Ziegler–Nichols auto-tuning
- PDF report generation
- Bode plots and Root Locus analysis
- Data logging and export

---

## 👨‍💻 Author

**Ishan Jain**

B.Tech Chemical Engineering  
Indian Institute of Technology (BHU), Varanasi

---

## 📄 License

This project is licensed under the MIT License.

# 🚀 Advanced PID Process Control Simulator

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
