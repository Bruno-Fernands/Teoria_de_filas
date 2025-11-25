def priorities_preemptive(mu, lambdas):
    out = {}
    cumulative = 0.0
    for i, lam in enumerate(lambdas, start=1):
        cumulative += lam
        rho_cum = cumulative / mu
        if rho_cum >= 1.0:
            out[f'class_{i}'] = {'error': 'Sistema instável para classes 1..%d' % i}
            continue
        W = 1.0 / (mu - cumulative)
        Wq = W - 1.0 / mu
        L = lam * W
        Lq = lam * Wq
        out[f'class_{i}'] = {'Taxa de chegada da classe i (λᵢ)': lam,
                             'Tempo médio no sistema da classe i (Wᵢ)': W,
                             'Tempo médio na fila da classe i (Wqᵢ)': Wq,
                             'Número médio no sistema da classe i (Lᵢ)': L,
                             'Número médio na fila da classe i (Lqᵢ)': Lq,
                             'Ocupação cumulativa até a classe i (ρ acumulado)': rho_cum}
    return out
