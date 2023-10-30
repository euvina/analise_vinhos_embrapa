# Análise sobre a Exportação de Vinhos no Brasil

*FIAP: Pós Tech - Data Analytics
Tech Challenge #01*

Grupo 32 - Autores:

- Cristiane Aline Fischer
- Pedro Baldini
- Vinícius Prado Lima
- Vitor Sarilio

**[Link do artigo](https://medium.com/p/0d9858104c67/)**

---

### Contexto

- Empresa que exporta vinhos do Brasil para o mundo, chamada Vinícola 32 (*nome fictício*)
- Área de Analytics recém-criada, responsável por relatórios iniciais a serem apresentados em uma reunião de investidores e acionistas
- Explicar a quantidade de vinhos exportados e os fatores externos que podem vir a surgir e que interferem nas análises
- Construir gráficos que passem a ideia central para que os investidores sigam com as ações
- Utilizar outros dados da vinícola, além de dados externos

### Objetivo

Nossa tarefa é analisar os dados de exportação de vinhos de uma empresa, a qual chamaremos de Vinícola 32, durante o período de 2008 a 2022. Os [dados](http://vitibrasil.cnpuv.embrapa.br/index.php) foram disponibilizados pela Empresa Brasileira de Pesquisa Agropecuária (Embrapa). O foco é orientar os próximos investimentos de um grupo de acionistas da Vinícola 32. Também, preparar uma tabela geral, contendo:

-`País de origem` ('Brasil')

-`País de destino` do vinho

-`Quantidade em litros` de vinho exportado (1kg = 1L)

-`Valor em US$` de vinho exportado

<div class="alert-info">
<b>📊🍷:</b> A tabela geral de exportações de vinho pode ser gerada a partir de duas maneiras diferentes, nos notebooks com prefixo A01 e B01.</div>

---

### Arquivos importantes

**main/**

Existem diversas maneiras de resolver o mesmo problema com Python. Por isso, mantivemos notebooks que contam a mesma história, a partir de métodos diferentes:

    A01_tratamento_vinhos_grupo32.ipynb: tratamento de dados, gera a base de dados para o notebook de prefixo A02

    A02_base_powerbi_vinhos_grupo32.ipynb: gera as bases de dados para o PowerBI, com principais insights

    B01_unico_vinhos_grupo32.ipynb: análise única, com tratamento e visualização de dados

    Vinícola 32.pbix: dashboard desenvolvido no PowerBI com dados gerais de exportação da Vinícola 32
    

**./utils/**

    functions.py: funções utilizadas no notebook com prefixo B01

    wine_style.mplstyle: folha de estilo para matplotlib utilizada no notebook com prefixo B01

---

### Fontes de dados

*Todos as bases de dados são mantidas pelas respectivas fontes.*

* [Vitibrasil - Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php)
* [Governo Brasileiro -  Comex](http://comexstat.mdic.gov.br/pt/faq)
* [OIV - Organização Internacional da Vinha e do Vinho](https://www.oiv.int/en)
* [Python BCB - @Wilson Freitas](https://wilsonfreitas.github.io/python-bcb/)
* [Banco Central do Brasil - Dados Abertos](https://dadosabertos.bcb.gov.br)
