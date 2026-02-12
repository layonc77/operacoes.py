import streamlit as st

st.title("Tabela de balcão GLS")
Print("creat by layon souza")
quantidade = st.number_input("Quantidade de volumes", min_value=1)#st.number_input --- funcao para criar um campo de input numerico, min_value define o valor minimo permitido 
kg = st.number_input("Peso da bagagem (kg)", min_value=0.0)

if st.button("Calcular"):
    
    if kg <= 1:
        valor = 8.05
    elif kg >= 1.1 and kg <= 3:
        valor = 8.94
    elif kg >= 3.1 and kg <= 5:
        valor = 9.61
    elif kg >= 5.1 and kg <= 10:
        valor = 11.18
    elif kg >= 10.1 and kg <= 15:
        valor = 13.41
    elif kg >= 15.1 and kg <= 20:
        valor = 14.75
    elif kg >= 20.1 and kg <= 25: 
        valor = 16.99
    elif kg >= 25.1 and kg <= 30: 
        valor = 17.88
    elif kg >= 31 and kg <= 40:
        valor = 18.46
    else:
        st.error("Peso acima do limite permitido.")
        st.stop()

    total = quantidade * valor
    st.success(f"Valor total: R$ {total:.2f}")
