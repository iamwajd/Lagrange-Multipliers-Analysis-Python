# Constrained Cost Minimization: A Python-Based Lagrange Analysis 📐

This project applies the **Lagrange Multipliers** method to solve a nonlinear optimization problem, specifically minimizing a quadratic cost function under a single linear resource constraint.

## 📝 Project Overview
[cite_start]The objective is to determine the most cost-effective production allocation between two products while meeting a mandatory production quota[cite: 309, 312]. [cite_start]This project bridges the gap between theoretical calculus and numerical computation[cite: 314].

### 🎯 Optimization Problem
* [cite_start]**Objective Function:** Minimize $C(x, y) = 3x^2 + 4y^2$[cite: 326, 348].
* [cite_start]**Constraint:** $x + y = 80$ (with $x, y \geq 0$)[cite: 330, 349, 350].
* **Analytical Approach:** Constructing and solving the Lagrangian function:  
    [cite_start]$L(x, y, \lambda) = 3x^2 + 4y^2 + \lambda(80 - x - y)$[cite: 335, 353].

## 💻 Python Implementation
[cite_start]The solution is implemented in **Python**, leveraging its scientific library stack for high-precision numerical results and visualization[cite: 449].

* [cite_start]**Optimization Algorithm:** Utilized `scipy.optimize.minimize` with the **SLSQP** (Sequential Least Squares Programming) method[cite: 397, 450].
* [cite_start]**Numerical Verification:** The Python script successfully matched the analytical solution[cite: 456, 462, 506].
* [cite_start]**Visualization:** Generated contour plots using **Matplotlib** to show the elliptical cost contours and the linear production constraint[cite: 421, 467, 498].



## 📊 Key Results
| Metric | Analytical Value | Python Output |
| :--- | :--- | :--- |
| **Optimal X ($x^*$)** | [cite_start]45.7143 [cite: 370] | [cite_start]45.7143 [cite: 455] |
| **Optimal Y ($y^*$)** | [cite_start]34.2857 [cite: 371] | [cite_start]34.2857 [cite: 456] |
| **Min. Cost ($C^*$)** | [cite_start]10,971.43 [cite: 375] | [cite_start]10,971.4286 [cite: 457] |

## 📁 Repository Structure
* [cite_start]`project.py`: The Python source code for optimization and plotting[cite: 395].
* [cite_start]`cs 348.pdf`: Full technical report detailing the mathematical proofs[cite: 291].

## 👥 Prepared By
* [cite_start]**Shaden Alkhalifah** (Introduction, Analysis, Visualization)[cite: 537].
* [cite_start]**Wajd Alharbi** (Mathematical Formulation, Lagrange Method, Numerical Analysis)[cite: 537].
* [cite_start]**Taif Alharbi** (Implementation, Conclusion, Results & Discussion)[cite: 537].

[cite_start]*Supervised by: T. Ghadi Alrasheed* [cite: 290]
