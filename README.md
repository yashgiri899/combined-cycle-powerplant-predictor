# Power Output Prediction using Deep Learning 🔥⚡

This project predicts the **power output** of a Combined Cycle Power Plant using deep learning techniques in TensorFlow/Keras. The dataset consists of 9,568 data points collected over 6 years, containing hourly average ambient variables and the corresponding power output.

---

## 📂 Dataset

The dataset used is **Folds5x2_pp.xlsx**, containing the following features:

- **AT**: Temperature (in °C)
- **V**: Exhaust Vacuum (in cm Hg)
- **AP**: Ambient Pressure (in millibar)
- **RH**: Relative Humidity (in %)
- **PE**: Power Output (in MW) — *target variable*

---

## 🧠 Model Architecture

The model is built using TensorFlow's Keras API with the following structure:

- Input Layer (256 units, ReLU, L2 regularization)
- Dropout Layer (0.2)
- Hidden Layer (128 units, ReLU, L2)
- Dropout Layer (0.2)
- Hidden Layer (64 units, ReLU, L2)
- Output Layer (1 unit, Linear activation)

> Optimizer: **Adam** with learning rate `0.0005`  
> Loss: **Mean Squared Error**  
> Regularization: **Dropout & L2**

---

## 📉 Performance Metrics

| Metric | Value |
|--------|-------|
| Mean Absolute Error (MAE) | ~3.42 |
| Mean Squared Error (MSE)  | ~18.66 |
| Root Mean Squared Error (RMSE) | ~4.32 |
| R² Score | **0.9362** ✅ |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yashgiri899/combined-cycle-powerplant-predictor.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the script
```bash
python code.py
```

> Make sure `dataset.xlsx` is in the same directory.

---

## 📦 Dependencies

See `requirements.txt` for full list of dependencies.

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Dataset source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant)

---

## ✨ Author

**[Yash Vardhan Giri](https://github.com/yashgiri899)**  
Feel free to ⭐ this repo if you found it helpful!
