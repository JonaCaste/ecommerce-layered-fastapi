# Virtual enviroment
* Para crear nuestro entorno virtual utilizamos `py -m venv env`
* Ahora iniciamos nuestro entorno con el comando `env/Scripts/activate`
    * En windows ejecutamos este comando para evitar errores `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
* instalamos nuestros paquetes cn el comando `pip install -r requirements.txt`
* Salimos del entorno virtual `deactivate env`

# Dev
* Iniciar aplicación `fastapi dev main.py`

# Prod
* Iniciar aplicación