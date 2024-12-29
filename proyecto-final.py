import sqlite3
from tabulate import tabulate
from estilos import titulos, estilos
from colorama import Fore, Back, Style, init

# Conectar a la base de datos SQLite
conn = sqlite3.connect("inventario.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    cantidad INTEGER NOT NULL CHECK(cantidad >= 0),
    precio REAL NOT NULL CHECK(precio > 0)
)
''')
conn.commit()

# Función para validar entradas
def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                raise ValueError("El valor debe ser positivo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}")

def validar_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El valor debe ser mayor que cero.")
            return valor
        except ValueError as e:
            print(f"Error: {e}")

# FUNCIONES
def registrar_nuevo_producto():
    print(Fore.CYAN + "Agregando producto...")
    nombre = input("Ingrese el nombre del producto: ").strip()
    cantidad = validar_entero("Cantidad: ")
    precio = validar_flotante("Precio: ")

    try:
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conn.commit()
        print("El Producto fue registrado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El producto ya existe.")

def listar_productos():
    print(Fore.CYAN + "\n---Mostrando Productos en Stock---")
    cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")
    productos = cursor.fetchall()

    if productos:
        # Usar tabulate para mostrar resultados
        tabla = tabulate(productos, headers=["ID", "Nombre", "Cantidad", "Precio ($)"], tablefmt="fancy_grid")
        print(tabla)
    else:
        print("No hay productos registrados.")

def actualizar_producto():
    listar_productos()
    id_producto = validar_entero(Fore.CYAN + "Ingrese el ID del producto a actualizar: ")
    print("Actualizando Stock...")
    nueva_cantidad = validar_entero("Nueva cantidad: ")
    nuevo_precio = validar_flotante("Nuevo precio: ")

    cursor.execute("UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?", (nueva_cantidad, nuevo_precio, id_producto))
    conn.commit()
    print(Fore.CYAN + "El Producto fue actualizado correctamente.")

def eliminar_producto():
    listar_productos()
    id_producto = validar_entero("Ingrese el ID del producto a eliminar: ")
    print(Fore.RED + "Borrando Producto")
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
    print("El Producto fue eliminado correctamente.")

def buscar_producto():
    print(Fore.CYAN + "Buscando producto...")
    nombre_o_parte = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre_o_parte + '%',))
    productos = cursor.fetchall()

    if productos:
        tabla = tabulate(productos, headers=["ID", "Nombre", "Cantidad", "Precio ($)"], tablefmt="fancy_grid")
        print(tabla)
    else:
        print("No se encontraron productos.")

def reporte_bajo_stock():
    print(Fore.CYAN + "\nMostrando Producto Con Stock Minimo...")
    limite = validar_entero("Ingrese el límite de bajo stock: ")
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    if productos:
        tabla = tabulate(productos, headers=["ID", "Nombre", "Cantidad", "Precio ($)"], tablefmt="fancy_grid")
        print(tabla)
    else:
        print(Fore.CYAN + "No hay Productos con bajo stock.")

def enter_para_continuar():
    input(Back.CYAN + "Enter para continuar....")

# Menú principal
while True:
    print(Style.BRIGHT + Fore.GREEN + Back.MAGENTA + "\nBIENVENIDX A KLEEFDEV INVENTORY APP" + Style.RESET_ALL + "\n")
    print(titulos['menu'])
    opcion = input(Back.GREEN + "\nIngrese una Opción: ")

    if opcion == '1':
        registrar_nuevo_producto()
    elif opcion == '2':
        listar_productos()
    elif opcion == '3':
        actualizar_producto()
    elif opcion == '4':
        eliminar_producto()
    elif opcion == '5':
        buscar_producto()
    elif opcion == '6':
        reporte_bajo_stock()
    elif opcion == '0':
        print(Fore.CYAN + "Gracias por usar nuestra App.")
        conn.close()
        break
    else:
        print(Fore.RED + "Opción incorrecta, intente de nuevo.")
    if opcion != "0":
        enter_para_continuar()