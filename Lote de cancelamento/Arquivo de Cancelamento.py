import pandas as pd
import xml.etree.ElementTree as ET
import time

dados_cancelamento = pd.read_excel()
# Chamada de arquivo

ListaCancelamento = dados_cancelamento.values.tolist()
# Referencial de valores para contagem da estrutura de repetição

Codigos_List = dados_cancelamento["req"].tolist()
Numero_List = dados_cancelamento["Número COAF"].tolist()
Autenticacao_List = dados_cancelamento["Autenticação"].tolist()
Motivo_List = dados_cancelamento["Motivo do cancelamento"].tolist()
# Transformação de colunas em listas

DataReporte = ('SISCOAFCancelamento')+(str(time.strftime('%d%m%Y')))
# Chamada de data para elaboração do atributo da comunicação

def create_xml():
    Lote = ET.Element("LOTECANCELAMENTO")
    ocx = ET.SubElement(Lote, "OCORRENCIAS", ID=(DataReporte).replace('""',''))
    # Cria o elemento principal, secundários estão na estrutura de repetição

    for linha in range(len(ListaCancelamento)):
        oco = ET.SubElement(ocx, "OCORRENCIA")

        NUMEROORIGEM = ET.SubElement(oco, "NUMEROORIGEM")
        NUMEROORIGEM.text = str(Codigos_List[linha])

        NUMEROCOAF = ET.SubElement(oco, "NUMEROCOAF")
        NUMEROCOAF.text = str(Numero_List[linha])

        AUTENTICACAO = ET.SubElement(oco, "AUTENTICACAO")
        AUTENTICACAO.text = str(Autenticacao_List[linha])

        MOTIVO = ET.SubElement(oco,"MOTIVO")
        MOTIVO.text = str(Motivo_List[linha])
    # Estrutura de repetição para inserir lista de elementos que comporão o XML, para cada linha da planilha

    Comunicacao = ET.ElementTree(Lote)
    Comunicacao.write("Arquivo de Cancelamento.xml", encoding='iso-8859-1', xml_declaration=True)
    # Escreve o xml

create_xml()