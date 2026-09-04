import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Abraham Amasifuen")

modulos=st.sidebar.selectbox("Seleccione el modulo", ["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de Listas")
elif modulos == "Arreglos":
   st.write("Te encuentras en el modulo de Arreglos")
elif modulos == "Funciones":
  st.write("Te encuentras en el modulo de Funciones")
else
  st.write("Te encuentras en el modulo de POO")
  
