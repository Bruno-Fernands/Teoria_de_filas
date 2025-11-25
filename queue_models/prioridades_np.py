def priorities_nonpreemptive(mu, lambdas):

    k = len(lambdas)
    rho_list = [lam / mu for lam in lambdas]


    if sum(rho_list) >= 1:
        return {"error": "Sistema instável: soma das cargas >= 1"}

    ES2 = 2 / (mu ** 2)

    results = {}
    sum_rho_prev = 0

    for i in range(k):
        lam_i = lambdas[i]
        rho_i = rho_list[i]

        sum_rho_i = sum(rho_list[:i+1])

        denom = (1 - sum_rho_i) * (1 - sum_rho_prev)
        Wqi = (sum(lambdas) * ES2) / (2 * denom)

        Wi = Wqi + 1/mu
        Li = lam_i * Wi
        Lqi = lam_i * Wqi

        results[f"class_{i+1}"] = {
            "lambda": lam_i,
            "rho": rho_i,
            "Wq": Wqi,
            "W": Wi,
            "Lq": Lqi,
            "L": Li,
        }

        sum_rho_prev += rho_i

    return results

