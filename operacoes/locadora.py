from entidades.equipamento import Equipamento, Camera, Notebook
from entidades.cliente import Cliente
from utilitarios.exceptions import EquipamentoIndisponivelError, EquipamentoInexistenteError, ClienteInexistenteError

class Locadora():
    
    def __init__(self, nome: str):
        
        self.nome = nome 
        self._clientes = {}
        self._equipamentos = {}
    
    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:
        
        if cpf in self._clientes:
            print("Cliente com esse CPF já cadastrado!")
            return self._clientes[cpf]
        
        novo_cliente = Cliente(nome, cpf)
        
        # adiciona o cliente ao dicionário de clientes
        self._clientes[cpf] = novo_cliente
        
        print(f"\nCliente {novo_cliente.nome} adicionado com sucesso!")
        
        return novo_cliente
    
    def cadastrar_equipamento(self, nome: str, valor_diaria: float, tipo: str) -> Equipamento:
        
        if valor_diaria <= 0:
            print("Valor inválido. Por favor, digite um valor válido.")
            return 
        
        if tipo.lower() == 'camera' or tipo.lower() == 'câmera':
            novo_equipamento = Camera(nome, valor_diaria)
        
        elif tipo.lower() == 'notebook':
            novo_equipamento = Notebook(nome, valor_diaria)
        
        else:
            print("\nTipo de equipamento inválido. Escolha camera ou notebook.")
            return
        
        codigo = novo_equipamento.pegar_codigo
        
        self._equipamentos[codigo] = novo_equipamento
        print(f"\nEquipamento {nome} cadastrado com sucesso! Código: {codigo}")
        
        return novo_equipamento
    
    def alugar_equipamento(self, cpf, codigo):
        
        if cpf not in self._clientes:
            raise ClienteInexistenteError(cpf)
        
        if codigo not in self._equipamentos:
            raise EquipamentoInexistenteError(codigo)
        
        equipamento = self._equipamentos[codigo]
        
        if not equipamento.disponivel:
            raise EquipamentoIndisponivelError(codigo)
        
        cliente = self._clientes[cpf]
        
        equipamento.alugar()
        equipamento.calcular_calcao()
        
        cliente.adicionar_equipamento(equipamento)
        
        nome_equipamento = equipamento.nome
        equipamento.registrar_historico(f"Aluguel do equipamento {nome_equipamento} | Cód. {codigo}")
        
        print(f"\nEquipamento {nome_equipamento} alugado com sucesso!")
        
    def devolver_equipamento(self, cpf, codigo):
        
        if cpf not in self._clientes:
            raise ClienteInexistenteError(cpf)
        
        if codigo not in self._equipamentos:
            raise EquipamentoInexistenteError(codigo) 
        
        equipamento = self._equipamentos[codigo]
        cliente = self._clientes[cpf]
        
        if  not equipamento.disponivel and equipamento not in cliente.equipamentos_alugados:
            print(f"\nO equipamento não foi alugado por este cliente! ")
            
        else:
                
            equipamento.devolver()
            cliente.remover_equipamento(equipamento)
        
            nome_equipamento = equipamento.nome
            equipamento.registrar_historico(f"Devolução do equipamento {nome_equipamento}| Cód. {codigo}")
        
            print(f"\nEquipamento {nome_equipamento} devolvido com sucesso!")   
    
    def buscar_equipamento(self, codigo):
        
        if codigo not in self._equipamentos:
            raise EquipamentoInexistenteError(codigo)
        
        return self._equipamentos[codigo]
    