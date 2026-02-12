import streamlit as st

st.title("Calculadora de Tarifa de Produtos")

# Inicializar lista na sessão
if "produtos" not in st.session_state:
    st.session_state.produtos = []

# Inputs de peso e quantidade
peso = st.number_input("Peso do produto (kg)", min_value=0.0, step=0.1)
quantidade = st.number_input("Quantidade do produto", min_value=1, step=1)

# Botão para adicionar produto à lista
if st.button("Adicionar produto"):
    st.session_state.produtos.append((peso, quantidade))
    st.success(f"Adicionado {quantidade} produto(s) de {peso} kg")

# Mostrar produtos adicionados
if st.session_state.produtos:
    st.write("Produtos adicionados:")
    for i, (p, q) in enumerate(st.session_state.produtos, start=1):
        st.write(f"{i}. {q} produto(s) de {p} kg")

if st.button("Limpar produtos"):
    st.session_state.produtos = []
    st.success("Lista de produtos limpa.")

# Faixas de peso e valores
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

# Botão para calcular total
if st.button("Calcular total"):
    if not st.session_state.produtos:
        st.error("Nenhum produto adicionado.")
    else:
        total = 0
        for peso, quantidade in st.session_state.produtos:
            valor = None
            for min_peso, max_peso, preco in faixas:
                if min_peso <= peso <= max_peso:
                    valor = preco
                    break
            if valor is None:
                st.error(f"Produto de {peso} kg acima do limite permitido.")
                continue
            subtotal = valor * quantidade
            st.write(f"{quantidade} produto(s) de {peso} kg: € {subtotal:.2f}")
            total += subtotal
        st.success(f"Valor total de todos os produtos: € {total:.2f}")


print("Creat by layon")
