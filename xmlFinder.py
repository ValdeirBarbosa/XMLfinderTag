import xml.etree.ElementTree as ET
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def stringFy(testo,tabulacao):
    text = str(testo)
    text = text.strip("(")
    text = text.strip(")")
    text = text.replace(' ','')
    text = text.replace("'",'')
    text = text.replace(",",' ')
    if(tabulacao):
        return '\t'+text+'\n'
    else:
        return text+'\n'

def openResultFilesFolder(folderpath):
    path = os.path.normpath(folderpath)
    if os.path.isdir(folderpath):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(folderpath):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

def XMLEncoder(xmlPathFile, arquivo):
    tree = ET.parse(xmlPathFile)
    root = tree.getroot()
    mapListNode = []
    mapListNode_tag = []
    mappinTagDivergente = []
    nodeRootList = []
    tagList = [
        '{urn:abb-robotics-safety-controller-configuration}ValidationInfo',
        '{urn:abb-robotics-safety-controller-configuration}ConfigurationSeal',
        '{urn:abb-robotics-safety-controller-configuration}ProtectedElements',
        '{urn:abb-robotics-safety-controller-configuration}FuncIOMappings'
    ]
    funIOmappings = [
        '{urn:abb-robotics-safety-controller-configuration}AutomaticMode',
        '{urn:abb-robotics-safety-controller-configuration}AutoIn',
        '{urn:abb-robotics-safety-controller-configuration}DriveEnable',
        '{urn:abb-robotics-safety-controller-configuration}LocalEmergencyStopStatus',
        '{urn:abb-robotics-safety-controller-configuration}ManualMode',
        '{urn:abb-robotics-safety-controller-configuration}ManualIn',
        '{urn:abb-robotics-safety-controller-configuration}ManualFullSpeedMode',
        '{urn:abb-robotics-safety-controller-configuration}ManualFSIn',
        '{urn:abb-robotics-safety-controller-configuration}SafetyEnable',
        '{urn:abb-robotics-safety-controller-configuration}ExternalPowerControlActive',
        '{urn:abb-robotics-safety-controller-configuration}ExternalPowerControlFeedback',
        '{urn:abb-robotics-safety-controller-configuration}DriveEnableFeedback'
    ]
    
    ResultTxtFile = 'ResultFile\\'+arquivo.replace('.xml','.txt')
   
    arquivo = open(ResultTxtFile, "w", encoding='utf-8')

    for nod in root.iter():
        nodeRootList.append(nod.tag)
    for tgl in tagList:
        if(not tgl in nodeRootList):
            print(tgl[50:], 'AUSENTE NO XML!!****')
            arquivo.write(u'{} AUSENTE NO XML!!****\n'.format(tgl[50:]))

    for node in root.iter():
        if(node.tag == tagList[0]):
            tagList[0] = node.tag[50:], 'validatedBy=',node.attrib.get('validatedBy', "Ausente!"), 'validationDate=',node.attrib.get('validationDate', "Ausente")
            print(node.tag[50:], '\t ', ':[ validatedBy=', node.attrib.get('validatedBy', "Ausente"),'validationDate=',node.attrib.get('validationDate', "Ausente")+']')
            linha = (node.tag[50:],':[ validatedBy=',node.attrib.get('validatedBy', "Ausente"), 'validationDate=', node.attrib.get('validationDate', "Ausente")+']')
            arquivo.write(u'{}'.format(stringFy(linha,False)))

        if(node.tag == tagList[1]):
            tagList[1] = node.tag[50:], 'checksum=', node.attrib.get(
                'checksum', "Ausente"), 'systemName=', node.attrib.get('systemName', "Ausente")
            print(node.tag[50:], ':[ checksum=', node.attrib.get(
                'checksum', "Ausente"), 'systemName=', node.attrib.get('systemName', "Ausente")+']')
            linha = node.tag[50:],':[ checksum=', node.attrib.get('checksum', "Ausente"), 'systemName=', node.attrib.get('systemName', "Ausente")+']'
           
            arquivo.write(u'{}'.format(stringFy(linha,False)))

            

        if(node.tag == tagList[2]):
            tagList[2] = node.tag[50:], 'checksum=', node.attrib.get('checksum', "Ausente")
            print(node.tag[50:], ':[ checksum=',node.attrib.get('checksum', "Ausente")+']')
            linha = node.tag[50:], ':[ checksum=',node.attrib.get('checksum', "Ausente")+']'
            arquivo.write(u'{}'.format(stringFy(linha,False)))

        if(node.tag == tagList[3] and node.tag == '{urn:abb-robotics-safety-controller-configuration}FuncIOMappings'):
            print(node.tag[50:], ':[')
            arquivo.write(u'{}\n'.format(node.tag[50:]+':[').replace("'",'').strip("(").strip(")"))
            for _node in node.iter():
                if (_node.tag != node.tag):
                    # gerando uma lista de todas as tags contidas em FuncIOMappings
                    mapListNode.append(_node)
                    # gera uma lista de nomes das tags contidas eFuncIOMappings
                    mapListNode_tag.append(_node.tag)
            for nd in mapListNode:
                if(nd.tag in funIOmappings):
                    if(len(nd.attrib) == 3):
                        print('\t', nd.tag[50:], '{signalName=', nd.attrib.get('signalName', "Ausente"), 'mandatory=', nd.attrib.get('mandatory', "Ausente"), 'visible=', nd.attrib.get('visible', "Ausente")+'}')
                        linha = ( nd.tag[50:], '{signalName=', nd.attrib.get('signalName', "Ausente"), 'mandatory=', nd.attrib.get('mandatory', "Ausente"), 'visible=', nd.attrib.get('visible', "Ausente")+'}')
                    else:
                        print('\t', nd.tag[50:], '{signalName=', nd.attrib.get('signalName', "Ausente"), 'mandatory=', nd.attrib.get('mandatory', "Ausente")+'}')
                        linha = nd.tag[50:], '{signalName=', nd.attrib.get('signalName', "Ausente"), 'mandatory=', nd.attrib.get('mandatory', "Ausente")+'}'
                    
                    arquivo.write(u'{}'.format(stringFy(linha,True)))
                else:
                    mappinTagDivergente.append(nd)
            print(']')
            arquivo.write(u']\n')
            for nodeT in funIOmappings:
                if(not nodeT in mapListNode_tag):
                    print('\t', nodeT[50:],'\t**** TAG AUSENTE NO ARQUIVO XML !!****')                    
                    linha = '\t'+str(nodeT[50:]+'\t**** TAG AUSENTE NO ARQUIVO XML !!****')                  
                    arquivo.write(u'{}\n'.format(linha))             
            if(len(mappinTagDivergente) != 0):
                print('\n'*2, 'TAGS EXEDENTES DENTRO Da TAG "FuncIOMappings"')
                linha = '\n'*2+'TAGS EXEDENTES DENTRO Da TAG "FuncIOMappings"'
                for n in mappinTagDivergente:
                    linha += '\n'+n.tag[50:]+'\t'+str(n.attrib)
                    print(n.tag[50:],'\n \t', n.attrib)
                arquivo.write(u'{}'.format(linha))
    arquivo.close()
