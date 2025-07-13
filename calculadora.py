import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Plan de Carrera",
    page_icon="🌸",
    layout="wide"
)

# --- FUNCIÓN PARA CARGAR Y MOSTRAR EL HTML ---
def show_html_file():
    # Abrir el archivo HTML
    try:
        with open('planificador.html', 'r', encoding='utf-8') as f:
            html_code = f.read()
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo 'planificador.html'.")
        st.info("Asegúrate de que el archivo 'planificador.html' esté en la misma carpeta que 'app.py'.")
        return

    # Usar st.components.v1.html para renderizar el archivo
    # El alto (height) es importante para que el scroll funcione bien dentro del HTML
    components.html(html_code, height=1200, scrolling=True)

# --- EJECUTAR LA APLICACIÓN ---
if __name__ == "__main__":
    show_html_file()

