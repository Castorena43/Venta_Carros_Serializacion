from Venta import Venta
from pickle import Pickler



class Interfaz():

    def __init__(self):
        self.venta = Venta()

    def Run(self):
        self.venta.Deserializar()
        self.Ingresar_Empleado()
        self.venta.Mostrar_nomina(self.venta.get_Empleado().empleado)
        self.venta.Serializar()



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


