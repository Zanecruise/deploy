import streamlit as st
import requests

st.title("FoundLab TrustScore Checker")

wallet = st.text_input("Wallet Address")
evento = st.selectbox("Evento", ["mint", "transfer", "withdraw"])
valor = st.number_input("Valor do Evento", min_value=0.0)

if st.button("Calcular TrustScore"):
    payload = {
        "wallet": wallet,
        "evento": evento,
        "valor": valor
    }
    response = requests.post("http://localhost:8080/trustscore", json=payload)
    if response.ok:
        data = response.json()
        st.success(f"Score: {data['trustscore']} | Tier: {data['tier']} | Decisão: {data['decisao']}")
        st.image("badge.svg")
    else:
        st.error("Erro ao calcular TrustScore")
