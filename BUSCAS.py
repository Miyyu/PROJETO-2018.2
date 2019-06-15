import matplotlib.pyplot as plt
import Historico
from matplotlib import style

def print_cash():
     print("\n⊰ A busca com esses parâmetros já foi realizada antes.\nExibiremos os dados armazenados em cash. ⊱")
     print("-"*95)

def receberNum3(nome):
     print("\n∽Quantidade de Jogos Disponíveis: De 1 a 16598.∽\n")
     numero = input(nome)
     try:
          numero3 = int(numero)
          if numero3 < 1 or numero3 > 16598:
               print("Entrada inválida, limite de jogos excedido. Digite novamente.")
               print('¨'*95)
               return receberNum3(nome)
          else:
               return numero3
     except:
          print ("Entrada inválida, digite novamente.")
          print('¨'*95)
          return receberNum3(nome)
     

def receberNum2(nome):
     print("\n∽Quantidade de Gêneros Disponíveis: De 1 a 12.∽\n")
     numero = input(nome)
     try:
          numero2 = int(numero)
          if numero2 < 1 or numero2 > 12:
               print("Entrada inválida, limite de gêneros excedido. Digite novamente.")
               print('¨'*95)
               return receberNum2(nome)
          else:
               return numero2
     except:
          print ("Entrada inválida, digite novamente.")
          print('¨'*95)
          return receberNum2(nome)

def receberAno(nome):
     print("\n∽Anos Disponíveis: De 1980 a 2017.∽\n")
     print ("Digite o Ano"+nome)
     valor = input("► ")
     try:
          valor2 = int(valor)
          if valor2 < 1980 or valor2 > 2017:
               print ("Entrada inválida, limite de anos excedido. Digite novamente.")
               print('¨'*95)
               return receberAno(nome)
          else:
               return valor2
     except:
          print ("Entrada inválida, digite novamente.")
          print('¨'*95)
          return receberAno(nome)
     
def inputAno():
     var = True
     while var:
          ano1 = receberAno(" Inicial: ")
          ano2 = receberAno(" Final: ")
          genero = generos()
          if ano1 > ano2:
               print("Entrada inválida, digite novamente.")
               print('¨'*95)
          else:
               var = False
               
     return ano1, ano2, genero

def generos():
     var = True
     lista = ["Sports","Platform","Racing","Role-Playing","Puzzle","Misc","Shooter","Simulation","Action","Fighting","Adventure","Strategy"]
     print("\n∽Gêneros Disponíveis: Sports, Platform, Racing, Role-Playing, Puzzle, Misc, Shooter, Simulation, Action,\nFighting, Adventure e Strategy.∽\n")
     while var:
          nome = input("Digite o gênero desejado:\n► ")
          nome2 = string2(nome)
          if nome2 in lista:
               var = False
          else:
               print ("O gênero solicitado não faz parte do Banco de Dados. Tente novamente.")
               print('¨'*95)
     return nome2

def existenciaElemento(lista, elemento1,elemento2):
     for i in range(len(lista)):
          if elemento1 == int (lista[i][0]):
               for j in range (1,len(lista[i])):
                    if elemento2 == lista[i][j][0]:
                         return True, i, j
     return False, 0, 1

def existenciaElemento2 (lista, elemento):
     for i in range(len(lista)):
          if lista[i][0] == elemento:
               return True, i
     return False, 0

def media(lista1, lista2):
     var = []
     for k in range(len(lista1)):
          var.append(lista1[k]/lista2[k])
     return var

def appends(aux1, aux2):
     lista = []
     for j in range(len(aux1)):
          aux = []
          aux.append(aux1[j])
          aux.append(aux2[j])
          lista.append(aux)
          
     return lista


def fun(lista_bid, genero):
     for i in range(len(lista_bid)):
          if lista_bid[i][0] == genero:
               return True, i
     return False, 0

def string(nome):
     return nome.upper()

def string2(nome):
     return nome.title()

