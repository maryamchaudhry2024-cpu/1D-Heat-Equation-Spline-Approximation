
# 1D Heat Equation: Numerical Solution and Spline Approximation

## Project Overview
This project explores the numerical solution of the one-dimensional heat equation using the Explicit Forward-Time Central-Space (FTCS) finite difference method. Natural cubic spline interpolation is used to reconstruct and approximate the numerical solution.

The implementation is developed using Python.

## Mathematical Model
The one-dimensional heat equation is given by:

\[
\frac{\partial u}{\partial t}=\alpha\frac{\partial^2u}{\partial x^2}
\]

where:
- \(u(x,t)\) represents temperature.
- \(\alpha\) is the thermal diffusivity.
- \(x\) represents the spatial variable.
- \(t\) represents time.

## Numerical Method
The Explicit Forward-Time Central-Space (FTCS) scheme is used to approximate the heat equation numerically.

The spatial second derivative is approximated using central differences, while the time derivative is approximated using a forward difference.

## Spline Approximation
Natural cubic spline interpolation is used to reconstruct a smooth approximation of the numerical solution at selected spatial points.

## Tools
- Python
- Numerical finite difference methods
- Natural cubic spline interpolation

## Project Objectives
- Study the numerical solution of the one-dimensional heat equation.
- Implement the FTCS finite difference scheme.
- Explore natural cubic spline reconstruction.
- Examine numerical approximations and solution behavior.

## Project Status
This project is currently under development. Numerical implementation, visualization, and further analysis will be added progressively.

