from Carro import Carro


class Empleado:

    def __init__(self):
        self.empleado = []
        self.nombre = ""
        self.sueldo = 2000
        self.bono = 0
        self.comision = 0
        self.carro = Carro()
        self.sueldo_total = 0

    def set_sueldoTotal(self):
        self.sueldo_total = self.sueldo+self.bono+self.comision

    def set_empleado(self, data = []):
        if len(data)==0:
            self.empleado.append({'nombre':self.nombre,'sueldo':self.sueldo,
                              'bono':self.bono,'comision':self.comision,
                              'Sueldo_Total': self.sueldo_total,'carros':self.carro.get_carro()})
        else:
            self.empleado.append(data)
        self.carro.borrarCarro()

    def get_empleado(self):
        return self.empleado

    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def get_sueldo(self):
        return self.sueldo

    def set_bono(self):
        cantidad = len(self.carro.get_carro())
        self.bono = cantidad * 1000

    def get_bono(self):
        return self.bono

    def set_comision(self):
        total = 0

        for x in self.carro.get_carro():
            total += (x['precio'])
        self.comision = total * .02

    def get_comision(self):
        return self.comision

    def get_carro(self):
        return self.carro