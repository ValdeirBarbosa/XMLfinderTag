# XMLfinderTag
Projeto que identifica tags especificas em arquivo XML

No processo de identificação de tags do arquivo XML, foi passado as tags 'alvo'
usando a lib xml.etree.ElementTree para realizar o parse do XMl, 
notificando quando uma das tags 'alvo' estavam ausente na estrutura.

Tratando exceções de ParseError, para que quando uma estrura do XML esteja faltante, 
se tratando de tags que são necessários tags de fechamento.

Quando a estrutura não está correta, é mostrado a possível posição do primeiro sinistro na 
estrutura do XML. 
Quando o xml está completo é gerado um arquivo txt com as informações pertinentes ao solicitante.

Obs: esta estrutura pode ser alterada para uso em outros arquivos XML, caso necessário.
Os arquivos XML a serem 'Parseados' devem ser inseridos na pasta XMLFiles.
A pasta ResultFile e o local onde é armazenado os arquivos txt gerados a partir de cada XML.
O arquivo txt possui o mesmo nome do arquivo xml, alterando somente a sua extensão.
