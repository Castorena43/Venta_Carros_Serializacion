from Venta import Venta
from pickle import Pickler
import pickle


class Interfaz():

    def __init__(self):
        self.venta = Venta()


    def Ingresar_Carro(self):
        opcion = ""
        while True:
            opcion = input("Vendio un carro? ")
            if opcion == "si":
                self.venta.get_Empleado().get_carro().set_modelo(input("Ingresa el modelo: "))
                self.venta.get_Empleado().get_carro().set_precio(int(input("Ingresa el precio: ")))
                self.venta.get_Empleado().get_carro().Guardar_Carro()
            else:
                break

    def Ingresar_Empleado(self):
        opcion = ""
        while True:
            opcion = input("Agregar empleado: ")
            if opcion == "si":
                self.venta.get_Empleado().set_nombre(input("Ingresa el nombre: "))
                self.Ingresar_Carro()
                self.venta.get_Empleado().set_bono()
                self.venta.get_Empleado().set_comision()
                self.venta.get_Empleado().set_sueldoTotal()
                self.venta.get_Empleado().set_empleado()
            else:
                break
        '''print(self.venta.get_empleados())'''

    def Mostrar_nomina(self):
        for empleado in self.venta.get_Empleado().get_empleado():
            print('Nombre: ' + empleado['nombre'] + '    Sueldo Total: ' + str(empleado['Sueldo_Total']))

    def Serializar(self):
        self.opcion = input("Quieres cargar los archivos")
        if self.opcion == "si":
            with open('pickled_file.pickle', 'wb') as f:
                # Pickle the 'data' dictionary using the highest protocol available.
                pickle.dump(self.venta.get_Empleado().get_empleado(), f, pickle.HIGHEST_PROTOCOL)

    def Deserializar(self):
        if self.opcion == "si":
            with open('pickled_file.pickle', 'rb') as f:
                # The protocol version used is detected automatically, so we do not
                # have to specify it.
                data = pickle.load(f)
            print(data)
