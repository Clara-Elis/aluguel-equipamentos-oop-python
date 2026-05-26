from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exceptions import EquipamentoIndisponivelError, EquipamentoNaoAlugadoError

class Equipamento(ABC):
    _total_equipamentos = 0
    
    def __init__(self, nome: str, valor_diaria: float):
        # Assim que a classe for instanciada, o total de equipamentos é incrementado
        Equipamento._total_equipamentos += 1
        self._codigo = Equipamento.get_total_equipamentos()
        self.nome = nome
        self._valor_diaria = valor_diaria
        self._disponivel = True
        self._historico = []
    
    @classmethod
    def get_total_equipamentos(cls):
        return cls._total_equipamentos
    
    @property
    def valor_diaria(self):
        return self._valor_diaria
    
    @property
    def pegar_codigo(self):
        return self._codigo
    
    @property
    def disponivel(self):
        return self._disponivel
    
    def alugar(self):
        if self._disponivel:
            self._disponivel = False
        else:
            raise EquipamentoIndisponivelError(self._codigo)
    
    def devolver(self):
        if not self._disponivel:
            self._disponivel = True
        else:
            raise EquipamentoNaoAlugadoError(self._codigo)
        
    def registrar_historico(self, mensagem):
        self._historico.append((datetime.now(), mensagem))
    
    def mostrar_historico(self):
        if not self._historico:
            print("Não há histórico de alugueis registrados.")
        else:
            for data, mensagem in self._historico:
                print(f"{data.strftime('%d/%m/%Y às %H:%M:%S')} - {mensagem}")

    @abstractmethod
    def calcular_calcao(self):
        pass
    

class Camera(Equipamento):
    
    def __init__(self, nome: str, valor_diaria: float):
        
        super().__init__(nome, valor_diaria)
    
    def calcular_calcao(self):
        valor_calcao = self._valor_diaria * 3
        print(f"O valor do calção para {self.nome} é R${valor_calcao:.2f}")

class Notebook(Equipamento):
    
    def __init__(self, nome: str, valor_diaria: float):
        
        super().__init__(nome, valor_diaria)
    
    def calcular_calcao(self):
        valor_calcao = self._valor_diaria * 5
        print(f"O valor do calção para {self.nome} é R${valor_calcao:.2f}")

