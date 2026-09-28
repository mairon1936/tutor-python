PALABRAS_SALIDA = ("salir", "adios", "adiós", "ok bye", "hasta luego", "nos vemos", "nos bemos", "gracias")


def main():
    tutor = TutorDePython()
    iniciar_conversacion(tutor)


class TutorDePython:
    def __init__(self):
        self.historial = []
        self.temas_dominados = {}
        self.temas = {
            "variables": {
                "explicacion": "Una variable es un nombre asociado a un valor que el programa puede usar. En Python se crea al asignarle un valor, por ejemplo, edad = 12 o nombre = 'Ana'. El signo igual asigna el valor; no significa que ambos lados sean iguales. Los nombres pueden contener letras, números y guion bajo, pero no empezar con un número. Python determina el tipo del valor automáticamente, y una variable puede recibir otro valor más adelante.",
                "uso": "Se utiliza para guardar y reutilizar datos mientras el programa se ejecuta, como nombres, edades, resultados o valores que cambian. Así puedes consultar y actualizar esos datos sin repetirlos en el código.",
                "pregunta": "¿Qué símbolo se usa holapara asignar un valor en Python?",
                "numero": 1,
                "respuesta": "=",
                "tipo": "texto",
            },
            "lista": {
                "explicacion": "Una lista guarda varios elementos en un orden definido y permite modificarlos después. Se escribe entre corchetes, por ejemplo, frutas = ['manzana', 'pera']. Las posiciones empiezan en 0, así que frutas[0] es 'manzana'. Puedes cambiar un elemento, agregar otros con append() y consultar cuántos contiene con len(). Una lista también puede guardar valores de distintos tipos.",
                "uso": "Se utiliza para reunir datos relacionados cuando necesitas conservar su orden y poder agregar, quitar o modificar elementos, por ejemplo, una lista de tareas, nombres o productos.",
                "pregunta": "¿En qué posición está el primer elemento de una lista?",
                "numero": 2,
                "respuesta": "0",
                "tipo": "numero",
            },
            "tuplas": {
                "explicacion": "Una tupla guarda varios elementos en un orden definido, pero no permite cambiar sus elementos después de crearla. Normalmente se escribe entre paréntesis, por ejemplo, coordenadas = (3, 8). Sus posiciones también empiezan en 0 y se consultan como en una lista. Una tupla de un solo elemento necesita una coma, por ejemplo (5,). Se usa cuando los datos deben permanecer fijos.",
                "uso": "Se utiliza para agrupar datos relacionados que no deberían cambiar, como coordenadas, dimensiones o valores fijos. También permite devolver varios valores juntos desde una función.",
                "pregunta": "¿Se pueden modificar las tuplas? (si/no)",
                "numero": 3,
                "respuesta": "no",
                "tipo": "texto",
            },
            "clase": {
                "explicacion": "Una clase es una plantilla que define los datos y acciones que tendrán sus objetos. Se declara con la palabra class y suele incluir un método __init__ para inicializar cada objeto. Los datos se guardan como atributos y las acciones se escriben como métodos. Después se crean instancias llamando a la clase, por ejemplo, mi_objeto = MiClase().",
                "uso": "Se utiliza para crear objetos que comparten estructura y comportamiento, por ejemplo, representar estudiantes con nombre y edad, y métodos para mostrar o modificar esos datos.",
                "pregunta": "¿Qué palabra clave se usa para definir una clase?",
                "numero": 4,
                "respuesta": "class",
                "tipo": "texto",
            },
            "git": {
                "explicacion": "Git es un sistema de control de versiones que registra cambios en los archivos de un proyecto. Un repositorio contiene esos archivos y su historial. git status muestra el estado, git add prepara cambios y git commit los guarda en el historial con un mensaje. git push envía commits a un repositorio remoto y git pull descarga cambios. Así puedes revisar versiones y colaborar sin perder el trabajo anterior.",
                "uso": "Se utiliza para guardar y revisar el historial de cambios de un proyecto, recuperar versiones anteriores y colaborar con otras personas usando repositorios remotos.",
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
                frases_de_uso = (
                    "para que se utiliza",
                    "para que se utilizan",
                    "para qué se utiliza",
                    "para qué se utilizan",
                    "para que sirve",
                    "para que sirven",
                    "para qué sirve",
                    "para qué sirven",
                )
                if any(frase in mensaje_normalizado for frase in frases_de_uso):
                    return info["uso"]
                return info["explicacion"]
        temas_disponibles = ", ".join(self.temas.keys())
        return f"No tengo ese tema. Puedo explicar: {temas_disponibles}."

    def hacer_pregunta(self, mensaje_normalizado):
        tema_encontrado = None
        for tema in self.temas:
            if tema in mensaje_normalizado or tema.rstrip("s") in mensaje_normalizado:
                tema_encontrado = tema
                break
        if tema_encontrado is None:
            temas_disponibles = ", ".join(self.temas.keys())
            return f"Sobre que tema? Puedo preguntar sobre: {temas_disponibles}."
        info = self.temas[tema_encontrado]
        respuesta_estudiante = input(f"{info['pregunta']} ")
        if info["tipo"] == "numero":
            respuesta_limpia = respuesta_estudiante.strip().lower()
            respuesta_numero = 0 if respuesta_limpia == "cero" else int(respuesta_limpia)
            es_correcta = respuesta_numero == int(info["respuesta"])
        else:
            es_correcta = respuesta_estudiante.strip().lower() == info["respuesta"]
        self.temas_dominados[tema_encontrado] = es_correcta
        if es_correcta:
            return "Correcto!"
        return f"No es correcto. La respuesta era: {info['respuesta']}."

    def mostrar_progreso(self):
        if not self.temas_dominados:
            return "Todavia no has respondido ninguna pregunta."
        correctas = sum(1 for v in self.temas_dominados.values() if v)
        total = len(self.temas_dominados)
        return f"Has respondido correctamente {correctas} de {total} temas intentados."

    

    def responder(self, mensaje):
        self.historial.append(("estudiante", mensaje))
        mensaje_normalizado = mensaje.lower()
        if any(palabra in mensaje_normalizado for palabra in PALABRAS_SALIDA):
            respuesta = "Hasta luego! Sigue practicando."
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = "Hola! Soy tu tutor de Python."
        elif "progreso" in mensaje_normalizado:
            respuesta = self.mostrar_progreso()
        elif "pregunta" in mensaje_normalizado or "quiz" in mensaje_normalizado:
            respuesta = self.hacer_pregunta(mensaje_normalizado)
        elif (
            "explica" in mensaje_normalizado
            or "explicame" in mensaje_normalizado
            or any(
                tema in mensaje_normalizado or tema.rstrip("s") in mensaje_normalizado
                for tema in self.temas
            )
        ):
            respuesta = self.explicar_concepto(mensaje_normalizado)
        else:
            respuesta = "Todavia no se responder eso."
        self.historial.append(("tutor", respuesta))
        return respuesta

    def mostrar_historial(self):
            for quien, texto in self.historial:
                print(f"{quien}: {texto}")


def iniciar_conversacion(tutor):
    print("Tutor de Python - escribe 'salir' para terminar\n")
    while True:
        try:
            mensaje = input("Tu: ")
        except EOFError:
            break
        respuesta = tutor.responder(mensaje)
        print(f"Tutor: {respuesta}\n")
        if any(palabra in mensaje.lower() for palabra in PALABRAS_SALIDA):
            break
    print("--- Historial de la conversacion ---")
    tutor.mostrar_historial()


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

