import os
import os.path 
from xmlFinder import XMLEncoder, openResultFilesFolder
import xml.etree.ElementTree as ET





    

def myApp():
    if(not os.path.isdir('ResultFile')):
        os.mkdir('ResultFile')

    if( not os.path.exists('XMLFiles')): 
        xmlEpmtyFolder  =  input('''Arquivos nao existentes na pasta XMLFiles!
            \n por favor revise e execute o programa novamente!
            \n PRESSIONE UMA TECLA PARA ENCERRAR! ''')
        os.mkdir('XMLFiles')
        
        

    for diretorio, subpastas, arquivos in os.walk('XMLFiles'):
        if (len(arquivos)==0):
            openResultFilesFolder('XMLFiles')
        else:
            for arquivo in arquivos:
                print(os.path.join(diretorio, arquivo))
                try:
                    XMLEncoder(os.path.join(diretorio, arquivo),arquivo)
                except ET.ParseError  as e:
                    print('''Arquivo com estrutura incompleta\n 
                    O erro  se aproxima da linha {} no arquivo XML\n 
                    podendo ser uma tag de abertura ou fechamento'''.format(e.args[0][-1:]),e,subpastas)
                    
                    ResultTxtFile = 'ResultFile\\'+arquivo.replace('.xml','.txt')
                    arquivo = open(ResultTxtFile, "w", encoding='utf-8')
                    arquivo.write(u'''{}\nArquivo com estrutura incompleta, o erro  se aproxima da linha {} no arquivo XML\npodendo ser uma tag de abertura  ou fechamento
        \nExemplo de tag de abertura : "<ConfigurationSeal>"\nExemplo de tag de fechamento: "</ConfigurationSeal>"\n \n {} \n{}'''.format('*'*83,e.args[0][-1:],e,'*'*83))
                    arquivo.close()
                    continue
            openResultFilesFolder('ResultFile')
   

if __name__ == "__main__":
    myApp()


