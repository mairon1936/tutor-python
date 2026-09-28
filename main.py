def main():
    print("Hello from tutor-python!")
    tutor = TutorDePython()
    print(tutor.responder("explicame variable"))
    print(tutor.responder("explicame algo que no existe"))


class TutorDePython:
    def __init__(self):
        self.historial = []
        self.temas = {
            "variables": {"explicacion": "Espacios con nombre para guardar datos."},
            "listas": {"explicacion": "Colecciones ordenadas y modificables."},
            "tuplas": {"explicacion": "Colecciones ordenadas e inmutables."},
            "clase": {"explicacion": "Plantilla para crear objetos."},
            "metodos_de_git": {
                "explicacion": "Comandos para gestionar repositorios y cambios."
            },
        }
        self.historiar()

    def historiar(self, mensaje=None, respuesta=None):
        if mensaje is None and respuesta is None:
            self.historial = []
        else:
            self.historial.append({"mensaje": mensaje, "respuesta": respuesta})

    def explicar_concepto(self, mensaje_normalizado):
        for tema, info in self.temas.items():
            if tema in mensaje_normalizado or tema.rstrip("s") in mensaje_normalizado:
                return info["explicacion"]
        temas_disponibles = ", ".join(self.temas.keys())
        return f"No tengo ese tema. Puedo explicar: {temas_disponibles}."

    def responder(self, mensaje):
        self.historial.append(("estudiante", mensaje))
        mensaje_normalizado = mensaje.lower()
        if "adios" in mensaje_normalizado or "salir" in mensaje_normalizado:
            respuesta = "Hasta luego! Sigue practicando."
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = "Hola! Soy tu tutor de Python."
        elif "explica" in mensaje_normalizado or "explicame" in mensaje_normalizado:
            respuesta = self.explicar_concepto(mensaje_normalizado)
        else:
            respuesta = "Todavia no se responder eso."
        self.historial.append(("tutor", respuesta))
        return respuesta

if __name__ == "__main__":
    main()

#1- ¿Que temas va a explicar mi tutor de python?

# explicara las variables, las listas, las tuplas, las (clase), metodos de git.

# 2- ¿Que necesita "self" para recordar: la conversacion completa, y el resultado de cada pregunta que ya intentaron?

# "self" necesita el metodo constructor _init_ , luego self.historiar

# 3-Si preguntan por un tema que no existe, que deve responder?

# deve enviar un mensaje por defecto que diga , que no tiene informacion sobre ese tema.

# 4-¿Cuando alguien responda una pregunta, como se sabe si acerto?

# se creara una variable "acerto" con respuesta_usuario.strip().lower() == respuesta correcta.lower()