def nomeRegiao ():
     regiao = input("Digite a região desejada (Ex: NA, EU, JP, Outros, Mundial):\n► ")
     regiao_for = string(regiao)

     if regiao_for != "NA" and regiao_for != "EU" and regiao_for != "JP" and regiao_for != "OUTROS" and regiao_for != "MUNDIAL":
          print("Entrada inválida, digite novamente.")
          print('¨'*95)
          return nomeRegiao ()
     else:
          return regiao_for

def indicie_e_nome_reg(regiao):
     if regiao == "NA":
          return 6, "NA_Sales"
     elif regiao == "EU":
          return 7, "EU_Sales"
     elif regiao == "JP":
          return 8, "JP_Sales"
     elif regiao == "OUTROS":
          return 9, "Other_Sales"
     elif regiao == "MUNDIAL":
          return 10, "Global_Sales\n"


def busca2(usuario):

     ano = receberAno(": ")
     genero = generos()
     existencia, lista2 = Historico.cashB2("Busca_2",ano,genero,usuario)

     if existencia == False:
          dados = open("vgsales.csv","r")
          
          dicto = {}

          lin = True

          for linha in dados:
               linhas = linha.split(",")
               if linhas[3] != "Year" and linhas[3] != "N/A":
                    if int(linhas[3]) == ano:
                         if linhas[4] == genero:
                              if lin == True:
                                   dicto[linhas[5]] = 1
                                   lin = False
                              else:
                                   if linhas[5] not in  dicto:
                                        dicto[linhas[5]] = 1
                                   else:
                                        dicto[linhas[5]] += 1
          dados.close()
          
          lista = list(dicto.items())
          lista2 = sorted(lista, key = lambda x:x[1], reverse = True)
          Historico.historico_B2("Busca_2",ano,genero,lista2,usuario)
     else:
          print_cash()
          Historico.historico_B2("Busca_2",ano,genero,lista2,usuario)
     

     style.use("dark_background")
     plt.xlabel("PUBLICAÇÕES", size = 14)
     plt.ylabel("EMPRESAS", size = 14)
     plt.title("EMPRESAS x PUBLICAÇÕES\nAno: {}.         Gênero: {}.".format(ano, genero))
     if len(lista2) < 10:
          for i in range(len(lista2)):
               plt.barh(lista2[i][0], lista2[i][1], color = "c")
     else:
          for i in range(10):
               plt.barh(lista2[i][0], lista2[i][1], color = "c")
     plt.show()
               
def busca3(usuario):
     
     

     regiao = nomeRegiao ()
     j,nome_reg = indicie_e_nome_reg(regiao)

     existencia,master2 = Historico.cashB3_B7("Busca_3",regiao,usuario)

     if existencia == False:
          dados = open("vgsales.csv","r")
          
          plataformas = []
          vendasNA = []
          quantidadeJ = []
          medias = []
          master = []

          for linha in dados:
               linhas = linha.split(",")
               if linhas[j] != nome_reg:
                    if linhas[2] in plataformas:
                         for i in range(len(plataformas)):
                              if plataformas[i] == linhas[2]:
                                   vendasNA[i] += float(linhas[j])
                                   quantidadeJ[i] += 1
                    else:
                         plataformas.append(linhas[2])
                         vendasNA.append(float(linhas[j]))
                         quantidadeJ.append(1)
          dados.close()

          for i in range(len(plataformas)):
               medias.append(vendasNA[i]/quantidadeJ[i])

          for j in range(len(plataformas)):
               aux = []
               aux.append(plataformas[j])
               aux.append(medias[j])
               master.append(aux)
          
          master2 =  sorted(master, key=lambda x : x[1],reverse = True)

          Historico.historico_B3_B7("Busca_3",regiao,master2,usuario)

     else:
          print_cash()
          Historico.historico_B3_B7("Busca_3",regiao,master2,usuario)

     style.use("dark_background")

     for k in range(10):
          plt.scatter(master2[k][0],master2[k][1], color = "r" )
     plt.xlabel("PLATAFORMA", size = 14)
     plt.ylabel("MÉDIA", size = 14)
     plt.title("MÉDIA x PLATAFORMA\nRegião {}.".format(regiao))
     plt.show()

