import os

def showError(message=""):
    enter = input(
        f"""
(!) {message}\nENTER para aceptar """
    )


def notice(message=""):
    os.system("cls")

    enter = input(
        f"""
\t--- (i) ---\n{message}\n\nENTER para continuar """
    )