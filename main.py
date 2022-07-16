import cliente

inforcliente=[]

verificar=0
print('seja bem vindo ao cadastro  e informaçoes de clientes de clientes!')


verificar=int(input('DIGITE (1) PARA CADASTRAR NOVO CLIENTE OU (2) PARA ACESSAR DADOS DE CLIENTES JA CADASTRADO E (3) PARA PARA:'))


while(verificar!=3):
 if verificar==1:
    p1=input('digite o nome completo:')
    datap1=input('data de nascimento:')
    cpfp1=input('CPF:')
    emailp1=input('email:')
    endereçop1=input('endereço:')

print('FIM DE CADASTRO!')
print('PRECIONE (1) PARA CONTINUAR INFORMARNDO NOVO CLIENTE, PRECIONE (2)')


obejecttonome=cliente.Cliente(p1)
objectdatatap1=cliente.Cliente(datap1)
objectcpfp1=cliente.Cliente(cpfp1)
objectemailp1=cliente.Cliente(emailp1)
objectendereço=cliente.Cliente(endereçop1)

objetocliente=cliente.Cliente('self' 'nomecli', 'datanascimento', 'cpf', 'email', 'endereço', 'divida')