def busca5(usuario):
     
     anoInicial, anoFinal, genero= inputAno()

     existencia,ano_ordem,media_ordem = Historico.cashB5_B6("Busca_5",anoInicial,anoFinal,genero,usuario)

     if existencia == False:
          dados = open("vgsales.csv","r")
          
          ano = []
          vendas = []
          jogos = []
          ano_ordem = []
          media_ordem = []

          for linha in dados:
               linhas = linha.split(",")
               if linhas[3] != "Year" and linhas[3] != "N/A":
                    if int(linhas[3]) >= anoInicial and int(linhas[3]) <= anoFinal:
                         if linhas[4] == genero:
                              if linhas[3] not in ano:
                                   ano.append(linhas[3])
                                   vendas.append(float(linhas[10]))
                                   jogos.append(1)
                              else:
                                   for i in range(len(ano)):
                                        if linhas[3] == ano[i]:
                                             vendas[i] += float(linhas[10])
                                             jogos[i] += 1
          dados.close()

          mediacalc = media(vendas,jogos)

          lista1 = appends(ano, mediacalc)
          master =  sorted(lista1, key=lambda x : x[0],reverse = False)
          
          for j in range(len(master)):
               ano_ordem.append(master[j][0])
               media_ordem.append(master[j][1])

          Historico.historico_B5_B6("Busca_5",anoInicial,anoFinal,genero,ano_ordem,media_ordem,usuario)

     else:
          print_cash()
          Historico.historico_B5_B6("Busca_5",anoInicial,anoFinal,genero,ano_ordem,media_ordem,usuario)

     style.use("dark_background")
     plt.plot(ano_ordem, media_ordem, "g-.", linewidth = 2)
     plt.xlabel("ANOS", size = 14)
     plt.ylabel("MÉDIA VENDAS", size = 14)
     plt.title("Médias de vendas Globais nos anos de {} a {}.\nGênero: {}.".format(anoInicial, anoFinal, genero))
     plt.show()

def busca6 (usuario):

     ano1 = receberAno(" Inicial: ")
     ano2 = receberAno(" Final: ")
     qttGen = receberNum2("\nDigite a quantidade de gêneros:\n► ")
     existencia, listaPlot, listaAnos = Historico.cashB5_B6("Busca_6", ano1, ano2, qttGen,usuario)

     if existencia == False:
          generosQuantidade = []
          generos = []
          anos = []
          listaPlot = []
          listaAnos = []
          
          for i in range((ano2-ano1)+1):
               listaAnos.append(ano1+i)

          dados = open ("vgsales.csv", "r")

          for linha in dados:
               linhas = linha.split(",")
               if linhas[3] != "Year" and linhas[3] != "N/A":
                    if int (linhas[3]) >= ano1 and int (linhas[3]) <= ano2:
                         if len(anos) == 0:
                              anos.append([int(linhas[3]),[linhas[4],1]])
                         else:
                              teste, i, j = existenciaElemento(anos, int(linhas[3]),linhas[4])
                              if teste == True:
                                   anos[i][j][1] += 1
                              else:
                                   anos.append([int(linhas[3]),[linhas[4],1]])
                              
          dados.close()

          dados2 = open ("vgsales.csv", "r")

          for linha in dados2:
               linhas = linha.split(",")
               if linhas[3] != "Year" and linhas[3] != "N/A":
                    if int (linhas[3]) >= ano1 and int (linhas[3]) <= ano2:
                         if len(generos) == 0:
                              generosQuantidade.append([linhas[4],1])
                              generos.append(linhas[4])
                         else:
                              teste2, i = existenciaElemento2 (generosQuantidade, linhas[4])
                              if teste2 == False:
                                   generosQuantidade.append([linhas[4],1])
                                   generos.append(linhas[4])
                              else:
                                   generosQuantidade[i][1] += 1
                                   
          dados2.close()

          
          for anos5 in listaAnos:
               for generos5 in generos:
                    flag = False
                    for k in range(len(anos)):
                        if anos[k][0] == anos5 and anos[k][1][0] == generos5:
                             flag = True
                             break
                    if flag != True:
                         anos.append([anos5,[generos5,0]])          

          generosQuantidadeOrd= sorted(generosQuantidade, key = lambda x : x[1],reverse = True)
          anos2 = sorted(anos, key=lambda x : x[0],reverse=False)

          for i in range (qttGen):
               listaPlot.append([generosQuantidadeOrd[i][0]])

          for genero in listaPlot:
               for i in range(len(anos2)):
                    for j in range(1,len(anos2[i])):
                         if genero[0] == anos2[i][j][0]:
                              genero.append(anos2[i][j][1])

          Historico.historico_B5_B6("Busca_6",ano1,ano2,qttGen,listaPlot,listaAnos,usuario)

     else:
          print_cash()
          Historico.historico_B5_B6("Busca_6",ano1,ano2,qttGen,listaPlot,listaAnos,usuario)

     style.use("dark_background")
     for i in range(len(listaPlot)):
          plt.plot(listaAnos,listaPlot[i][1:len(listaPlot[i])],label = "{}".format(listaPlot[i][0]))
     plt.xlabel("ANOS", size = 14)
     plt.ylabel("JOGOS", size = 14)
     plt.title("Quantidade de jogos de acordo com os {} maiores gêneros\n entre os anos de {} a {}.".format(qttGen,ano1,ano2))
     plt.legend()
     plt.show()

