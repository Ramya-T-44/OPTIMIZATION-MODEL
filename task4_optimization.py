from pulp import *

# Create model
model = LpProblem("Profit_Maximization", LpMaximize)

# Variables
x = LpVariable('Product_A', lowBound=0)
y = LpVariable('Product_B', lowBound=0)

# Objective
model += 40 * x + 30 * y

# Constraints
model += 2 * x + y <= 100
model += x + 2 * y <= 80

model.solve(PULP_CBC_CMD(msg=0))

# ✅ Clean Output
print("\n--- Final Decision ---")
print(f"Produce {int(x.value())} units of Product A")
print(f"Produce {int(y.value())} units of Product B")
print(f"Maximum Profit: ₹{int(value(model.objective))}")