# XMLfinderTag
projeto que identifica tags especificas em arquivo XML

No processo de identificação de tags do arquivo XML, foi passado as tags 'alvo'
usando a lib xml.etree.ElementTree para realizar o parse do XMl, 
notificando quando uma das tags 'alvo' estavam ausente na estrutura XML
tratando a exeção de ParseErro, para que quando uma estrura do XML esteja faltante, 
se tratando de tags que são necessários tags de fechamento.
Quando a estrutura nao esta correta, e mostrado a possiel posição do primeiro sinistro na 
estrutura do XML. Quando o xml está completo e gerado um arquivo txt com as informações 
pertinentes ao solicitante.
Obs: esta estrutura pode ser alterada para uso em outros arquivos XML, caso necessário.
Os arquivos XML a serem 'Parseados' devem ser inseridos na pasta XMLFiles.
A pasta ResultFile e o local onde e armazenado os arquivos txt gerados a partir de cada XML.
O arquivo txt posui o mesmo nome do arquivo xml, alterando somente a sua extenção.


