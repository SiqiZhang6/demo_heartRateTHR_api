# ❤️ Heart Rate Health Predictor API

Designed for demo purposes that predicts health status based on heart rate input. Simple if-else logic.

## 🏗️ Project Architecture
* **Communication:** JSON via HTTP POST requests

---

## Model Logic
To keep the demo simple and transparent, the backend applies the following logic:

| Heart Rate (BPM) | Status | Recommendation |
| :--- | :--- | :--- |
| **Above 100** | High | Please rest and hydrate. |
| **60 - 100** | Normal | Your heart rate is within a healthy range. |
| **Below 60** | Low | Monitor for dizziness or fatigue. |

---

## Getting Started
Navigate to your root directory and ensure you have Python installed.

```bash
# Install dependencies
pip install flask flask-cors

# Run the backend
python app.py