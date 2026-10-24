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


def agregar_expediente(dni, zona, recurso, damnificados, urgencia):
    codigos_exp.append("EXP-2026-" + str(len(codigos_exp) + 1).zfill(3))
    dnis_solicitante.append(dni)
    zonas_quebrada.append(zona)
    tipos_recurso.append(recurso)
    cant_damnificados.append(damnificados)
    niveles_urgencia.append(urgencia)
    puntajes_prioridad.append((urgencia * 100) + damnificados)
    estados_tramite.append("Pendiente")


def cargar_datos_iniciales():
    agregar_expediente("45871236", "Quirio", "Agua potable", 45, 3)
    agregar_expediente("70214589", "Pedregal Alto", "Medicamentos", 120, 4)
    agregar_expediente("41236587", "Moyopampa", "Carpas", 18, 2)
    agregar_expediente("72589634", "Carapongo", "Alimentos no perecibles", 85, 4)


cargar_datos_iniciales()
print("Expedientes cargados: " + str(len(codigos_exp)))
