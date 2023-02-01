# NeoWay_ChallengePirates

O desafio foi desenvolvido na linguaguem python usando a lógica abaixo:

Passos para o desenvolvimento:

1 - Extrair lista de todos os estados conforme opção de pesquisa fornecida pelo site dos correios, mostrado na imagem abaixo.
    
![image](https://user-images.githubusercontent.com/124132986/215987235-21b59c22-9c06-4281-9377-d8fa1c914164.png)

- Obteve-se as informações necessárias para o código, no caso 'class', através da opção 'inspecionar' do html
    
![image](https://user-images.githubusercontent.com/124132986/215989440-63185c06-5981-4f6c-bccb-d007eeb3ef18.png)

- Foram utilizadas as bibliotecas BeautifulSoup e request para extrair o conteudo html do site dos correios e o parser para particioná-lo. 
    
- Utilizou-se a biblioteca re para identificar o padrão da string e extrair somente a sigla dos estados.
    
- Fez-se a limpeza da lista.

2 - Criar lista dos campos de pesquisas a serem inseridos no loop para extrair dados de pesquisa de todos os estados.

- A pesquisa é feita por estado e gera uma tabela tipo 'form' para cada estado.

![image](https://user-images.githubusercontent.com/124132986/215990605-b781692d-ea23-4cd2-b0a0-cc033216afba.png)

- Para extrair a tabela do estado, precisa-se identificar qual é a 'UF' e a 'Localidade'. 
- Para isso foi realizado um loop para criar uma lista com os campos a serem pesquisados para cada estado.

        => post_fields = {"UF": estado, "Localidade" : " "}

