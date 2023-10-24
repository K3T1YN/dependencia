class Eletrodomestico:
    def __init__(self, ligado, voltagem, consumo):
        self.ligado = ligado
        self.voltagem = voltagem
        self.consumo = consumo
    

    def set_valorVoltagem(self, voltagem):
        self.voltagem = voltagem

    def get_valorVoltagem(self, voltagem):
        return voltagem
        
    def set_valorConsumo(self, consumo):
        self.voltagem = consumo

    def get_valorConsumo(self, consumo):
        return consumo

e = Eletrodomestico(True, 220, 100)
e.set_valorVoltagem(500)
print(e.get_valorVoltagem())
e.set_valorConsumo(100)
print(e.get_valorConsumo())
    
        


