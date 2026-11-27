import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Parameters
alpha = 0.01
L = 1.0
Nx = 15
t_final = 1.84

# Spatial grid
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

# Stable time step for FTCS
r = 0.4
dt = r * dx**2 / alpha
Nt = int(np.ceil(t_final / dt))
dt = t_final / Nt
r = alpha * dt / dx**2

# Initial condition
u = np.sin(np.pi * x)

# FTCS numerical solution
for _ in range(Nt):
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + r * (
        u[2:] - 2 * u[1:-1] + u[:-2]
    )
    u_new[0] = 0.0
    u_new[-1] = 0.0
    u = u_new

# Analytical solution
x_dense = np.linspace(0, L, 500)
u_exact = np.sin(np.pi * x_dense) * np.exp(
    -alpha * np.pi**2 * t_final
)

# Natural cubic spline reconstruction
spline = CubicSpline(x, u, bc_type="natural")
u_spline = spline(x_dense)

# Absolute error
error = np.abs(u_spline - u_exact)

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_dense, u_exact, "b-", label="Exact Analytical Solution")
plt.plot(x, u, "ro", label="FTCS Coarse Nodes (Nx=15)")
plt.plot(x_dense, u_spline, "g--", label="Cubic Spline Reconstruction")
plt.xlabel("Position (x)")
plt.ylabel("Temperature u(x, t)")
plt.title(f"1D Heat Equation & Spline Approximation (t={t_final:.2f}s)")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_dense, error, "m-", label="|Cubic Spline - Exact|")
plt.xlabel("Position (x)")
plt.ylabel("Absolute Error")
plt.title("Pointwise Cubic Spline Approximation Error")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("heat_equation_spline.png", dpi=300)
plt.show()
