from BUSCAS import *
from Historico import *
import sys
import os

os.chdir("Arquivos")


# CRIAR GERENTE ---------------------------------------------------------------------//
def criar_geren():
     print("»CADASTRO GERENTE\n")
     user = input("Informe o USER: ")
     if len(user) == 0:
          print("ERRO! Entrada vazia, tente novamente.")
          print('-'*95)
          criar_geren()
     else:
          geren_exi = busc_usuario(user+".csv")
          if geren_exi == True:
               print("O Usuário já está cadastrado.")
               print('¨'*95)
               menu_principal()
          else:
               senha = input("Informe a SENHA: ")
               if len(senha) == 0:
                    print("ERRO! Entrada vazia, tente novamente.")
                    print('-'*95)
                    criar_geren()
               else: 
                    geren = open(user+".csv", "a")
                    geren.write("G"+";"+user+";"+senha)
                    geren.write(";\n")
                    geren.close()
                    print("\nCadastro realizado com sucesso ☺!")
                    print('⊳⊲'*50)
               menu_principal()
          
# CRIAR FUNCIONÁRIO ------------------------------------------------------------------------------------//     
def criar_fun():
     print("»CADASTRO FUNCIONÁRIO\n")
     user = input("Informe o USER: ")
     if len(user) == 0:
          print("ERRO! Entrada vazia, tente novamente.")
          return criar_func()
     else:
          func_exi = busc_usuario(user+".csv")
          if func_exi == True:
               print("O Usuário já está cadastrado.")
               print('¨'*95)
               return menu_principal()
          else:
               senha = input("Informe a SENHA: ")
               if len(senha) == 0:
                    print("ERRO! Entrada vazia, tente novamente.")
                    return criar_func()
               else:
                    func = open(user+".csv", "a")
                    func.write("F"+";"+user+";"+senha)
                    func.write(";\n")
                    func.close()
                    print("\nCadastro realizado com sucesso ☺!")
                    print('⊳⊲'*50)
                    return menu_principal()

