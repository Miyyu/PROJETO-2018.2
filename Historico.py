import json
import io


def historico_B2(busca,entrada1,entrada2,saida,usuario):
     arq = open(usuario,"a")
     arq.write(busca+";"+str(entrada1)+";"+str(entrada2)+";")
     var = json.dumps(saida)
     arq.write(var)
     arq.write(";"+"\n")
     arq.close()

def cashB2(busca,entrada1,entrada2,usuario):
     arq = open(usuario,"r")
     for linha in arq:
          linhas = linha.split(";")
          if linhas[0] == busca:
               if int (linhas[1]) == int(entrada1) and linhas[2] == entrada2:
                    var = json.loads(linhas[3])
                    return True, var
     arq.close()          
     return False, 0

def historico_B3_B7(busca,entrada1,saida,usuario):
     arq = open(usuario,"a")
     arq.write(busca+";"+str(entrada1)+";")
     var = json.dumps(saida)
     arq.write(var)
     arq.write(";"+"\n")
     arq.close()

def cashB3_B7(busca,entrada,usuario):
     arq = open(usuario,"r")
     for linha in arq:
          linhas = linha.split(";")
          if linhas[0] == busca:
               if str(linhas[1]) == str(entrada):
                    var = json.loads(linhas[2])
                    return True, var
     arq.close()          
     return False, 0

def historico_B5_B6(busca,entrada1,entrada2,entrada3,saida1,saida2,usuario):
     arq = open(usuario,"a")
     arq.write(busca+";"+str(entrada1)+";"+str(entrada2)+";"+str(entrada3)+";")
     var1 = json.dumps(saida1)
     var2 = json.dumps(saida2)
     arq.write(var1)
     arq.write(";")
     arq.write(var2)
     arq.write(";"+"\n")
     arq.close()

def cashB5_B6(busca,entrada1,entrada2,entrada3,usuario):
     arq = open(usuario,"r")
     for linha in arq:
          linhas = linha.split(";")
          if linhas[0] == busca:
               if int(linhas[1]) == int(entrada1) and int(linhas[2]) == int(entrada2) and str(linhas[3]) == str(entrada3):
                    var1 = json.loads(linhas[4])
                    var2 = json.loads(linhas[5])
                    return True, var1,var2
     arq.close()          
     return False, 0, 1

def historico_B8_B11(busca,entrada1,saida1,saida2,usuario):
     arq = open(usuario,"a")
     arq.write(busca+";"+str(entrada1)+";")
     var1 = json.dumps(saida1)
     var2 = json.dumps(saida2)
     arq.write(var1)
     arq.write(";")
     arq.write(var2)
     arq.write(";"+"\n")
     arq.close()

def cashB8_B11(busca,entrada1,usuario):
     arq = open(usuario,"r")
     for linha in arq:
          linhas = linha.split(";")
          if linhas[0] == busca:
               if int(linhas[1]) == int(entrada1):
                    var1 = json.loads(linhas[2])
                    var2 = json.loads(linhas[3])
                    return True, var1,var2     
     arq.close()         
     return False, 0, 1

def verHistorico(usuario):
     
     print("»EXIBIR HISTÓRICO DE BUSCAS\n")
     print("⩫"*80)
     
     arq = open(usuario,"r")
     for linha in arq:
          linhas = linha.split(";")
          if linhas[0] != "G" and linhas[0] != "F":
               if linhas[0] != "Busca_2" and linhas[0] != "Busca_5" and linhas[0] != "Busca_6":
                    print("{}  |  Entrada = {}  |".format(linhas[0],linhas[1]))
                    
               elif linhas[0] != "Busca_2" and linhas[0] != "Busca_3" and linhas[0] != "Busca_7" and linhas[0] != "Busca_8":
                    print("{}  |  Entrada 1 = {}  |  Entrada 2 = {}  |  Entrada 3 = {}  |".format(linhas[0],linhas[1],linhas[2],linhas[3]))
                    
               elif linhas[0] != "Busca_3" and linhas[0] != "Busca_5" and linhas[0] != "Busca_6" and linhas[0] != "Busca_7" and linhas[0] != "Busca_8":
                    print("{}  |  Entrada 1 = {}  |  Entrada 2 = {}  |".format(linhas[0],linhas[1], linhas[2]))
     arq.close()
     print("⩫"*80)
     print("")
