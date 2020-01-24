class Carro():

    def __init__(self):
        self.carro = []
        self.modelo = ""
        self.precio = 0

    def set_precio(self,precio):
        self.precio = precio

    def get_precio(self):
        return self.precio

    def set_modelo(self,modelo):
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def Guardar_Carro(self):
        self.carro.append({'modelo':self.modelo,'precio':self.precio})

    def borrarCarro(self):
        self.carro = []

    def get_carro(self):
        return self.carro


