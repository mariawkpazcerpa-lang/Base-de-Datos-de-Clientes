import sqlite3
import colorama
colorama.init()

conexion = sqlite3.connect("base_datos_clientes.db")
cursor = conexion.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            dni INTEGER NOT NULL,
            edad INTEGER NOT NULL,
            email TEXT NOT NULL
            
   )
''')
conexion.commit()
conexion.close()

def registrar_cliente():
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    
    try:
        while True:
                    print(colorama.Fore.CYAN + "~~Registrar cliente nuevo~~")
                    nombre = input( "Ingresa el Nombre del cliente: ").strip().capitalize()
                    apellido = input( "Ingresa la Apellido del cliente: ").strip().capitalize()
                    dni = input( "Ingresa el DNI del cliente (Sin puntos, ni comas): ").strip()
                    edad = input( "Ingresa la Edad del cliente: ").strip()
                    email = input( "Ingresa le Correo Electrónico del cliente: "+ colorama.Style.RESET_ALL).strip().lower()

                    if not nombre or not apellido:
                        print(colorama.Fore.RED + "[ERROR] El Nombre y el Apellido no pueden estar vacíos." + colorama.Style.RESET_ALL)
                        continue
                    
                    if not dni.isdigit() or not edad.isdigit():
                        print(colorama.Fore.RED + "[ERROR] El DNI y la Edad deben ser digitos"+ colorama.Style.RESET_ALL)
                        continue
                    
                    
                    if not email:
                        print(colorama.Fore.RED + "[ERROR] El Correo Electrónifco no puede estar vacío." + colorama.Style.RESET_ALL)
                        continue

                    if not "@" in email or email.count("@") != 1:
                        print("[ERROR] El Correo Electrónico debe contener una única '@'.")
                        continue
                    
                    _, domain_part = email.split("@")
                    if "." not in domain_part:
                        print("[ERROR] El dominio del correo debe contener al menos un punto ('.').")
                        continue
                    
                    cursor.execute("SELECT * FROM clientes WHERE dni = ?", (dni,))
                    resultado = cursor.fetchone()
                    if resultado:
                        print(colorama.Fore.RED + "Este cliente ya está registrado" + colorama.Style.RESET_ALL)
                        continue
                    else:
                        break
       
        conexion.execute("BEGIN TRANSACTION")
        cursor.execute('''
            INSERT INTO clientes (nombre, apellido, dni, edad, email)
            VALUES (?,?,?,?,?)
        ''', (nombre, apellido, int(dni), int(edad), email))
        conexion.commit()
        print(colorama.Fore.GREEN +  f"Cliente {nombre} registrado correctamente" + colorama.Style.RESET_ALL)
       
    except sqlite3.IntegrityError:
      conexion.rollback()
      print(colorama.Fore.RED + "[ERROR] El cliente ya está registrado" + colorama.Style.RESET_ALL)
    
    except sqlite3.Error as e:
      conexion.rollback()
      print(colorama.Fore.RED +  f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)


    finally:
      conexion.close()

def ver_lista_clientes():
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    print("\nLista de clientess: ")
    for cliente in clientes:
        print(colorama.Fore.MAGENTA +  f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)

def busqueda_cliente():
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    try:
            while True:    
                    print(colorama.Fore.CYAN + "---Búsqueda de cliente---")
                    print("1 ~ Buscar por ID.")
                    print("2 ~ Buscar por Nombre.")
                    print("3 ~ Buscar por Apellido.")
                    print("4 ~ Buscar por  DNI." + colorama.Style.RESET_ALL)
                        
                    try:
                        opcion = int(input(colorama.Fore.CYAN + "Ingresa la opcion deseada: " + colorama.Style.RESET_ALL))
            
                    except ValueError:
                        print(colorama.Fore.RED + "Por favor, ingresá un número válido." + colorama.Style.RESET_ALL)
                        continue

                    match opcion:
                        case 1:
                            try:
                                id_cliente = input(colorama.Fore.MAGENTA + "Ingresá el ID del cliente a buscar: " + colorama.Style.RESET_ALL).strip()
                                if not id_cliente.isdigit():
                                    print(colorama.Fore.RED + "El ID debe ser numérico." + colorama.Style.RESET_ALL)
                                    return
                                
                                cursor.execute("SELECT * FROM clientes WHERE id = ?",(id_cliente,))
                                resultado = cursor.fetchone()
                                if not resultado:
                                    print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
                                
                                else:
                                    cliente = resultado 
                                    print(colorama.Fore.MAGENTA + f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)
                    
                            except ValueError:
                                print(colorama.Fore.RED + "La casilla de DNI no puede quedar vacía o con caracteres no numéricos." + colorama.Style.RESET_ALL)

                            except sqlite3.Error as e:
                                print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
                                    
                            finally:
                                conexion.close()
                                break

                        case 2:
                            try:
                                nombre_cliente = input(colorama.Fore.MAGENTA + "Ingresá el nombre del cliente a buscar: " + colorama.Style.RESET_ALL).strip()
                                cursor.execute("SELECT * FROM clientes WHERE nombre = ?",(nombre_cliente,))
                                resultado = cursor.fetchall()
                                if not resultado:
                                    print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
                                else:
                                    for cliente in resultado:
                                        print(colorama.Fore.MAGENTA + f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)
                            

                            except sqlite3.Error as e:
                                print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
                                    
                            finally:
                                conexion.close()
                                break
                          
                        case 3:
                            try:
                                apellido_cliente = input(colorama.Fore.MAGENTA + "Ingresá el apellido del cliente a buscar: " + colorama.Style.RESET_ALL).strip()
                                cursor.execute("SELECT * FROM clientes WHERE apellido = ?",(apellido_cliente,))
                                resultado = cursor.fetchall()
                                if not resultado:
                                    print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
                                else:
                                    for cliente in resultado:
                                        print(colorama.Fore.MAGENTA + f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)
                            

                            except sqlite3.Error as e:
                                print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
                                    
                            finally:
                                conexion.close()
                                break
                        case 4:
                            try:
                                DNI_cliente = input(colorama.Fore.MAGENTA + "Ingresá el DNI del cliente a buscar: " + colorama.Style.RESET_ALL).strip()
                                if not DNI_cliente.isdigit():
                                    print(colorama.Fore.RED + "El DNI debe ser numérico." + colorama.Style.RESET_ALL)
                                    return
                                
                                cursor.execute("SELECT * FROM clientes WHERE dni = ?",(DNI_cliente,))
                                resultado = cursor.fetchone()
                                if not resultado:
                                    print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
                                
                                else:
                                    cliente = resultado 
                                    print(colorama.Fore.MAGENTA + f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)
                    
                            except ValueError:
                                print(colorama.Fore.RED + "La casilla de DNI no puede quedar vacía o con caracteres no numéricos." + colorama.Style.RESET_ALL)

                            except sqlite3.Error as e:
                                print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
                                    
                            finally:
                                conexion.close()
                                break

    except sqlite3.Error as e:
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
    finally:
            conexion.close()

def actualizar_nombre(id_cliente, nuevo_nombre,):
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    conexion.execute("BEGIN TRANSACTION")
    try:
        cursor.execute("UPDATE clientes SET nombre = ? WHERE id = ?", (nuevo_nombre, id_cliente,))
        conexion.commit() 
        print(colorama.Fore.GREEN + "Nombre actualizado correctamente." + colorama.Style.RESET_ALL) 
    except ValueError:
        conexion.rollback()
        print(colorama.Fore.RED + "La casilla de Nombre no puede quedar vacía" + colorama.Style.RESET_ALL)
    except sqlite3.Error as e:
        conexion.rollback()
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
    
    finally:
        conexion.close()

def actualizar_apellido(id_cliente, nuevo_apellido,):
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    conexion.execute("BEGIN TRANSACTION")
    try:
        cursor.execute("UPDATE clientes SET apellido = ? WHERE id = ?", (nuevo_apellido, id_cliente,))
        conexion.commit() 
        print(colorama.Fore.GREEN + "Apellido actualizado correctamente." + colorama.Style.RESET_ALL) 
    except ValueError:
        conexion.rollback()
        print(colorama.Fore.RED + "La casilla de Apellido no puede quedar vacía" + colorama.Style.RESET_ALL)
    except sqlite3.Error as e:
        conexion.rollback()
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
    
    finally:
        conexion.close()

def actualizar_email(id_cliente, nuevo_email,):
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    conexion.execute("BEGIN TRANSACTION")
    try:
        cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (nuevo_email, id_cliente,))
        conexion.commit() 
        print(colorama.Fore.GREEN + "Correo Electrónico actualizado correctamente." + colorama.Style.RESET_ALL) 
    except ValueError:
        conexion.rollback()
        print(colorama.Fore.RED + "La casilla de Correo Electrónico no puede quedar vacía" + colorama.Style.RESET_ALL)
    except sqlite3.Error as e:
        conexion.rollback()
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
    
    finally:
        conexion.close()

def actualizar_edad(id_cliente, nuevo_edad,):
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    conexion.execute("BEGIN TRANSACTION")
    try:
        cursor.execute("UPDATE clientes SET edad = ? WHERE id = ?", (nuevo_edad, id_cliente,))
        conexion.commit() 
        print(colorama.Fore.GREEN + "Edad actualizado correctamente." + colorama.Style.RESET_ALL) 
    except ValueError:
        conexion.rollback()
        print(colorama.Fore.RED + "La casilla de Edad no puede quedar vacía" + colorama.Style.RESET_ALL)
    except sqlite3.Error as e:
        conexion.rollback()
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
    
    finally:
        conexion.close()

def actualizar_cliente():
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    
    id_cliente = input(colorama.Fore.CYAN + "Ingresá el ID del cliente a actualizar: " + colorama.Style.RESET_ALL).strip()
    if not id_cliente.isdigit():
        print(colorama.Fore.RED + "El ID debe ser numérico." + colorama.Style.RESET_ALL)
        return
   
    try:    
        cursor.execute("SELECT * FROM clientes WHERE id = ?",(id_cliente,))
        resultado = cursor.fetchone()
        if not resultado:
            print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
        else:
            print(resultado)
            while True:    
                print(colorama.Fore.CYAN + "---Actualización de datos---")
                print("1 ~ Actualizar Nombre.")
                print("2 ~ Actualizar Apellido.")
                print("3 ~ Actualizar Edad.")
                print("4 ~ Actualizar Correo Electrónico." + colorama.Style.RESET_ALL)
                
                try:
                    opcion = int(input(colorama.Fore.CYAN + "Ingresa la opcion deseada: " + colorama.Style.RESET_ALL))
    
                except ValueError:
                    print(colorama.Fore.RED + "Por favor, ingresá un número válido." + colorama.Style.RESET_ALL)
                    continue

                match opcion:
                    case 1:
                        nuevo_nombre = input(colorama.Fore.CYAN + "Ingrese el nuevo Nombre del cliente: " + colorama.Style.RESET_ALL).strip().capitalize()
                        if not nuevo_nombre:
                            print(colorama.Fore.RED + "[ERROR] El Nombre no puede estar vacío." + colorama.Style.RESET_ALL)
                            continue
                        actualizar_nombre(id_cliente, nuevo_nombre,)
                        
                        break 

                    case 2:
                        nuevo_apellido = input(colorama.Fore.CYAN + "Ingrese el nuevo Apellido del cliente: " + colorama.Style.RESET_ALL).strip().capitalize()
                        actualizar_apellido(id_cliente, nuevo_apellido,)
                        if not nuevo_apellido:
                            print(colorama.Fore.RED + "[ERROR] El Apellido no puede estar vacío." + colorama.Style.RESET_ALL)
                            continue
                        break 

                    case 3:
                        nuevo_edad = input(colorama.Fore.CYAN + "Ingrese el nueva Edad del cliente: " + colorama.Style.RESET_ALL).strip()
                        if not nuevo_edad.isdigit():
                            print(colorama.Fore.RED + "[ERROR] La Edad deben ser digitos"+ colorama.Style.RESET_ALL)
                            continue
                        actualizar_edad(id_cliente, nuevo_edad,)
                        
                        break 
                    
                    case 4:
                        nuevo_email = input(colorama.Fore.CYAN + "Ingrese el nuevo Correo Electrónico del cliente: " + colorama.Style.RESET_ALL).strip().lower()
                        if not nuevo_email:
                            print(colorama.Fore.RED + "[ERROR] El Correo Electrónifco no puede estar vacío." + colorama.Style.RESET_ALL)
                            continue

                        if not "@" in nuevo_email or nuevo_email.count("@") != 1:
                            print("[ERROR] El Correo Electrónico debe contener una única '@'.")
                            continue
                        
                        _, domain_part = nuevo_email.split("@")
                        if "." not in domain_part:
                            print("[ERROR] El dominio del correo debe contener al menos un punto ('.').")
                            continue

                        actualizar_email(id_cliente, nuevo_email,)
                        
                        break 
    
    
    except ValueError:
                    print(colorama.Fore.RED + "Por favor, ingresá un número válido." + colorama.Style.RESET_ALL)
            
    except sqlite3.Error as e:
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
        conexion.rollback()
    
    finally:
        conexion.close()

def eliminar_cliente():
    conexion = sqlite3.connect("base_datos_clientes.db")
    cursor = conexion.cursor()
    
    try:
        id_cliente = input(colorama.Fore.CYAN + "Ingresá el ID del cliente a eliminar: " + colorama.Style.RESET_ALL).strip()
        if not id_cliente.isdigit():
            print(colorama.Fore.RED + "El ID debe ser numérico." + colorama.Style.RESET_ALL)
            return 
        cursor.execute("SELECT * FROM clientes WHERE id = ?",(id_cliente,))
        resultado = cursor.fetchone()
        if not resultado:
            print(colorama.Fore.RED + "El cliente buscado no existe." + colorama.Style.RESET_ALL)
        else:
            cliente = resultado 
            print(colorama.Fore.MAGENTA + f"ID: {cliente[0]} | Nombre: {cliente[1]} | Apellido: {cliente[2]} | DNI: {cliente[3]} | Edad: {cliente[4]} | Correo Electrónico: {cliente[5]} " + colorama.Style.RESET_ALL)
                    
            
            orden = int(input(colorama.Fore.CYAN + "Ingrese confirmación: Presione 0 para borrar.\n Presione 1 para volver al menu principal " + colorama.Style.RESET_ALL))
            if orden == 0:
                conexion.execute("BEGIN TRANSACTION")
                cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
                conexion.commit()
                print(colorama.Fore.GREEN + "El cliente ha sido eliminado" + colorama.Style.RESET_ALL)

            elif orden == 1:
                print(colorama.Fore.CYAN + "Volviendo al menú principal sin modificaciones..." + colorama.Style.RESET_ALL)
                conexion.commit()

    except sqlite3.Error as e:
        print(colorama.Fore.RED + f"[ERROR] Error en la base de datos: {e}" + colorama.Style.RESET_ALL)
        conexion.rollback()
        
    finally:
        conexion.close()

def menu():
     while True:   
                print(colorama.Fore.BLUE + "*~~*Base de Datos de Clientes*~~*") 
                print("*~~Menú Principal~~*")
                print("1 ~ Registrar un nuevo Cliente.")
                print("2 ~ Visualizar Base de Datos de Clientes.")
                print("3 ~ Buscar un Cliente.")
                print("4 ~ Actualizar un Cliente.")
                print("5 ~ Eliminar un Cliente.")
                print("6  ~ Salir." + colorama.Style.RESET_ALL)
                
                
                try:
                    opcion = int(input(colorama.Fore.BLUE + "Ingresa la opcion deseada: " + colorama.Style.RESET_ALL))
    
                except ValueError:
                    print(colorama.Fore.RED + "Por favor, ingresá un número válido." + colorama.Style.RESET_ALL)
                    continue

                match opcion:
                    case 1:
                        registrar_cliente()

                    case 2:
                        ver_lista_clientes()
                                        
                    case 3:
                        busqueda_cliente()
                        
                    case 4:
                        actualizar_cliente()
                        
                    case 5:
                        eliminar_cliente()

                    case 6:
                        break

menu()