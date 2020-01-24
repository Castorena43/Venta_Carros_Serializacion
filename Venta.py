from Empleado import Empleado
import pickle


class Venta():

    def __init__(self):
        self.empleado = Empleado()


    '''def detalle_Venta(self, nombre, total):
        print("Nombre: " + str(nombre) + " Sueldo: " + total)'''

    def get_Empleado(self):
        return self.empleado

    def Mostrar_nomina(self,lista):
        for empleado in lista:
            print('Nombre: ' + empleado['nombre'] + '    Sueldo Total: ' + str(empleado['Sueldo_Total']))

    def Serializar(self):
        opcion = input("Quieres guardar los archivos")
        if opcion == "si":
            with open('pickled_file.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(self.empleado.get_empleado(), f, pickle.HIGHEST_PROTOCOL)

    def Deserializar(self):
        opcion = input("Quieres ver los archivos")
        if opcion == "si":
            with open('pickled_file.pickle', 'rb') as f:
                # The protocol version used is detected automatically, so we do not
                # have to specify it.
                data = pickle.load(f)

            self.Mostrar_nomina(data)
