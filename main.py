def main():
    print("Hello from tutor-python!")
    tutor = TutorDePython()
    print(tutor.responder("explicame variable"))
    print(tutor.responder("explicame algo que no existe"))


class TutorDePython:
    def __init__(self):
        self.historial = []
        self.temas_dominados = {}
        self.temas = {
            "variables": {
                "explicacion": "Espacios con nombre para guardar datos.",
                "pregunta": "¿Qué símbolo se usa para asignar un valor en Python?",
                "numero": 1,
                "respuesta": "=",
                "tipo": "texto",
            },
            "lista": {
                "explicacion": "Colecciones ordenadas y modificables.",
                "pregunta": "¿En qué posición está el primer elemento de una lista?",
                "numero": 2,
                "respuesta": "0",
                "tipo": "numero",
            },
            "tuplas": {
                "explicacion": "Colecciones ordenadas e inmutables.",
                "pregunta": "¿Se pueden modificar las tuplas? (si/no)",
                "numero": 3,
                "respuesta": "no",
                "tipo": "texto",
            },
            "clase": {
                "explicacion": "Plantilla para crear objetos.",
                "pregunta": "¿Qué palabra clave se usa para definir una clase?",
                "numero": 4,
                "respuesta": "class",
                "tipo": "texto",
            },
            "git": {
                "explicacion": "Comandos para gestionar repositorios y cambios.",
                "pregunta": "¿Qué comando de Git registra un commit?",
                "numero": 5,
                "respuesta": "commit",
                "tipo": "texto",
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

    def hacer_pregunta(self, mensaje_normalizado):
        tema_encontrado = None
        for tema in self.temas:
            if tema in mensaje_normalizado:
                tema_encontrado = tema
                break
        if tema_encontrado is None:
            temas_disponibles = ", ".join(self.temas.keys())
            return f"Sobre que tema? Puedo preguntar sobre: {temas_disponibles}."
        info = self.temas[tema_encontrado]
        respuesta_estudiante = input(f"{info['pregunta']} ")
        if info["tipo"] == "numero":
            respuesta_numero = int(respuesta_estudiante)
            es_correcta = respuesta_numero == int(info["respuesta"])
        else:
            es_correcta = respuesta_estudiante.strip().lower() == info["respuesta"]
        self.temas_dominados[tema_encontrado] = es_correcta
        if es_correcta:
            return "Correcto!"
        return f"No es correcto. La respuesta era: {info['respuesta']}."

    def responder(self, mensaje):
        self.historial.append(("estudiante", mensaje))
        mensaje_normalizado = mensaje.lower()
        if "adios" in mensaje_normalizado or "salir" in mensaje_normalizado:
            respuesta = "Hasta luego! Sigue practicando."
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = "Hola! Soy tu tutor de Python."
        elif "pregunta" in mensaje_normalizado or "quiz" in mensaje_normalizado:
            respuesta = self.hacer_pregunta(mensaje_normalizado)
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

