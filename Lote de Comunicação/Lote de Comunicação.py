import pandas as pd
import xml.etree.ElementTree as ET
import time

dados_lote = pd.read_excel()
# Chamada de arquivo

datatypes_per_column = {
    'req': 'string',
    'nome do cliente': 'string',
    'cpf_cnpj': 'string',
    'Data da Análise': 'string',
    'Data de Cadastro': 'string',
    'Pessoa Obrigada': 'string',
    'Servidor público': 'string',
    'Detalhamento da ocorrência': 'string'
}
dados_lote = dados_lote.astype(datatypes_per_column)
# Normalização de classes por coluna (muito útil para as datas)

ListaCom = dados_lote.values.tolist()
# Referencial de valores para contagem da estrutura de repetição

Codigos_List = dados_lote["req"].tolist()
Nomes_List = dados_lote["nome do cliente"].tolist()
CPFs_List = dados_lote["cpf_cnpj"].tolist()
DataAnalise_List = dados_lote["Data da Análise"].tolist()
PEP_List = dados_lote["PEP"].tolist()
DataAbConta_List = dados_lote["Data de Cadastro"].tolist()
ServPub_List = dados_lote["Servidor público"].tolist()
PObrigada_List = dados_lote["Pessoa Obrigada"].tolist()
Det_List = dados_lote["Detalhamento da ocorrência"].tolist()
# Transformação de colunas em listas

DataReporte = ('SISCOAF')+(str(time.strftime('%d%m%Y')))
# Chamada de data para elaboração do atributo da comunicação

def create_xml():
    Lote = ET.Element("LOTE")
    ocx = ET.SubElement(Lote, "OCORRENCIAS", ID=DataReporte)
    # Cria o elemento principal, secundários estão na estrutura de repetição

    for linha in range(len(ListaCom)):
        oco = ET.SubElement(ocx, "OCORRENCIA")

        CNPJ = ET.SubElement(oco, "CPFCNPJCom")
        CNPJ.text = "00019"

        Num = ET.SubElement(oco, "NumOcorrencia")
        Num.text = str(Codigos_List[linha])

        DtInicio = ET.SubElement(oco,"DtInicio")
        DtInicio.text = str(DataAnalise_List[linha])

        DtFim = ET.SubElement(oco, "DtFim")
        DtFim.text = str(DataAnalise_List[linha])

        AgNum = ET.SubElement(oco, "AgNum")
        AgNum.text = "0001"

        AgNome = ET.SubElement(oco, "AgNom")
        AgNome.text = "Banco XXX"

        AgMun = ET.SubElement(oco, "AgMun")
        AgMun.text = "Sao Paulo"

        AgUF = ET.SubElement(oco, "AgUF")
        AgUF.text = "SP"

        VlCred = ET.SubElement(oco, "VlCred")
        VlCred.text = "1"

        VlDeb = ET.SubElement(oco, "VlDeb")
        VlDeb.text = "1"

        VlProv = ET.SubElement(oco, "VlProv")
        VlProv.text = "1"

        VlProp = ET.SubElement(oco, "VlProp")
        VlProp.text = "1"

        Det = ET.SubElement(oco, "Det")
        Det.text = str(Det_List[linha])

        enq = ET.SubElement(oco, "ENQUADRAMENTOS")
        CodEnq = ET.SubElement(enq, "CodEnq")
        CodEnq.text = '1012'

        env = ET.SubElement(oco, "ENVOLVIDOS")
        CPF = ET.SubElement(env, "CPFCNPJEnv")
        CPF.text = str(CPFs_List[linha])

        NmEnv = ET.SubElement(env, "NmEnv")
        NmEnv.text = str(Nomes_List[linha])

        TpEnv = ET.SubElement(env, "TpEnv")
        TpEnv.text = "Ativo"

        AgNumEnv = ET.SubElement(env, "AgNumEnv")
        AgNumEnv.text = "0001"

        AgNomeEnv = ET.SubElement(env, "AgNomeEnv")
        AgNomeEnv.text = "Banco XXX"

        DtAbConta = ET.SubElement(env, "DtAbConta")
        DtAbConta.text = str(DataAbConta_List[linha])

        DtAtuaCad = ET.SubElement(env, "DtAtuaCad")
        DtAtuaCad.text = str(DataAbConta_List[linha])

        PObrigada = ET.SubElement(env, "PObrigada")
        PObrigada.text = str(PObrigada_List[linha])

        PEP = ET.SubElement(env, "PEP")
        PEP.text = str(PEP_List[linha])

        ServPub = ET.SubElement(env, "ServPub")
        ServPub.text = str(ServPub_List[linha])


    # Estrutura de repetição para inserir lista de elementos que comporão o XML, para cada linha da planilha

    Comunicacao = ET.ElementTree(Lote)
    Comunicacao.write("Lote.xml", encoding='iso-8859-1', xml_declaration=True)
    # Escreve o xml

create_xml()