from Empleado import Empleado


class Venta():

    def __init__(self):
        self.empleado = Empleado()

    '''def detalle_Venta(self, nombre, total):
        print("Nombre: " + str(nombre) + " Sueldo: " + total)'''

    def get_Empleado(self):
        return self.empleado
