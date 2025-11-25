import math

def mm_inf(lambda_, mu):

    rho = lambda_ / mu
    L = rho
    W = 1/ mu
    Wq = 0
    P0 = math.exp(-rho)


    return {
        "Taxa de ocupação (ρ)": rho,
        "Probabilidade do sistema vazio (P₀)": P0,
        "Número médio no sistema (L)": L,
        "Tempo médio no sistema (W)": W,
        "Tempo médio na fila (Wq)": Wq
    }
