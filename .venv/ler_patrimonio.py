import csv
# Abrir o arquivo csv e atribuir a uma variavel
arquivo = open("Patrimônio.csv","r",encoding="utf8")
linhas= csv.reader(arquivo)


for i in linhas:
    lin = str(i).replace("['","").replace("']","").split(";")
    if(lin[0]=="9483"):
        print(lin)