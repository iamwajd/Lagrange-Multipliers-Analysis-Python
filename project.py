import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, Bounds, LinearConstraint

# Objective Function (Minimize C(x, y) = 3x^2 + 4y^2)
def objective_function(X):
    x, y = X
    return 3 * x**2 + 4 * y**2

# Constraint: x + y = 80
# A = [1, 1] , b = 80
linear_constraint = LinearConstraint([1, 1], [80], [80])

# Non-Negativity Bounds: x >= 0, y >= 0
bounds = Bounds([0, 0], [np.inf, np.inf])

initial_guess = [40, 40]

# Run the optimization algorithm
result = minimize(
    objective_function,  
    initial_guess,       
    method='SLSQP',      
    bounds=bounds,       
    constraints=linear_constraint 
)

# results
x_optimal, y_optimal = result.x
cost_optimal = result.fun 


print("             Optimization Results")

print(f"Success Status: {result.success}")
print(f"Optimal X (x*): {x_optimal:.4f}")
print(f"Optimal Y (y*): {y_optimal:.4f}")
print(f"Minimum Cost (C*): {cost_optimal:.4f}")



# Visualization (Contour Plot)

x_vals = np.linspace(0, 80, 100)
y_vals = np.linspace(0, 80, 100) 
X, Y = np.meshgrid(x_vals, y_vals)
C = 3 * X**2 + 4 * Y**2 


plt.figure(figsize=(10, 7))


levels_to_plot = [5000, 10000, 15000, 19542.86, 25000]
contour = plt.contour(X, Y, C, levels=levels_to_plot, cmap='coolwarm')
plt.clabel(contour, inline=True, fontsize=10, fmt='%1.0f')
plt.colorbar(label='Total Cost C(x,y)')

y_constraint = 80 - x_vals
plt.plot(x_vals, y_constraint, 'g--', linewidth=2, label='Production Constraint: x + y = 80')


plt.plot(x_optimal, y_optimal, 'ko', markersize=8, label='Optimal Point $(x^*, y^*)$')
plt.annotate(
    f'Optimal:\n({x_optimal:.2f}, {y_optimal:.2f})', 
    (x_optimal, y_optimal), 
    textcoords="offset points", 
    xytext=(10, -10), 
    ha='left', 
    fontsize=12, 
    color='black'
)


plt.title('Cost Minimization using Lagrange (Contour Plot)')
plt.xlabel('Product X Quantity')
plt.ylabel('Product Y Quantity')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()