import math

def mms_k(lambda_, mu, s, K):
    sum1 = 0.0
    for n in range(0, s):
        sum1 += (lambda_/mu)**n / math.factorial(n)
    sum2 = 0.0
    for n in range(s, K+1):
        sum2 += (lambda_/mu)**s / math.factorial(s) * (lambda_/(s*mu))**(n-s)
    P0 = 1.0 / (sum1 + sum2)
    Pn = []
    for n in range(0, K+1):
        if n < s:
            pn = P0 * (lambda_/mu)**n / math.factorial(n)
        else:
            pn = P0 * (lambda_/mu)**s / math.factorial(s) * (lambda_/(s*mu))**(n-s)
        Pn.append(pn)
    Pk = Pn[-1]
    lambda_eff = lambda_ * (1 - Pk)
    L = sum(n * Pn[n] for n in range(0, K+1))
    Lq = L - lambda_eff/mu
    W = L / lambda_eff if lambda_eff>0 else float('inf')
    Wq = Lq / lambda_eff if lambda_eff>0 else float('inf')
    rho = lambda_/(s*mu)
    return {'Probabilidade de sistema vazio (P₀)': P0,
            'Taxa de ocupação (ρ)': rho,
            'Probabilidade de n clientes no sistema (Pₙ)': Pn,
            'Probabilidade de bloqueio (Pₖ)': Pk,
            'Taxa efetiva de chegada (λₑ)': lambda_eff,
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
