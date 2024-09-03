class Calificacion:
    def __init__(self):
        self.calificacion_numerica = 0.0
        self.calificacion_literal = ""

    def ingresar_datos(self):
        self.calificacion_numerica = float(input("Ingrese la calificación numérica: "))

    def asignar_calificacion_literal(self):
        if self.calificacion_numerica > 9.0:
            self.calificacion_literal = "A Excelente"
        elif self.calificacion_numerica > 8.0:
            self.calificacion_literal = "B Muy bien"
        elif self.calificacion_numerica >= 7.5:
            self.calificacion_literal = "C Bien"
        else:
            self.calificacion_literal = "R Reprobado"

    def mostrar_calificacion(self):
        print(f"La calificación literal es: {self.calificacion_literal}")


# Ejemplo de uso
calificacion = Calificacion()
calificacion.ingresar_datos()
calificacion.asignar_calificacion_literal()
calificacion.mostrar_calificacion()
