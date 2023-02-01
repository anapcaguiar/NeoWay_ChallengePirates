# NeoWay_ChallengePirates

O desafio foi desenvolvido na linguaguem python usando a lógica abaixo:

Passos para o desenvolvimento:

1 - Extrair lista de todos os estados conforme opção de pesquisa fornecida pelo site dos correios, mostrado na imagem abaixo.
    
![image](https://user-images.githubusercontent.com/124132986/215987235-21b59c22-9c06-4281-9377-d8fa1c914164.png)

    a) Obteve-se as informações necessárias para o código, no caso 'class', através da opção 'inspecionar' do html
    
    ![image](https://user-images.githubusercontent.com/124132986/215989440-63185c06-5981-4f6c-bccb-d007eeb3ef18.png)

    b) Foram utilizadas as bibliotecas BeautifulSoup e request para extrair o conteudo html do site dos correios e o parser para particioná-lo. 
    
    c) Utilizou-se a biblioteca re para identificar o padrão da string e extrair somente a sigla dos estados.
    
    d) Fez-se a limpeza da lista.

2 - Criar lista dos campos de pesquisas a serem inseridos no loop para extrair dados de pesquisa de todos os estados.

![image](https://user-images.githubusercontent.com/124132986/215986848-d8334922-8680-4b2a-bdec-b26e1b4348ae.png)
