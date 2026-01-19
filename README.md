# Análise Exploratória: Selic Vs IPCA e Desempenho do E-commerce no Brasil (Olist)
Análise de Macroeconomia vs. E-commerce

Hipótese: A variação da taxa de juros real (Selic ajustada pelo IPCA) influencia diretamente o volume de vendas e o ticket médio no e-commerce brasileiro. Espera-se que, em períodos de juros reais elevados, o consumo de bens não essenciais diminua devido ao custo de oportunidade do capital e encarecimento do crédito.

Pergunta-Chave:

    "Qual é a correlação temporal entre a taxa de juros real brasileira e o comportamento de compra dos clientes no dataset da Olist entre 2016 e 2018?"

Resumo da Implementação: O código consome dados da API do Banco Central do Brasil (SGS) via biblioteca python-bcb.

    Extrai a Selic Meta (anualizada) e o IPCA (variação mensal).

    Converte a Selic para base mensal decimal.

    Aplica a Equação de Fisher para determinar o juro real mensal:
    (1+r)=(1+π)(1+i)​

    (Onde r é o juro real, i o nominal e π a inflação).

    Agrega os dados por frequência mensal para compatibilidade com análises de faturamento.

Sugestões de Cruzamento para o Grupo (Continuação)

    Dados da Olist (pedidos, itens, pagamentos)

    Análise de Lag (Defasagem): A Selic não afeta o consumo no mesmo dia. Criar coluna de juros defasada em 1 ou 2 meses (df['selic_real'].shift(1)) e ver se a correlação com o número de pedidos é maior do que no mês corrente.

    Ticket Médio por Categoria vs. Juros: Cruzar o juro real com o preço dos produtos. Categorias de alto valor (como eletrônicos e móveis), que dependem mais de parcelamento/crédito, tendem a sofrer mais com a alta dos juros do que categorias de baixo valor (beleza, utilidades domésticas).

    Método de Pagamento: Verificar se em meses de juro real alto o número de parcelas no cartão de crédito aumenta ou se o uso de boleto (à vista) diminui.

    Correlação de Pearson: Criar uma matriz de correlação entre selic_real_am e faturamento_mensal_olist. Se o coeficiente for negativo e forte (ex: -0.7), a hipótese de que o juro inibe as vendas é validada.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** Pandas, NumPy (Manipulação) | Matplotlib, Seaborn (Visualização) | Scikit-learn (Normalização)
* **Ambiente:** Jupyter Notebook 

---
> **Nota:** Este projeto foi desenvolvido para fins acadêmicos utilizando dados reais anonimizados.
