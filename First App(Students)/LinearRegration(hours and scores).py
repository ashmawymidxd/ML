# Aim: To learn the linear regression algorithm
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Importing the dataset
file_path = '/dataset.csv'
data = pd.read_csv(file_path)

x = data["Hours"].values
y = data["Scores"].values

# Splitting the dataset into the Training set and Test set
plt.figure(figsize=(8,6))
plt.title('Correlation Matrix')
plt.scatter(x,y)
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

# apply the linner regration to train the model
L_rate = 0.001
iterations = 100

theta_1 = 0
theta_0 = 0

n = x.shape[0]
losses = []

for i in range(iterations):
  h_x = theta_0 + theta_1*x
  mse = (1/n)*np.sum((h_x-y)**2)

  losses.append(mse)

  d_theta0 = (2/n) * np.sum(h_x-y)
  d_theta1 = (2/n) * np.sum(x * (h_x-y))

  theta_1 = theta_1 - L_rate * d_theta1
  theta_0 = theta_0 - L_rate * d_theta0


print("theta_0 = ",round(theta_0,2))
print("theta_1 = ",round(theta_1,2))
print("MSE = ",mse)

#try the model
new_x = 3
prediction_model = theta_0+theta_1*new_x
print("predicted Scores = ",round(prediction_model,2))

#calculate the accurcy for this model
accurcy = 1 - (losses[-1]/losses[0])
print("accurcy = ",(round(accurcy,2)*100))

# Plotting the losses
plt.title("losses values")
plt.plot(losses)
plt.ylabel("losses")
plt.xlabel("iterations")

print("inetial losses \t = ",losses[0])
print("final losses \t = ",losses[-1])