def menu_gerente(usuario):
     print("-"*95)
     print("♔Bem vindo(a) Gerente!♔".center(95))
     print("")
     print("»BUSCAS GERENTE:")
     print("➀ - Quais as 10 empresas que mais publicaram em um determinado ano, de acordo com o gênero.")
     print("➁ - Top 10 média de vendas por plataforma para uma determinada região.")
     print("➂ - Média das Vendas globais por ano, baseadas em um intervalo de anos e um gênero.")
     print("➃ - Quantidade de jogos de acordo com os “X” maiores gênero num intervalo de anos.")
     print("➄ - Vendas Globais de jogos de cada plataforma de uma determinada Publicadora.")
     print("➅ - Relação Top “X” de jogos, de acordo com as vendas em NA e EU.")
     print("➆ - Taxas de vendas por região, de jogos vendidos em um determinado ano, ordenados por maior PIB.")
     print("➇ - Exibir Histórico de Buscas.")
     print("➈ - Voltar ao MENU.")
     print("")

     menugerente = input("Informe o número da busca desejada:\n► ")
     if menugerente == "1":
          print("-"*95)
          busca2(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "2":
          print("-"*95)
          busca3(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "3":
          print("-"*95)
          busca5(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "4":
          print("-"*95)
          busca6(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "5":
          print("-"*95)
          busca7(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "6":
          print("-"*95)
          busca8(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "7":
          print("-"*95)
          busca11(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "8":
          print("-"*95)
          verHistorico(usuario)
          return menu_gerente(usuario)
          
     elif menugerente == "9":
          print("-"*95)
          return menu_principal()
     
     else:
          print("Opção inválida, tente novamente.".center(95))
          print('-'*95)
          return menu_gerente(usuario)

def menu_funcionario(usuario):
     print("-"*95)
     print("♘Bem vindo(a) Funcionário(a)!♘".center(95))
     print("")
     print("»BUSCAS FUNCIONÁRIO:")
     print("➀ - Quais as 10 empresas que mais publicaram em um determinado ano, de acordo com o gênero.")
     print("② - Média das Vendas globais por ano, baseadas em um intervalo de anos e um gênero.")
     print("➂ - Relação Top “X” de jogos, de acordo com as vendas em NA e EU.")
     print("➃ - Taxas de vendas por região, de jogos vendidos em um determinado ano, ordenados por maior PIB.")
     print("➄ - Exibir Histórico de Buscas.")
     print("➅ - Voltar ao MENU.")
     print("")

     menufuncionario = input("Informe o número da busca desejada:\n► ")
     
     if menufuncionario == "1":
          print("-"*95)
          busca2(usuario)
          return menu_funcionario(usuario)
          
     elif menufuncionario == "2":
          print("-"*95)
          busca5(usuario)
          return menu_funcionario(usuario)
          
     elif menufuncionario == "3":
          print("-"*95)
          busca8(usuario)
          return menu_funcionario(usuario)
          
     elif menufuncionario == "4":
          print("-"*95)
          busca11(usuario)
          return menu_funcionario(usuario)

     elif menufuncionario == "5":
          print("-"*95)
          verHistorico(usuario)
          return menu_funcionario(usuario)
          
     elif menufuncionario == "6":
          print("-"*95)
          return menu_principal()
     
     else:
          print("Opção inválida, tente novamente.".center(95))
          print('-'*95)
          return menu_funcionario(usuario)
     
     #entrar gerente ----------------------------------------------------------------------------//
def enter_usuario():
     print("»LOGIN\n")
     user = input("⇀USUÁRIO: ")
     if len(user) == 0:
          print("ERRO! Entrada vazia, tente novamente.")
          print("-"*95)
          return enter_usuario()
     else:
          user_exi = busc_usuario(user+".csv")
          if user_exi == False:
               print("O Usuário NÃO existe.")
               print('¨'*95)
               return menu_principal()
          else:
               arq = open(user+".csv")
               for linha in arq:
                    dados = linha.split(';')
                    if dados[0] == "G":                    
                         senha = input("⇀SENHA: ")
                         if len(senha) == 0:
                              print("ERRO! Entrada vazia, tente novamente.")
                              print("-"*95)
                              arq.close()
                              return enter_usuario()
                         else:
                              if dados[2] == senha:
                                   arq.close()
                                   menu_gerente(user+".csv")
                                        
                              else:
                                   print("SENHA INCORRETA! Tente novamente.")
                                   print('×'*95)
                                   arq.close()
                                   return menu_principal()
                         
                    elif dados[0] == "F":
                         senha = input("⇀SENHA: ")
                         if len(senha) == 0:
                              print("ERRO! Entrada vazia, tente novamente.")
                              print("-"*95)
                              arq.close()
                              return enter_usuario()
                         else:
                              if dados[2] == senha:
                                   arq.close()
                                   menu_funcionario(user+".csv")
                              else:
                                   print("SENHA INCORRETA! Tente novamente.")
                                   print('×'*95)
                                   arq.close()
                                   return menu_principal()
               
               
     
def busc_usuario(user):
     return os.path.exists(user)  #verificar usuário ----------//

     # REMOVER USUÁRIO -----------------------------------------------------------------//               
def remover_usu():
     print("»EXCLUIR USUÁRIO.\n")
     user = input("⇀USUÁRIO: ")
     if len(user) == 0:
          print("ERRO! Entrada vazia, tente novamente.")
          print("-"*95)
          return remover_usu()
     else:
          user_exi = busc_usuario(user+".csv")
          if user_exi == False:
               print("O Usuário NÃO existe.")
               print('¨'*95)
               return op_avancadas()
          else:
               arq = open(user+".csv")
               for linha in arq:
                    dados = linha.split(';')  #separando o arq em ","
                    passw = input("⇀SENHA: ")
                    if len(passw) == 0:
                         print("ERRO! Entrada vazia, tente novamente.")
                         print("-"*95)
                         return remover_usu()
                    else:
                         if dados[2] == passw:  #local senha
                              arq.close()
                              confirmar = int(input("\nVocê realmente deseja Excluir o Usuário?\n➀ - NÃO\n➁ - SIM\n► "))
                              if confirmar == 1:
                                   print("¨"*95)
                                   return menu_principal()
                              elif confirmar == 2:
                                   os.remove(user+".csv")
                                   print ("Usuário removido com sucesso!".center(60,'='))
                                   return menu_principal()
                              else:
                                   print("Opção inválida, tente novamente.".center(80))
                                   print('-'*95)
                                   return op_avancadas()
                         else:
                              print("SENHA INCORRETA! Tente novamente.")
                              print('×'*95)
                              return op_avancadas()
               
     #OPÇÕES AVANÇADAS -------------------------------------------------------------------------------------//   
def op_avancadas():
     print("»OPÇÕES AVANÇADAS.\n")
     print("➀ - Excluir Usuário.")
     print("➁ - Contatos e Informações.")
     print("➂ - Voltar ao MENU.\n")
     print("Digite o número da opção desejada:")
     submenu_ = input("► ")
     print("-"*95)
     if submenu_ == '1':
          remover_usu()
          
     elif submenu_ == '2':
          print("»CONTATOS E INFORMAÇÕES\n")
          print("⌳TELEFONE PARA CONTATO:\n☏(81)1234-4568\n")
          print("⌳EMAIL:\n✉uag-games@ufrpe.com\n")
          print("⌳CRIADORA:\n☞Emily Souza de Almeida Santos.\n")
          print("⌳DISCIPLINA:\n⌨Introdução à Programação.\n\n⌳PROFESSOR:\n☞Luis Filipe Alves Pereira.")
          print("⟨ BCC - UAG / 2018.2 ⟩".center(95))
          print("")
          menu_ = input("➀ - Voltar ao MENU.\n► ")
          if menu_ == '1':
               print("-"*95)
               return menu_principal()
          else:
               print("Opção inválida, tente novamente.".center(95))
               print('-'*95)
               return op_avancadas()
          
     elif submenu_ == '3':
          return menu_principal()
          
     else:
          print("Opção inválida, tente novamente.".center(95))
          print('-'*95)
          return op_avancadas()

     #LOGIN ---------------------------------------------------------------------------------------//
def login_menu():
     enter_usuario()
                   
          
def menu_principal():
     ok = True
     while ok == True:

         # Menu Inicio ---------------------------------------------------------------------------------------------//
          print("»MENU")
          print("\n➀ - Cadastro de Usuário.")
          print("➁ - Login.")
          print("➂ - Opções Avançadas.")
          print("➃ - Sair.\n")
                  
          menuop = input("Digite o número da opção desejada:\n► ")
          print('-'*95)
          
          #menu cadastro -----------------------------------------------------------------------------------------//
          if menuop == '1':
               print("»CADASTRO DE USUÁRIO.")
               print("\n➀ - Cadastrar como Gerente.")
               print("➁ - Cadastrar como Funcionário.")
               print("➂ - Voltar ao MENU.\n")
               print("Digite o número da opção desejada:")
               submenu = input("► ")
               print("-"*95)
               if submenu == '1':
                    criar_geren()
                    
               elif submenu == '2':
                    criar_fun()
                    
               elif submenu == '3':
                    return menu_principal()
               
               else:
                    print("Opção inválida, tente novamente.".center(80))
                    print('-'*95)
                    return menu_principal()

           
          if menuop == '2':
               login_menu()

          elif menuop == '3':
               op_avancadas() 
                
              # Fecha Programa -----------------------------------------------------------------------------------------//
          elif menuop == '4':
               print("")
               print(" VOLTE SEMPRE! ".center(95,"ᛃ"))
               ok = False
               sys.exit()
               
          else:
               print("Opção inválida, tente novamente.".center(80))
               print('-'*95)
               return menu_principal()             
                    

 #INICIO------------------------------------------------------------------------------------//                   
print("♠ ♣ ♦ ♥ "*12)
print("")
print("SEJA BEM VINDO(A) AO BANCO DE DADOS UAG - GAMES™".center(95))
print("")
print("♠ ♣ ♦ ♥ "*12)
menu_principal()
