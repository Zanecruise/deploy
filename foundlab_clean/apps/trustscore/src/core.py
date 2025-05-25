def calcular_trustscore_comportamental(wallet, evento, valor, historico_wallet):
    score = 50  # Base neutra

    if valor > 500:
        score += 10
    if evento == "mint":
        score += 5
    elif evento == "withdraw":
        score -= 10
    if historico_wallet.get("negados", 0) >= 3:
        score -= 15
    if historico_wallet.get("liberados", 0) >= 5:
        score += 10
    if historico_wallet.get("mudanca_comportamento", False):
        score -= 7
    if historico_wallet.get("eventos_dia", 0) > 10:
        score -= 12
    if historico_wallet.get("nft_foundlab", False):
        score += 8
    if historico_wallet.get("flag_fraude", False):
        score -= 30
    if historico_wallet.get("apenas_mint", False):
        score -= 5
    if historico_wallet.get("trusted_origin", False):
        score += 12
    if historico_wallet.get("curva_valor", "flat") == "ascendente":
        score += 6
    if historico_wallet.get("dormencia", False):
        score -= 8
    if historico_wallet.get("eventos_premium", 0) > 0:
        score += 5
    if historico_wallet.get("dias_atividade", 0) < 3:
        score -= 10
    if historico_wallet.get("whitelisted", False):
        score += 15

    score = max(0, min(score, 100))
    return score

def interpretar_score(score):
    if score >= 95:
        return ("liberado", "excelente", "verde-escuro")
    elif score >= 90:
        return ("liberado", "muito confiável", "verde")
    elif score >= 85:
        return ("liberado", "confiável", "verde-claro")
    elif score >= 80:
        return ("liberado", "bom risco", "azul")
    elif score >= 75:
        return ("sob avaliação", "risco moderado+", "azul-claro")
    elif score >= 70:
        return ("sob avaliação", "risco moderado", "amarelo")
    elif score >= 65:
        return ("sob avaliação", "limítrofe", "amarelo-claro")
    elif score >= 60:
        return ("negado", "risco relevante", "laranja")
    elif score >= 55:
        return ("negado", "risco acentuado", "laranja-claro")
    elif score >= 50:
        return ("negado", "risco elevado", "vermelho-claro")
    elif score >= 40:
        return ("negado", "risco crítico", "vermelho")
    elif score >= 35:
        return ("bloqueado", "fraude suspeita", "vermelho-escuro")
    elif score >= 30:
        return ("bloqueado", "análise manual", "preto")
    elif score >= 20:
        return ("bloqueado", "carteira perigosa", "cinza-escuro")
    else:
        return ("bloqueado", "inviável", "cinza")