def busca7(usuario):
     
     publi = input("Digite a Publicadora que deseja saber:\n► ")
     publi_for = string2(publi)

     existencia,dicto = Historico.cashB3_B7("Busca_7",publi_for,usuario)

     if existencia == False:
          dicto = {}
          lin = True

          dados = open("vgsales.csv","r")

          for linha in dados:
               linhas = linha.split(',')
               if linhas[5] != "Publisher":
                    if linhas[5] == publi_for:
                         if lin == True:
                              dicto.update({linhas[2]:float(linhas[10])})
                              lin = False
                         else:
                              if linhas[2] in dicto.keys():
                                   for valores, values in dicto.items():
                                        if valores == linhas[2]:
                                             dicto[valores] += float(linhas[10])
                              else:
                                   dicto.update({linhas[2]:float(linhas[10])})
          dados.close()

          Historico.historico_B3_B7("Busca_7",publi_for,dicto,usuario)

     else:
          print_cash()
          Historico.historico_B3_B7("Busca_7",publi_for,dicto,usuario)

     style.use("dark_background")
     plt.bar(dicto.keys(),dicto.values(), color = "blue")
     plt.xlabel("PLATAFORMAS", size = 14)
     plt.ylabel("VENDAS", size = 14)
     plt.title("Vendas Globais de jogos da publicadora {}\nde acordo com as plataformas.".format(publi_for))
     plt.show()

def busca8(usuario):

     jogos =  receberNum3("Digite quantos jogos deseja saber:\n►")

     existencia,jogos_NA,jogos_EU = Historico.cashB8_B11("Busca_8",jogos,usuario)

     if existencia == False:
     
          dados = open("vgsales.csv", "r")
          
          jogos_EU = []
          jogos_NA = []
          for linha in dados:
              linhas = linha.split(",")
              if linhas[6] != "NA_Sales" and linhas[6] != "N/A":
                  jogos_NA.append(float (linhas[6]))
              if linhas[7] != "EU_Sales" and linhas[7] != "N/A":
                  jogos_EU.append(float(linhas[7]))
                  
          dados.close()
                         
          jogos_NA.sort(reverse = True)
          jogos_EU.sort(reverse = True)

          Historico.historico_B8_B11("Busca_8",jogos,jogos_NA[0:jogos],jogos_EU[0:jogos],usuario)

     else:
          print_cash()
          Historico.historico_B8_B11("Busca_8",jogos,jogos_NA[0:jogos],jogos_EU[0:jogos],usuario)
          
     tuplaNA = tuple(jogos_NA[0:jogos])
     tuplaEU = tuple(jogos_EU[0:jogos])

     lista = []
     for i in range(jogos):
         lista.append(i+1)

     style.use("dark_background")
     plt.plot(lista, tuplaNA, "b--", label = u"Vendas NA", linewidth = 2)
     plt.plot(lista, tuplaEU, label = u"Vendas EU", color = "orange")

     plt.xlabel("JOGOS", size = 14)
     plt.ylabel("VENDAS", size = 14)
     plt.title("Relação Top {} de jogos.\nVendas NA e EU.".format(jogos))
     plt.legend()
     plt.show()

