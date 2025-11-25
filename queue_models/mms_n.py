import math

def mms_n(lambda_, mu, s, N):
    terms = []
    for n in range(0, N+1):
        if n <= s:
            val = math.factorial(N) / math.factorial(N-n) * (lambda_/mu)**n / math.factorial(n)
        else:
            val = math.factorial(N) / math.factorial(N-n) * (lambda_/mu)**n / (math.factorial(s) * s**(n-s))
        terms.append(val)
    S = sum(terms)
    P0 = 1.0 / S
    Pn = [P0 * terms[n] for n in range(0, N+1)]
    L = sum(n*Pn[n] for n in range(0, N+1))
    lambda_eff = lambda_ * (N - L)
    Lq = L - lambda_eff/mu
    W = L / lambda_eff if lambda_eff>0 else float('inf')
    Wq = Lq / lambda_eff if lambda_eff>0 else float('inf')
    return {'Probabilidade de sistema vazio (P₀)': P0,
            'Probabilidade de n clientes no sistema (Pₙ)': Pn,
            'Taxa efetiva de chegada (λₑ)': lambda_eff,
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
