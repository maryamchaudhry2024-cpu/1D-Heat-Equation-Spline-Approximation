
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Parameters
alpha = 0.01
L = 1.0
t_final = 1.84
r_target = 0.4

# Different spatial grid sizes
grid_sizes = [8, 16, 32, 64]

errors = []
grid_spacings = []

for Nx in grid_sizes:

    x = np.linspace(0, L, Nx)
    dx = x[1] - x[0]

    # Stable time step
    Nt = int(np.ceil(t_final / (r_target * dx**2 / alpha)))
    dt = t_final / Nt
    r = alpha * dt / dx**2

    # Initial condition
    u = np.sin(np.pi * x)

    # FTCS method
    for _ in range(Nt):
        u_new = u.copy()
        u_new[1:-1] = (
            u[1:-1] + r * (
                u[2:] - 2*u[1:-1] + u[:-2]
            )
        )
        u_new[0] = 0
        u_new[-1] = 0
        u = u_new

    # Natural cubic spline
    spline = CubicSpline(x, u, bc_type="natural")

    # Dense grid for error calculation
    x_dense = np.linspace(0, L, 1000)
    u_spline = spline(x_dense)

    # Exact analytical solution
    u_exact = np.sin(np.pi*x_dense) * np.exp(
        -alpha * np.pi**2 * t_final
    )

    # Maximum absolute error
    error = np.max(np.abs(u_spline - u_exact))

    errors.append(error)
    grid_spacings.append(dx)

    print(
        f"Nx = {Nx:2d}, "
        f"dx = {dx:.6f}, "
        f"Maximum Error = {error:.8e}"
    )

# Estimate observed convergence rate
rate = np.polyfit(
    np.log(grid_spacings),
    np.log(errors),
    1
)[0]

print(f"\nObserved convergence rate: {rate:.4f}")

# Convergence plot
plt.figure(figsize=(8, 5))
plt.loglog(
    grid_spacings,
    errors,
    "o-",
    label="Maximum Absolute Error"
)

plt.xlabel("Spatial Grid Spacing (dx)")
plt.ylabel("Maximum Absolute Error")
plt.title("Convergence Analysis of FTCS and Cubic Spline")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig("convergence_plot.png", dpi=300)
plt.show()
