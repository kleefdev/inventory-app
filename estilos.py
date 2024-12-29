from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)

# Definir estilos adicionales
estilos = {
    'bold': Style.BRIGHT + "Negrita" + Style.RESET_ALL,               # Negrita
    'italic': '\033[3m',               # Cursiva (manual, no en colorama)
    'underline': '\033[4m',            # Subrayado (manual, no en colorama)
    'centered': Style.BRIGHT + Fore.CYAN + "Centrado" + Style.RESET_ALL # Centrado (solo decorativo)
}

# Definir títulos con estilos personalizados
titulos = {
    'menu': (
        Style.BRIGHT + Fore.WHITE + Back.BLACK + "\n=== MENU DE GESTION DE INVENTARIO ===" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLACK + Back.WHITE + "\nExplora las Opciones y Optimiza tu Inventario de Forma Eficiente" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.YELLOW + "\n1. ➕  REGISTRAR NUEVO PRODUCTO" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.MAGENTA + "2. 📃  LISTAR PRODUCTOS" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.YELLOW + "3. 🔄️  ACTUALIZAR PRODUCTOS" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.MAGENTA + "4. ❌  ELIMINAR PRODUCTOS" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.YELLOW + "5. 🔍  BUSCAR PRODUCTOS" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.MAGENTA + "6. 🏢  REPORTE DE BAJO STOCK" + Style.RESET_ALL + "\n" +
        Style.BRIGHT + Fore.BLUE + Back.YELLOW + "0. 👋  SALIR" + Style.RESET_ALL
    )
}

