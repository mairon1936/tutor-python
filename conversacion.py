from tutor import PALABRAS_SALIDA, TutorPython


def iniciar_conversacion(tutor: TutorPython):
    print("Tutor de Python - escribe 'salir' para terminar\n")
    while True:
        try:
            mensaje = input("Tu: ")
        except EOFError:
            break
        respuesta = tutor.responder(mensaje)
        print(f"Tutor: {respuesta}\n")
        if tutor.quiz_terminado or any(
            palabra in mensaje.lower() for palabra in PALABRAS_SALIDA
        ):
            break
    print("--- Historial de la conversacion ---")
    tutor.mostrar_historial()