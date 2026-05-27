# Sistema de Locação de Equipamentos com Python e Orientação a Objetos

Mini projeto desenvolvido em Python para praticar Programação Orientada a Objetos, organização em módulos e tratamento de exceções personalizadas.

## Objetivo

O objetivo do projeto é simular um sistema simples de locação de equipamentos, permitindo cadastrar clientes, cadastrar equipamentos, alugar, devolver e consultar o histórico de locações.

## Conceitos praticados

- Classes e objetos
- Herança
- Classe abstrata
- Método abstrato
- Polimorfismo
- Composição/agregação
- Encapsulamento por convenção
- Dicionários armazenando objetos
- Listas de objetos
- Exceções personalizadas
- Tratamento de erros com try/except
- Organização em módulos

## Funcionalidades

- Adicionar cliente
- Cadastrar equipamento
- Alugar equipamento
- Devolver equipamento
- Ver histórico de equipamento
- Tratar erros como:
  - cliente inexistente
  - equipamento inexistente
  - equipamento indisponível
  - equipamento não alugado
  - entradas inválidas

## Estrutura do projeto

```text
.
├── entidades/
│   ├── cliente.py
│   └── equipamento.py
├── operacoes/
│   └── locadora.py
├── utilitarios/
│   └── exceptions.py
├── menu_principal.py
└── .gitignore
```

## Como executar

No terminal, dentro da pasta do projeto, execute:
```bash 
python menu_principal.py
```

`python` executa o interpretador Python.
`menu_principal.py` é o arquivo principal do sistema.