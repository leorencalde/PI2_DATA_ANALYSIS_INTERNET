import subprocess

# Ruta al archivo del dashboard de Streamlit
dashboard_file = "./dashboard.py"

# Ruta completa al ejecutable de Streamlit
streamlit_path = r"C:\Users\aleja\AppData\Local\Programs\Python\Python312\Scripts\streamlit.exe"

# Comando para ejecutar el archivo de Streamlit
command = [streamlit_path, "run", dashboard_file]

# Ejecutar el comando
subprocess.run(command)
