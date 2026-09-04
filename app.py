import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Abraham Amasifuen")

modulos=st.sidebar.selectbox("Seleccione el modulo", ["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de Listas")
  
  valor_inicial = int(st.number_input("Ingresa el valor inicial del rango: "))
  valor_final = int(st.number_input("Ingresa el valor final del rango: "))

  lista = list(range(valor_inicial, valor_final))

  st.write(lista)

elif modulos == "Arreglos":
   st.write("Te encuentras en el modulo de Arreglos")
elif modulos == "Funciones":
  st.write("Te encuentras en el modulo de Funciones")
else
  st.write("Te encuentras en el modulo de POO")
  
