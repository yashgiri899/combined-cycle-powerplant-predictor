# 📦 Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers
from tensorflow.keras.optimizers import Adam

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 📁 Load Dataset
dataset = pd.read_excel('dataset.xlsx')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# ⚙️ Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔀 Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=0)

# 🧠 Build Neural Network
model = Sequential([
    Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001), input_shape=(x_train.shape[1],)),
    Dropout(0.2),
    Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    Dropout(0.2),
    Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    Dense(1)  # Output layer (linear activation for regression)
])

# 🛠️ Compile Model
optimizer = Adam(learning_rate=0.0005)
model.compile(optimizer=optimizer, loss='mean_squared_error')

# ⏱️ Early Stopping
early_stop = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)

# 🚀 Train the Model
history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=500,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

# 🔮 Make Predictions
y_pred = model.predict(x_test)

# 📊 Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# 🧾 Display Results
print("\n📊 Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R² Score: {r2:.4f}")
