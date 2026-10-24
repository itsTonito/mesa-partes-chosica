codigos_exp = []
dnis_solicitante = []
zonas_quebrada = []
tipos_recurso = []
cant_damnificados = []
niveles_urgencia = []
puntajes_prioridad = []
estados_tramite = []

QUEBRADAS = ["Pedregal Alto", "Carapongo", "Quirio", "Moyopampa", "Mariscal Castilla"]
RECURSOS = ["Agua potable", "Alimentos no perecibles", "Medicamentos", "Carpas", "Frazadas"]


def validar_dni(dni):
    return len(dni) == 8 and dni.isdigit()


def generar_codigo():
    numero = len(codigos_exp) + 1
    return "EXP-2026-" + str(numero).zfill(3)


def calcular_puntaje(urgencia, damnificados):
    return (urgencia * 100) + damnificados


def agregar_expediente(dni, zona, recurso, damnificados, urgencia):
    codigos_exp.append(generar_codigo())
    dnis_solicitante.append(dni)
    zonas_quebrada.append(zona)
    tipos_recurso.append(recurso)
    cant_damnificados.append(damnificados)
    niveles_urgencia.append(urgencia)
    puntajes_prioridad.append(calcular_puntaje(urgencia, damnificados))
    estados_tramite.append("Pendiente")


def cargar_datos_iniciales():
    agregar_expediente("45871236", "Quirio", "Agua potable", 45, 3)
    agregar_expediente("70214589", "Pedregal Alto", "Medicamentos", 120, 4)
    agregar_expediente("41236587", "Moyopampa", "Carpas", 18, 2)
    agregar_expediente("72589634", "Carapongo", "Alimentos no perecibles", 85, 4)


def pedir_opcion_lista(titulo, opciones):
    print(titulo)
    for i in range(len(opciones)):
        print("  " + str(i + 1) + ". " + opciones[i])
    eleccion = input("Elige una opcion: ").strip()
    while not (eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones)):
        print("Opcion no valida.")
        eleccion = input("Elige una opcion: ").strip()
    return opciones[int(eleccion) - 1]


def pedir_numero(mensaje, minimo, maximo):
    texto = input(mensaje).strip()
    while not (texto.isdigit() and minimo <= int(texto) <= maximo):
        print("Ingresa un numero entre " + str(minimo) + " y " + str(maximo) + ".")
        texto = input(mensaje).strip()
    return int(texto)


def registrar_solicitud():
    print("\n--- Registrar solicitud ---")
    dni = input("DNI del solicitante (8 digitos): ").strip()
    while not validar_dni(dni):
        print("DNI invalido: deben ser 8 digitos numericos.")
        dni = input("DNI del solicitante (8 digitos): ").strip()

    zona = pedir_opcion_lista("Quebrada afectada:", QUEBRADAS)
    recurso = pedir_opcion_lista("Recurso solicitado:", RECURSOS)
    damnificados = pedir_numero("Cantidad de damnificados (1 a 5000): ", 1, 5000)
    urgencia = pedir_numero("Nivel de emergencia (1 a 4): ", 1, 4)

    agregar_expediente(dni, zona, recurso, damnificados, urgencia)
    ultimo = len(codigos_exp) - 1
    print("Solicitud registrada con codigo " + codigos_exp[ultimo]
          + " (puntaje " + str(puntajes_prioridad[ultimo]) + ")")


cargar_datos_iniciales()
registrar_solicitud()
