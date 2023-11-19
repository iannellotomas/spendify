import os


def submenuSearchByString(option):
    message = ">> BUSCAR > "
    match option:
        case "1":
            message += "POR NOMBRE"
        case "2":
            message += "POR CATEGORÍA"
        case "3":
            message += "POR MÉTODO DE PAGO"

    while True:
        os.system("cls")
        print(
            f"""
{message}\n← VOLVER (V)
----------------------------------
                """
        )
        name = input("Cadena a buscar: ")
        print(name)
        enter = input("\nPresioná ENTER para volver al menú")
        break
    return
