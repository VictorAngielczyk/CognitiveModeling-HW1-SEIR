import numpy as np


def simulate_seir(
    parameters: tuple[float, float, float] = (3, 0.5, 0.5),
    init_conditions: tuple[float, float, float, float] = (9999., 1., 0., 0.),
    days: int = 51,
) -> tuple[np.ndarray[np.float64], np.ndarray[np.float64], np.ndarray[np.float64], np.ndarray[np.float64]]:

    beta, sigma, gamma = parameters
    S0, E0, I0, R0 = init_conditions
    N = S0 + E0 + I0 + R0

    S = np.empty(days, dtype=np.float64)
    E = np.empty(days, dtype=np.float64)
    I = np.empty(days, dtype=np.float64)
    R = np.empty(days, dtype=np.float64)
    S[0], E[0], I[0], R[0] = S0, E0, I0, R0

    for t in range(1, days):
        E_new = (beta*S[t-1]*I[t-1]) / N
        I_new = sigma*E[t-1]
        R_new = gamma*I[t-1]

        S[t] = S[t-1] - E_new
        E[t] = E[t-1] + E_new - I_new
        I[t] = I[t-1] + I_new - R_new
        R[t] = R[t-1] + R_new

    return (S, E, I, R)
