# import packages
from openai import OpenAI
import streamlit as st

client: OpenAI = None


# Load environment variables from -env file
def load_env_variables():
    try:
        from dotenv import load_dotenv

        load_dotenv()  # Cargar variables desde .env
        print("INFO: Archivo .env cargado.")
    except ImportError:
        print(
            "INFO: python-dotenv no está instalado, no se cargará .env automáticamente en main.py."
        )


def setup_gui():
    st.title("Hello, GenAI")
    st.write("This is your first Streamlit app.")


@st.cache_data
def get_response(prompt: str, temperature: float):
    response = client.responses.create(
        model="gpt-4o",
        input=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_output_tokens=100,
    )

    return response


def test_genai(prompt: str, temperature: float):

    with st.spinner("IA está trabajando..."):
        response = get_response(prompt, temperature)

        st.write(response.output_text)


def build_gui_controls():
    # prompt = st.text_input("Instruccion", "", placeholder="Especifique su instrucción")
    prompt = st.text_area("Instruccion", "", placeholder="Especifique su instrucción")

    temperature = st.slider(
        "Temperatura del modelo",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.01,
        help="Control de aleatoriedad: 0 = deterministico, 1 = muy creativo",
    )

    test_genai(prompt, temperature)


if __name__ == "__main__":
    load_env_variables()
    # Initialize OpenAI client
    client = OpenAI()

    setup_gui()
    build_gui_controls()
