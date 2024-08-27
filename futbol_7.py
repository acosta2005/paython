jugadores = [
    {"nombres": "vidal","equipo": "colo colo","representante": "fernando felicovich"},
    {"nombres": "palacios","equipo": "colo colo","representante": None},
    {"nombres": "falcon","equipo": "colo colo","representante": "Gerardo Arias"}, 
    {"nombres": "charles Aranguiz","equipo": "Universidad de Chile","representante": "Andres Cury"}
]

for jugador in jugadores:
    print(jugador["nombres"], jugador["equipo"], jugador["representante"],sep=" - ")