
# 1D Heat Equation: Numerical Solution and Spline Approximation

## 1. Project Overview
This project investigates the numerical solution of the one-dimensional heat equation using the Explicit Forward-Time Central-Space (FTCS) finite difference method and natural cubic spline interpolation.

The implementation is developed in Python.

## 2. Mathematical Model

The one-dimensional heat equation is:

du/dt = alpha * d²u/dx²

where alpha represents thermal diffusivity.

The computational domain is 0 <= x <= 1, with the initial condition:

u(x,0) = sin(pi*x)

and homogeneous Dirichlet boundary conditions:

u(0,t) = u(1,t) = 0

## 3. Numerical Method

The FTCS finite difference scheme is used to approximate the solution.

The numerical solution is reconstructed using natural cubic spline interpolation.

The stability parameter is:

r = alpha * dt / dx²

The explicit FTCS scheme requires r <= 1/2.

## 4. Analytical Solution

For the selected initial and boundary conditions, the analytical solution is:

u(x,t) = exp(-alpha*pi²*t) * sin(pi*x)

This solution is used as a reference for comparison.

## 5. Implementation

The project uses:
- Python
- NumPy
- SciPy
- Matplotlib

Install the dependencies:

pip install -r requirements.txt

Run the program:

python heat_equation_spline.py

## 6. Results

The numerical solution is compared with the analytical solution.

The project includes:
- FTCS coarse-grid numerical values.
- 
## 10. Convergence Analysis

A convergence study was performed using four different spatial grid sizes: 8, 16, 32, and 64 nodes.

The maximum absolute error was calculated by comparing the natural cubic spline reconstruction with the analytical solution.

### Numerical Results

| Grid Size (Nx) | Grid Spacing (dx) | Maximum Absolute Error |
|---|---|---|
| 8 | 0.142857 | 2.18103001e-03 |
| 16 | 0.066667 | 7.05913489e-04 |
| 32 | 0.032258 | 1.76522390e-04 |
| 64 | 0.015873 | 4.37934021e-05 |

### Observed Convergence Rate

The experimentally observed convergence rate was:

**p = 1.7897**

The results demonstrate that the maximum absolute error decreases as the spatial grid is refined.

The observed convergence rate is close to second order, indicating approximately second-order convergence over the tested grids.

### Conclusion

The numerical experiment demonstrates the effectiveness of combining the FTCS finite difference method with natural cubic spline reconstruction for approximating the one-dimensional heat equation.

Further investigation may examine the individual contributions of finite difference discretization and spline interpolation to the overall approximation error.

- Natural cubic spline reconstruction.
- Analytical solution.
- Pointwise absolute error plot.

## 7. Project Objectives

- Study numerical solutions of partial differential equations.
- Implement explicit finite difference methods.
- Explore natural cubic spline interpolation.
- Compare numerical approximations with analytical solutions.
- Investigate approximation accuracy.

## 8. Repository Files

- heat_equation_spline.py: Python implementation.
- requirements.txt: Required Python libraries.
- heat_equation_spline.png: Visualization of numerical results.
- README.md: Project documentation.

## 9. Project Status

The initial numerical implementation and visualization are complete. Further investigation of convergence, stability, and numerical error is a potential extension.


