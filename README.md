# OPTIMIZATION-MODEL

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : TADEPALLI R N V SAI RAMYA

*INTERN ID*: CTIS6700

*DOMAIN* : DATA SCIENCE

*DURATION* : 6 WEEKS

*MENTOR* : NEELA SANTHOSH

**Description**

In this task, the main goal was to build an optimization model using Linear Programming (LP) to maximize profit while working within certain limits. Optimization is an important concept in areas like operations research and data science, and it is widely used in industries such as manufacturing, logistics, finance, and supply chain management. The idea behind this task was to recreate a real-world situation where resources are limited and decisions need to be made in the most efficient way possible.

The problem focused on a company that produces two products: Product A and Product B. Each product generates a certain amount of profit, but at the same time, it requires resources such as labor and materials, which are limited. So, the challenge was to figure out how many units of each product should be produced in order to earn the highest profit without exceeding the available resources.

To solve this problem, the Python library PuLP was used. PuLP is a simple and beginner-friendly tool that helps in defining and solving linear optimization problems. It allows us to clearly set up variables, objectives, and constraints in a structured way.

The first step was to define decision variables, which represent the number of units of each product to be produced. These values cannot be negative, since it doesn’t make sense to produce a negative number of items. After that, the objective function was created to represent total profit. This was done by multiplying the number of units of each product by its profit value and adding them together.

Next, constraints were added to reflect real-world limitations. For example, the total production time required for both products could not exceed the available labor hours, and the total material used had to stay within the available supply. These constraints ensure that the solution is practical and realistic.

Once everything was defined, the model was solved using the built-in CBC solver. The solver checks all possible combinations within the given constraints and finds the one that gives the maximum profit. The final output showed the optimal number of units to produce for each product along with the maximum profit that can be achieved.

The results indicated that producing 40 units of Product A and 20 units of Product B gives the highest profit of 2200. This confirmed that the model was working correctly and successfully solving the problem.

One of the key takeaways from this task was learning how real-world problems can be converted into mathematical models and then solved using code. It also showed how important constraints are in decision-making. Without constraints, the model would produce unrealistic results, such as unlimited production.

Overall, this task provided valuable hands-on experience with optimization techniques and improved problem-solving skills. It also demonstrated how Python can be used not just for programming, but also for making smart, data-driven decisions. In conclusion, this task successfully showed how linear programming can be applied to optimize production and maximize profit in a practical and efficient way.

**Output**

<img width="525" height="115" alt="Image" src="https://github.com/user-attachments/assets/20140c23-4a28-49ca-8c75-f1258c129c14" />
