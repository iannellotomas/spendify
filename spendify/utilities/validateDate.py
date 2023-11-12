from datetime import datetime, timedelta
from . import messages
import locale


def isValidDate(day, month, year, notFuture=False):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        enterDate = datetime(year, month, day)

        today = datetime.now()
        if notFuture and enterDate > today:
            messages.showError("La fecha ingresada no puede ser futura")
            return False

        return True
    except ValueError:
        messages.showError("La fecha ingresada no existe")
        return False


def getDateLabel(date):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)

    # Configuramos el idioma de la región a español
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

    if date.date() == today.date():
        return "Hoy"
    elif date.date() == yesterday.date():
        return "Ayer"
    elif date >= last_week:
        return "Esta semana"
    elif date >= last_month:
        return "Este mes"
    else:
        return date.strftime("%B %Y")
