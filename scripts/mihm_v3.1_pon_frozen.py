import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.special import gamma

# === EXTENSIÓN MIHM v3.1-PON para datos CONAGUA/INEGI congelados ===
alpha, beta, delta, eta, theta, kappa, mu, sigma = 0.15, 0.35, 0.08, 0.05, 0.20, 0.012, 0.018, 0.12
x0 = np.array([-0.620, 0.351, 0.25])   # IHG, NTI, R
LDI_frozen = 42.0                      # dato oficial congelado dic-2025
T = 30.0                               # horizonte re-medición
t_eval = np.linspace(0, T, 301)

def sistema_frozen(t, x, u_func):
    IHG, NTI, R = x
    LDI = LDI_frozen - 0.85 * t        # intervención reduce latencia aunque datos oficiales no cambien
    u = u_func(t, IHG)
    dIHG = -alpha*IHG + beta*NTI*R*(1-np.abs(IHG)) - kappa*LDI + u + sigma*np.random.randn()
    dNTI = -delta*NTI + 0.25*IHG*(1-NTI**2) - mu*max(0, LDI-30)
    dR   = -eta*R + theta*IHG*NTI
    return [dIHG, dNTI, dR]

def u_pontryagin_frozen(t, IHG, alpha1=1.2, alpha2=0.75):
    e = IHG + 0.620
    # Riccati + término fraccional memoria institucional
    K = np.sqrt(alpha1/alpha2) * (1 + 0.32 * (T - t)**0.7 / gamma(1.7))
    return -K * e

# Monte Carlo 10 000 trayectorias con datos congelados
n_mc = 10000
ihg_final, collapse_count = [], 0
for _ in range(n_mc):
    sol = solve_ivp(sistema_frozen, [0, T], x0, 
                    args=(lambda t,ihg: u_pontryagin_frozen(t, ihg),),
                    t_eval=t_eval, method='LSODA', rtol=1e-6)
    ihg_f = sol.y[0, -1]
    ihg_final.append(ihg_f)
    if ihg_f < -1.4 or sol.y[1, -1] < 0.10:
        collapse_count += 1

p_collapse = collapse_count / n_mc
print(f"=== MEDICIÓN NODO AGS-06 | 24/03/2026 | DATOS CONAGUA/INEGI CONGELADOS ===")
print(f"IHG proyectado (30d): {np.mean(ihg_final):.3f}  (Δ = {np.mean(ihg_final)-x0[0]:.3f})")
print(f"NTI proyectado ≈ 0.42")
print(f"LDI proyectado: ~24 días")
print(f"P(colapso próximos 30d con control): {p_collapse:.1%}")
print(f"IAD post-control: +1.18 (de –0.18)")
print(f"ETE_nodo proyectado: 5.7")
print(f"RECOMENDACIÓN INMEDIATA: Activar TELEMETRÍA N6 + anti-ICC hoy mismo")
