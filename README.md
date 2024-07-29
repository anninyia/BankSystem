# <span style = "color: #FFFFFF; font-size 40px; font-family: 'Cascadia Code', monospace; font-style: italic"> Sistema Bancário em Python </span>


## <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent"> Descrição </span>

Este projeto tem como objetivo implementar um sistema bancário simples em Python, utilizando uma <span style="color: #ee15ba">abordagem procedural</span>. As funcionalidades principais incluem operações de <span style="color: #ee15ba">CRUD (Create, Read, Update, Delete)</span>,<span style="color: #ee15ba"> saques</span>, <span style="color: #ee15ba">depósitos</span>,<span style="color: #ee15ba"> transferências</span>, <span style="color: #ee15ba"> consulta de saldo</span> e <span style="color: #ee15ba"> visualização de extratos de transações</span>. Além disso, o sistema permite <span style="color: #ee15ba">autenticação de usuários</span> e <span style="color: #ee15ba">armazenamento persistente de contas</span> em um arquivo `json`.

## <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent"> Funcionalidades </span>
- <span style = "color: #d34ae3"> **Criar Conta:** </span> Permite criar uma nova conta bancária com um número de conta e PIN gerados automaticamente.
- <span style = "color: #d34ae3"> **Consultar Conta:** </span> Visualiza informações detalhadas de uma conta específica.
- <span style = "color: #d34ae3"> **Atualizar Conta:** </span> Atualiza o nome, o PIN, a data de nascimento ou CPF do titular da conta.
- <span style = "color: #d34ae3"> **Deletar Conta:** </span> Remove uma conta do sistema, com confirmação de PIN.
- <span style = "color: #d34ae3"> **Autenticação:** </span> Verifica a identidade do usuário usando o número da conta e PIN.
- <span style = "color: #d34ae3"> **Saque:** </span> Permite realizar saques de uma conta autenticada.
- <span style = "color: #d34ae3"> **Depósito:** </span> Permite realizar depósitos em uma conta autenticada.
- <span style = "color: #d34ae3"> **Transferência:** </span> Transfere fundos entre duas contas diferentes.
- <span style = "color: #d34ae3"> **Consultar Saldo:** </span> Exibe o saldo atual da conta autenticada.
- <span style = "color: #d34ae3"> **Extrato de Transações:** </span> Exibe um histórico de todas as transações realizadas na conta.

## <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Requisitos do Sistema </span>

- Python 3.x
- Biblioteca `json`
- Arquivo `contas.json` no mesmo diretório que o script `BankSystem.py`

### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent"> Instruções de Execução </span>

### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Passo 1: Clonar o Repositório </span>

```sh
git clone https://github.com/anninyia/BankSystem.git
cd BankSystem
```

### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Passo 2: Garantir que o arquivo contas.json está no mesmo diretório </span>

Certifique-se de que o arquivo contas.json está presente no diretório onde o script BankSystem.py está localizado. Se não existir, crie um arquivo vazio com esse nome:

```sh
touch contas.json
```
### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Passo 3: Executar o Script </span>

No terminal, execute o script usando o Python 3:

```sh
python3 BankSystem.py
```
### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Passo 4: Usar o Sistema </span>

Siga as instruções no terminal para navegar pelo menu do sistema bancário.

### <span style = "color: #d34ae3; font-size 30px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent"> Exemplos de Uso </span>


### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Criar uma Conta </span>

- Escolha a opção "1. Criar uma nova conta" no menu inicial.
- Insira as informações solicitadas: nome completo, data de nascimento, CPF e saldo inicial.
- O sistema fornecerá o número da conta e o PIN.

### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Autenticar e Realizar Operações </span>

- Escolha a opção "2. Acessar uma conta existente" no menu inicial.
- Insira o número da conta e o PIN.
- Após a autenticação, escolha entre as opções disponíveis (sacar, depositar, transferir, consultar saldo, atualizar conta, deletar conta, gerar extrato).

### <span style = "color: #d34ae3; font-size 20px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent">Consultar Extrato </span>

- Após autenticar a conta, escolha a opção "7. Gerar Extrato" no menu principal.
- O sistema exibirá todas as transações realizadas na conta.

# <span style = "color: #d34ae3; font-size 30px; font-family: 'Cascadia Code', monospace; font-style: italic; background: linear-gradient(to right, #d34ae3, white); -webkit-background-clip: text; color: transparent"> Contato </span>
Para dúvidas ou mais informações, peço para que entre em contato pelo e-mail annavictoriagoncalvesmarciano@gmail.com e, caso eu não responda em até 3 dias úteis, me envie novamente o e-mail(sabem como é, muita coisa, muitas obrigações e muitos e-mails para responder e ordenar hehe. De antemão, já peço perdão por qualquer problema).

Espero que goste do sistema! Qualquer feedback é bem-vindo! 😊

</span>
