class EquipamentoIndisponivelError(Exception):
    
    def __init__(self, codigo_equipamento, mensagem = "Equipamento já alugado. Tente novamente mais tarde"):
        
        self.codigo = codigo_equipamento
        self.mensagem = f'{mensagem} - Código do equipamento: {codigo_equipamento}'
        
        super().__init__(self.mensagem)

class EquipamentoInexistenteError(Exception):
    
    def __init__(self, codigo_equipamento: str, mensagem = "Equipamento não encontrado."):
        
        self.codigo = codigo_equipamento
        self.mensagem = f'{mensagem} - Código procurado: {codigo_equipamento}'

        super().__init__(self.mensagem)

class ClienteInexistenteError(Exception):
    
    def __init__(self, cpf_buscado: str, mensagem = "Cliente não cadastrado."):
        
        self.cpf = cpf_buscado
        self.mensagem = f'{mensagem} - CPF buscado: {cpf_buscado}'
        
        super().__init__(self.mensagem)

class EquipamentoNaoAlugadoError(Exception):
    
    def __init__(self, codigo, mensagem = "Não há como devolver um equipamento não alugado!"):
        
        self.codigo = codigo 
        self.mensagem = f'{mensagem} Código do equipamento: {codigo}'
        
        super().__init__(self.mensagem)
        

