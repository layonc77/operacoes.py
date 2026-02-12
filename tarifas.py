import streamlit as st

st.title("Calculadora de Tarifa")

# Lista para armazenar os pesos
pesos = []

# Campo para adicionar um peso
novo_peso = st.number_input("Peso da bagagem (kg)", min_value=0.0, step=0.1)

if st.button("Adicionar bagagem"):
    pesos.append(novo_peso)
    st.session_state.pesos = pesos  # Guardar na sessão

# Inicializar lista na sessão se não existir
if "pesos" not in st.session_state:
    st.session_state.pesos = []

# Mostrar bagagens adicionadas
st.write("Bagagens adicionadas:", st.session_state.pesos)

# Definindo faixas de peso e valores
faixas = [
    (0, 1, 8.05),
    (1.1, 3, 8.94),
    (3.1, 5, 9.61),
    (5.1, 10, 11.18),
    (10.1, 15, 13.41),
    (15.1, 20, 14.75),
    (20.1, 25, 16.99),
    (25.1, 30, 17.88),
    (31, 40, 18.46),
]

if st.button("Calcular total"):
    total = 0
    for peso in st.session_state.pesos:
        valor = None
        for min_peso, max_peso, preco in faixas:
            if min_peso <= peso <= max_peso:
                valor = preco
                break
        if valor is None:
            st.error(f"Peso {peso} kg acima do limite permitido.")
        else:
            total += valor
            st.write(f"Bagagem {peso} kg: R$ {valor:.2f}")
    st.success(f"Valor total de todas as bagagens: R$ {total:.2f}")


print("Creat by layon")
