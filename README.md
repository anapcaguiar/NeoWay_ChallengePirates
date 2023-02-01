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

3 - Consultar faixa de cep de todos os estados e concatenar dados em uma lista unica.
- Utilizou o loop para consultar cada estado, extrair a tabela da primeira página, adicionar todas as tabelas em uma única lista e posteriormente transformar em dataframe.
- A solução desse problema está incompleta, pois coleta apenas a primeira página, ao invés de todas as páginas que forem geradas conforme a quantidade de faixa de CEP.
- Tentei fazer um loop para ler o href de cada página, para assim coletar os dados de todas as páginas. Mas por ser um 'form', não consegui usar essa solução.
- Fiquei bastante curiosa em como resolver essa parte do código. Poderiam me explicar depois? :)

![image](https://user-images.githubusercontent.com/124132986/215993200-c0c43116-de2d-45ee-9ea6-ee1575861f5a.png)

4 - Limpeza dos dados para atender as requisições do desafio, como:
- Remoção de colunas desnecessárias;
- Adição de coluna como identificador único;
- Remoção de dados duplicados.

5 - Transformar dataframe em JSON