def busca11(usuario):
     from collections import OrderedDict

     ano = receberAno(": ")

     existencia, lista1, lista2 = Historico.cashB8_B11("Busca_11",ano,usuario)

     if existencia == False:
          
          NA = []
          EU = []
          JP = []
          OTHER = []
          GLOBALL = []
          listaPlot= []

          dados = open("vgsales.csv","r")
          for linha in dados:
               linhas = linha.split(",")
               if linhas[3] != "Year" and linhas[3] != "N/A":
                    if int(linhas[3]) == ano:
                         NA.append(float(linhas[6]))
                         EU.append(float(linhas[7]))
                         JP.append(float(linhas[8]))
                         OTHER.append(float(linhas[9]))
                         GLOBALL.append(float(linhas[10]))
          dados.close()

          listaPlot.append(["NA",sum(NA)])
          listaPlot.append(["EU",sum(EU)])
          listaPlot.append(["JP",sum(JP)])
          listaPlot.append(["OTHER",sum(OTHER)])

          arquivo = open("paises.txt",encoding="utf8")
          pibNA = []
          pibEU = []
          pibJP = []
          pibOther = []

          for variaveis in arquivo:
               infor = variaveis.split(",")
               if len(infor) == 10:
                    if infor[8] == "NA":
                         pibNA.append(float(infor[1]))
                    elif infor[8] == "EU":
                         pibEU.append(float(infor[1]))
                    elif infor[0] != "Japao":
                         if infor[8] != "NA" and infor[8] != "EU":
                              pibOther.append(float(infor[1]))
                    elif infor[0] == "Japao":
                         pibJP.append(float(infor[1]))
               elif len(infor) == 9:
                    if infor[7] == "NA":
                         pibNA.append(float(infor[1]))
                    elif infor[7] == "EU":
                         pibEU.append(float(infor[1]))
                    elif infor[0] != "Japao":
                         if infor[7] != "NA" and infor[7] != "EU":
                              pibOther.append(float(infor[1]))
                    elif infor[0] == "Japao":
                         pibJP.append(float(infor[1]))
               elif len(infor) == 8:
                    if infor[6] == "NA":
                         pibNA.append(float(infor[1]))
                    elif infor[6] == "EU":
                         pibEU.append(float(infor[1]))
                    elif infor[0] != "Japao":
                         if infor[6] != "NA" and infor[6] != "EU":
                              pibOther.append(float(infor[1]))
                    elif infor[0] == "Japao":
                         pibJP.append(float(infor[1]))


          arquivo.close()
          listaOrd = []
          listaOrd.append(["NA", sum(pibNA)])
          listaOrd.append(["EU", sum(pibEU)])
          listaOrd.append(["JP", sum(pibJP)])
          listaOrd.append(["OTHER", sum(pibOther)])


          listaOrdPib = listaOrd

          for elemento in listaOrdPib:
               for elemento2 in listaPlot:
                    if elemento[0] == elemento2[0]:
                         elemento[1] = elemento2[1]

          lnome = []
          lnum = []
          lnumOrd = []
          lista1 = []
          lista2 = []
          for i in range(len(listaOrdPib)):
              lnome.append(listaOrdPib[i][0])
              lnum.append(listaOrdPib[i][1])
              lnumOrd.append(listaOrdPib[i][1])
          lnumOrd= sorted(lnumOrd,reverse=True)

          for i in lnumOrd:#numeros
              for j in range(len(lnome)):#nomes
                  if lnum[j] == i:
                       lista1.append(lnome[j])
                       lista2.append(i)
                        
          Historico.historico_B8_B11("Busca_11",ano,lista1,lista2,usuario)
          
     else:
          print_cash()
          Historico.historico_B8_B11("Busca_11",ano,lista1,lista2,usuario)
          
                         
     style.use("dark_background")
     plt.plot(lista1,lista2, label = lista1, color = "m", linewidth = 2)
     plt.xlabel("REGIÃO", size = 14)
     plt.ylabel("TAXA DE VENDAS", size = 14)
     plt.title("REGIÃO x TAXAS\nAno {}.".format(ano))
     plt.show()
