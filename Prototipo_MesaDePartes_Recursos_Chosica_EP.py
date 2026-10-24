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


def mostrar_expedientes():
    print("\n" + "-" * 94)
    print(f"{'CODIGO':<14}{'DNI':<10}{'QUEBRADA':<19}{'RECURSO':<25}{'DAMN.':>6}{'URG.':>6}{'PUNT.':>7}  ESTADO")
    print("-" * 94)
    if len(codigos_exp) == 0:
        print("No hay expedientes registrados.")
    for i in range(len(codigos_exp)):
        print(f"{codigos_exp[i]:<14}{dnis_solicitante[i]:<10}{zonas_quebrada[i]:<19}"
              f"{tipos_recurso[i]:<25}{cant_damnificados[i]:>6}{niveles_urgencia[i]:>6}"
              f"{puntajes_prioridad[i]:>7}  {estados_tramite[i]}")
    print("-" * 94)


def buscar_por_codigo():
    print("\n--- Buscar expediente ---")
    buscado = input("Codigo (ej. EXP-2026-001): ").strip().upper()
    posicion = -1
    for i in range(len(codigos_exp)):
        if codigos_exp[i] == buscado:
            posicion = i
    if posicion == -1:
        print("No se encontro el expediente " + buscado)
    else:
        print("Expediente encontrado:")
        print("  Codigo:        " + codigos_exp[posicion])
        print("  DNI:           " + dnis_solicitante[posicion])
        print("  Quebrada:      " + zonas_quebrada[posicion])
        print("  Recurso:       " + tipos_recurso[posicion])
        print("  Damnificados:  " + str(cant_damnificados[posicion]))
        print("  Urgencia:      " + str(niveles_urgencia[posicion]))
        print("  Puntaje:       " + str(puntajes_prioridad[posicion]))
        print("  Estado:        " + estados_tramite[posicion])


cargar_datos_iniciales()
mostrar_expedientes()
buscar_por_codigo()
