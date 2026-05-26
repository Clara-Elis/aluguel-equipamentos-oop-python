class Cliente():
    
    def __init__(self, nome: str, cpf: str):
        
        self.nome = nome
        self.cpf = cpf
        self.equipamentos_alugados = []
    
    def adicionar_equipamento(self, equipamento):
        self.equipamentos_alugados.append(equipamento)
    
    def remover_equipamento(self, equipamento):
        self.equipamentos_alugados.remove(equipamento)
    
    def __str__(self):
        return f'Cliente: {self.nome} - CPF: {self.cpf}'
    