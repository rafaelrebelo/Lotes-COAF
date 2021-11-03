# Montagem de lotes COAF

<b> Descrição: </b>

Bibliotecas em Python para geração dos lotes de comunicação ao COAF (.xml) a partir de planilhas do excel. Baseado no manual de integração do SISCOAF, versão 2.0.

<b> Libraries: </b>

   1)  xml.etree.ElementTree
    https://docs.python.org/3/library/xml.etree.elementtree.html
   
   2)  pandas
    https://pandas.pydata.org/docs/
    
   3)  datetime
    https://docs.python.org/3/library/datetime.html
    

<b> Observações: </b> 

  - CodEnq e TpEnv possuem tabelas próprias de domínio, que dependem do segmento da Pessoa Obrigada;
  - Para padronização de campos, é preferível a alteração do código, e não da planilha;
  - Não contém a estrutura de assinatura digital. É a mesma utilizada em assinaturas de NFE;
  - Estruturas de retificação serão adicionadas em breve.
