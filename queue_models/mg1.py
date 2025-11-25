def mg1(lambda_, mu, sigma2):
    rho = lambda_ / mu
    if rho >= 1:
        return {'error': 'Sistema instável (ρ >= 1)'}
    Lq = (lambda_**2 * sigma2 + rho**2) / (2 * (1 - rho))
    L = rho + Lq
    Wq = Lq / lambda_
    W = Wq + 1.0 / mu
    P0 = 1 - rho
    return {'Probabilidade de sistema vazio (P₀)': P0,
            'Taxa de ocupação (ρ)': rho,
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
