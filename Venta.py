from Empleado import Empleado
import pickle
import os.path as path


class Venta():

    def __init__(self):
        self.empleado = Empleado()

    def get_Empleado(self):
        return self.empleado

    def Mostrar_nomina(self,lista):
        for empleado in lista:
            print('Nombre: ' + empleado['nombre'] + '    Sueldo Total: ' + str(empleado['Sueldo_Total']))

    def Serializar(self):
        opcion = input("Quieres guardar los archivos")
        if opcion == "si":
            with open('data.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(self.empleado.get_empleado(), f, pickle.HIGHEST_PROTOCOL)

    def Deserializar(self):
        if path.exists('data.pickle'):
            with open('data.pickle', 'rb') as f:
                # The protocol version used is detected automatically, so we do not
                # have to specify it.
                data = pickle.load(f)
                if data:
                    for x in data:
                        self.empleado.set_empleado(x)
                    self.Mostrar_nomina(data)
        else:
            file = open('data','wb')
            file.close()