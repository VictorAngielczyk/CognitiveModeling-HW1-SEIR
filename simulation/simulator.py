import numpy as np
from typing import Tuple

def simulate_seir(
    parameters: Tuple[np.float64, np.float64, np.float64] = (3.0, 0.5, 0.5),
    init_conditions: Tuple[np.float64, np.float64, np.float64, np.float64] = (9999.0, 1.0, 0.0, 0.0),
    days: int = 51,
)-> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """TODO"""

    # Extract parameters and initial conditions (Your code here)
    beta, sigma, gamma = parameters
    S0, E0, I0, R0 = init_conditions
    N = S0 + E0 + I0 + R0

    # Use NumPy arrays instead of Python lists
    S = np.empty(days, dtype=float)
    E = np.empty(days, dtype=float)
    I = np.empty(days, dtype=float)
    R = np.empty(days, dtype=float)
    S[0], E[0], I[0], R[0] = S0, E0, I0, R0
    
    # For each day, perform SEIR update
    for t in range(1, days):

        # Compute new cases and update equations
        E_new = (beta*S[t-1]*I[t-1]) / N
        I_new = sigma*E[t-1]
        R_new = gamma*I[t-1]
      
        # Update equations
        S[t] = S[t-1] - E_new
        E[t] = E[t-1] + E_new - I_new
        I[t] = I[t-1] + I_new - R_new
        R[t] = R[t-1] + R_new

    return (S, E, I, R)
