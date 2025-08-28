
## **Set up the development environment**

### **1. Creating the isolated Python environment**

To create an isolated Python environment, run the following command:

```bash
python -m venv .venv
```

This command will create a new folder with the new environment that will contain everything you need to activate the environment.

### **2. Activating the environment**

Now, we must activate the environment by executing the following command:

```bash
source .venv/scripts/activate
```

### **3. Installing dependencies**

Then we must install the dependencies.

```bash
pip install -r requirements.txt
```

### **4. Creating a hidden .env file**

We must create a hidden file called .env in the root directory. In this file, we will set our secret data.

### **5. Starting the app from Streamlit**

To start our app in a web browser run the following command:

```bash
streamlit run app.py
```

Ejemplo de un prompt para probar cambios en la temperatura del MML:

```bash
Eres un asistente creativo. Responde a la siguiente solicitud de manera concisa pero completa.

Solicitud: "Describe cómo sería un día perfecto en la playa, usando exactamente 3 oraciones. Incluye al menos dos actividades específicas."

Por favor, genera 5 respuestas diferentes a esta misma solicitud, mostrando variaciones creativas pero manteniendo los requisitos exactos.
```
