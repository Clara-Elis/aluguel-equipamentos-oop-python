from operacoes.locadora import Locadora
from utilitarios.exceptions import ClienteInexistenteError, EquipamentoIndisponivelError, EquipamentoInexistenteError, EquipamentoNaoAlugadoError
from entidades.equipamento import Equipamento
def menu_principal():
    
    print(f"\n--- Sistema de Locação de Equipamentos ---\n")
    print("1. Adicionar Cliente")
    print("2. Cadastrar Equipamento")
    print("3. Alugar Equipamento")
    print("4. Devolver Equipamento")
    print("5. Ver Histórico de Equipamento")
    print("6. Sair")
    
    return input("Digite a opção desejada: ")

def main():
    
    minha_locadora = Locadora("Minha Locadora")
    
    while True:
    
        opcao = menu_principal()
    
        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o cpf do cliente: ")
        
            minha_locadora.adicionar_cliente(nome, cpf)
    
        elif opcao == '2':
            
            nome = input("Digite o nome do equipamento: ")
        
            try:
                valor_diaria = float(input("Digite o valor da diária: R$"))
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue
            
            tipo = input("Escolha o tipo de equipamento: camera ou notebook: ")    
        
            minha_locadora.cadastrar_equipamento(nome, valor_diaria, tipo)
    
        elif opcao == '3':
        
            cpf = input("Digite o CPF do cliente: ")
            try:
                codigo = int(input("Digite o código do equipamento: "))
            
                minha_locadora.alugar_equipamento(cpf, codigo)
            
            except ClienteInexistenteError as e:
                print(f"Erro: {e}")
            
            except EquipamentoInexistenteError as e:
                print(f"Erro: {e}")
            
            except EquipamentoIndisponivelError as e:
                print(f"Erro: {e}")
                
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue
    
        elif opcao == '4':
            
            cpf = input("Digite o CPF do cliente: ")
            
            try: 
                codigo = int(input("Digite o código do equipamento: "))
           
                minha_locadora.devolver_equipamento(cpf, codigo)
            except ClienteInexistenteError as e:
                print(f"Erro: {e}")
            except EquipamentoInexistenteError as e:
                print(f"Erro: {e}")
            except EquipamentoNaoAlugadoError as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue
        
        elif opcao == '5':
            
            try:
            
                codigo = int(input("Digite o código do equipamento: "))
                equipamento = minha_locadora.buscar_equipamento(codigo)
                equipamento.mostrar_historico()
                
            except EquipamentoInexistenteError as e:
                print(f"Erro: {e}")
                
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue
            
        elif opcao == '6':
            print("Obrigado por usar o sistema. Tchau!")
            break
        
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    main()
