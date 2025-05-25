def avaliar_carteira(carteira, evento, valor):
    # Regra dummy só para exemplo
    score = 50
    if valor > 1000:
        score -= 10
    if evento == "withdraw":
        score -= 15
    if evento == "mint":
        score += 10
    risco = "baixo"
    if score < 60:
        risco = "moderado"
    if score < 40:
        risco = "alto"
    return score, risco
