# 📋 Proyecto Base de Datos de Clientes (CRUD)

Este es un proyecto de consola en **Python** que implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) de clientes utilizando **SQLite** como base de datos.

## 🚀 Funcionalidades

- **Agregar clientes** con datos como nombre, apellido, DNI, edad y correo electrónico.  
- **Listar todos los clientes** registrados en la base de datos.  
- **Buscar clientes** por su ID o DNI.  
- **Actualizar datos** de un cliente existente.  
- **Eliminar clientes** de la base de datos.  
- Validaciones:  
  - El **DNI no puede repetirse** (único por cliente).  
  - Se valida que los IDs ingresados sean numéricos.  
  - Validación básica de correos electrónicos.  

## 🛠️ Tecnologías utilizadas

- **Python 3**  
- **SQLite3** (base de datos liviana incluida en Python)  
- **Colorama** para dar color a los mensajes en la consola  

## 📂 Estructura del proyecto
📦 Base-de-Datos-de-Clientes
┣ 📜 lista_clientes.py # Archivo principal con el menú y la lógica CRUD
┣ 📜 base_datos_clientes.db # Base de datos SQLite
┣ 📜 README.md # Documentación del proyecto
┗ 📜 requirements.txt # Dependencias necesarias


## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/mariawkpazcerpa-lang/Base-de-Datos-de-Clientes.git
´´´


Entrar en la carpeta:
cd Base-de-Datos-de-Clientes

(Opcional) Crear un entorno virtual:
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows


Instalar dependencias:
pip install -r requirements.txt


 Repositorio de código
Código completo: https://github.com/mariawkpazcerpa-lang/Base-de-Datos-de-Clientes

📬 Contacto
Email: mariawkpazcerpa@gmail.com

LinkedIn: María de la Paz Cerpa

Ejecutar el programa:
python lista_clientes.py
