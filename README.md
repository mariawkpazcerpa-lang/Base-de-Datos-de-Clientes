# 👥 Sistema de Gestión de Base de Datos de Clientes

Este proyecto es una aplicación de consola desarrollada en **Python** que implementa un sistema **CRUD** (Create, Read, Update, Delete) completo. Utiliza **SQLite3** para la persistencia de datos y **Colorama** para mejorar la experiencia del usuario mediante una interfaz visualmente organizada en la terminal.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🚀 Demo Interactiva

Prueba la aplicación directamente en tu navegador sin instalar nada:

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_in-Codespaces-blueviolet?style=for-the-badge&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=master&repo=mariawkpazcerpa-lang/Base-de-Datos-de-Clientes)

> **Instrucción:** Una vez que cargue el Codespace, escribe `python lista_clientes.py` en la terminal para iniciar el programa.

---

## ✨ Características Técnicas

El sistema no solo gestiona datos, sino que aplica reglas de integridad propias de la ingeniería de software:

* **Persistencia Real:** Uso de SQLite3 para garantizar que los datos no se pierdan al cerrar el programa.
* **Integridad de Datos:** Validación de DNI único (Primary Key) para evitar registros duplicados.
* **Validación de Inputs:** Control de tipos (IDs numéricos) y formatos de correo electrónico.
* **Interfaz Colorizada:** Feedback visual mediante Colorama para diferenciar éxitos, errores y alertas.
* **Arquitectura Limpia:** Separación de la lógica de negocio y la gestión de la base de datos.

## 🛠️ Tecnologías y Librerías

* **Python 3.x**: Lenguaje core del sistema.
* **SQLite3**: Motor de base de datos embebido.
* **Colorama**: Formateo de texto y colores en terminal.
* **OS & Sys**: Manejo del sistema operativo y limpieza de consola.

## 📂 Estructura del Proyecto

```text
📦 Base-de-Datos-de-Clientes
 ┣ 📜 lista_clientes.py    # Lógica principal y menú interactivo
 ┣ 📜 base_datos_clientes.db # Archivo de base de datos SQLite
 ┣ 📜 requirements.txt     # Dependencias del proyecto
 ┗ 📜 README.md            # Documentación

⚙️ Instalación Local
Si prefieres ejecutarlo en tu máquina:

Clonar el repositorio:

Bash
git clone [https://github.com/mariawkpazcerpa-lang/Base-de-Datos-de-Clientes.git](https://github.com/mariawkpazcerpa-lang/Base-de-Datos-de-Clientes.git)
cd Base-de-Datos-de-Clientes
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar:

Bash
python lista_clientes.py


✒️ Autora
María de la Paz Cerpa - Estudiante de Ingeniería Informática.
Mail: mariawkpazcerpa@gmail.com
LinkedIn: María de la Paz Cerpa


