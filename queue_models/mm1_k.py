import math

def mm1_k(lambda_, mu, K):
    if K < 1:
        return {'error': 'K deve ser >= 1'}
    rho = lambda_ / mu
    if abs(rho - 1.0) < 1e-12:
        P0 = 1.0 / (K + 1)
    else:
        P0 = (1 - rho) / (1 - rho**(K+1))
    Pn = [P0 * (rho**n) for n in range(0, K+1)]
    Pk = Pn[K]
    lambda_eff = lambda_ * (1 - Pk)
    if abs(rho - 1.0) < 1e-12:
        L = K / 2.0
    else:
        L = (rho / (1 - rho)) - ((K + 1) * rho**(K+1) / (1 - rho**(K+1)))
    Lq = L - (1 - P0)
    W = L / lambda_eff if lambda_eff > 0 else float('inf')
    Wq = Lq / lambda_eff if lambda_eff > 0 else float('inf')
    return {'Probabilidade de sistema vazio (P₀)': P0,
            'Taxa de ocupação (ρ)': rho,
            'Vetor de probabilidades de n clientes no sistema (Pₙ)': Pn,
            'Probabilidade de sistema cheio (Pₖ)': Pk,
            'Taxa efetiva de chegada (λₑ)': lambda_eff,
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
