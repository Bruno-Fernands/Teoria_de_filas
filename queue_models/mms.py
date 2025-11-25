import math

def mms(lambda_, mu, s):
    if s < 1:
        return {'error': 's deve ser >= 1'}
    rho = lambda_ / (s * mu)
    if rho >= 1:
        return {'error': 'Sistema instável: rho >= 1 (λ >= s*μ)'}
    sum_terms = sum((lambda_/mu)**n / math.factorial(n) for n in range(0, s))
    last = (lambda_/mu)**s / (math.factorial(s) * (1 - rho))
    P0 = 1.0 / (sum_terms + last)
    Lq = (P0 * (lambda_/mu)**s * rho) / (math.factorial(s) * (1 - rho)**2)
    L = Lq + lambda_/mu
    Wq = Lq / lambda_
    W = Wq + 1.0 / mu
    return {'Probabilidade do sistema vazio (P₀)': P0,
            'Taxa de ocupação (ρ)': rho,
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
