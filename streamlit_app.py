import os
import re
import string
import time
import pandas as pd
import streamlit as st

def build_gui():
    st.title("Hello, GenAI!")
    st.write("This is your GenAI-powered data processing app.")

    # Layout two buttons side by side
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📥 Carga de datos"):
            try:                
                with st.spinner("Cargando datos..."):
                    time.sleep(5)
                    csc_path = get_dataset_path()
                    st.session_state["df"] = pd.read_csv(csc_path)
                    st.success("¡Dataset cargado correctamente!")
            except FileNotFoundError:
                st.error("Dataset no encontrado. Por favor revise la ruta del archivo")

    with col2:
        if st.button("🧹 Analizar reseñas"):
            if "df" in st.session_state:
                st.session_state["df"]["CLEANED_SUMMARY"] = st.session_state["df"]["SUMMARY"].apply(clean_text)
                st.success("Análisis realizado")
            else:
                st.warning("Por favor cargue el dataset antes de analizar las reseñas")

    # Display the dataset if it exists
    if "df" in st.session_state:
        # Product filter dropdown
        st.subheader("🔍 Filtrar por producto")
        product = st.selectbox(
            "Elija un producto",
            ["Todos los productos"] + list(st.session_state["df"]["PRODUCT"].unique()),
        )
        st.subheader(f"📁 Reseñas del producto: {product}")

        if product != "Todos los productos":
            filtered_df = st.session_state["df"][
                st.session_state["df"]["PRODUCT"] == product
            ]
        else:
            filtered_df = st.session_state["df"]

        st.dataframe(filtered_df)
        
        st.subheader("Puntuación de sentimiento por producto")
        grouped = st.session_state["df"].groupby(["PRODUCT"])["SENTIMENT_SCORE"].mean()
        st.bar_chart(grouped)


# Helper function to get dataset path
def get_dataset_path():
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the CSV file
    csv_path = os.path.join(current_dir, "data", "customer_reviews.csv")
    return csv_path


def clean_text(text: str) -> str:
    """Limpia una cadena de texto:
    1. Convierte a minúsculas.
    2. Elimina la puntuación.
    3. Elimina espacios en blanco adicionales.

    Args:
        text (str): La cadena de texto a limpiar.

    Returns:
        str: La cadena de texto limpia.
    """
    if not isinstance(text, str):
        return ""
    # 1. Convertir a minúsculas
    text = text.lower()
    
    # 2. Eliminar puntuación
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # 3. Eliminar espacios en blanco adicionales y en los extremos
    text = re.sub(r"\s+", " ", text).strip()
    return text

if __name__ == "__main__":
    # Initialize OpenAI client
    build_gui()
