def mm1(lambda_, mu):
    if lambda_ >= mu:
        return {'error': 'Sistema instável (λ >= μ)'}
    rho = lambda_ / mu
    P0 = 1 - rho
    L = lambda_ / (mu - lambda_)
    Lq = (lambda_**2) / (mu * (mu - lambda_))
    W = 1.0 / (mu - lambda_)
    Wq = lambda_ / (mu * (mu - lambda_))
    return {'Probabilidade do sistema vazio (P₀)': P0,
            'Taxa de ocupação (ρ)': rho, 
            'Número médio no sistema (L)': L,
            'Número médio na fila (Lq)': Lq,
            'Tempo médio no sistema (W)': W,
            'Tempo médio na fila (Wq)': Wq}
