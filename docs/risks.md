# Gerenciamento de Riscos

## Introdução

Os riscos do projeto são empecilhos que podem acontecer e atrapalhar o andamento do desenvolvimento como o esperado. Para lidar com esses riscos, é necessário identificá-los para que a equipe, ciente de sua existência e impacto, possa trabalhar para contorná-los.

## Identificação de riscos

Durante os ritos de Review da Sprint, o grupo discute sobre como foi a sprint e os problemas enfrentados e são levantados possíveis riscos para o andamento do projeto. Esses riscos são registrados e pontuados conforme as metricas.

Abaixo temos uma tabela com os principais riscos identificados ao decorrer do projeto.

| Risco | Ação preventiva | Ação reativa |
| -- | -- | -- |
| Falta ou falha de equipamentos | Manutenção do equipamento | Pareamento através de chamadas de vídeo com piloto e copiloto|
| Falta de conhecimento da equipe em relação às tecnologias | Dojos ensinando cada tecnologia utilizada | Retirar dúvidas com a equipe e fazer pareamentos com os membros de EPS |
| Divergência de horários entre os membros | Quadro de horários disponíveis | Planejamento de pareamentos e reuniões de acordo com o quadro de horários |
| Indefinição de escopo | Contato com o cliente para maior especificação do problema | Aplicação do Lean Inception com validação do cliente |
| Falta de comunicação com o cliente | Marcar horários fixos de reunião | Adicionar o cliente em canais de comunicação da disciplina |
| Dificuldade em configurar ambiente | Tirar dúvidas de instalação com a equipe | Manter ambientes dockerizados |
| Dificuldade na elaboração das issues | Criação de templates para a criação de issues | Revisão após a criação das issues |
| Quantidade de débitos técnicos | Planejar melhor a sprint | Finalizar os débitos pendentes|

<br>

## Métricas

Para metrificar os riscos do projeto, foi utilizado um burndown de riscos, para obter a noção da relevância de um risco ao longo das sprints

Para obter a relevância de cada risco, deve-se levar em conta dois principais fatores, sendo eles:

- Probabilidade: A probabilidade representa a chance (%) desse risco ocorrer, tal indicação é feita em cada sprint.

- Impacto: O impacto representa o prejuízo que cada risco oferece ao projeto caso ocorra.

Abaixo, foi representado como foi feita a estimação de cada fator e o que ela representa.

|Probabilidade|Descrição|Valor|
|--|--|--|
|Nenhum|Nenhuma chance de acontecer|0|
Raro|Menor que 20% de chance de acontecer|1|
Improvável|Entre 21% e 40% de chance de acontecer|2|
Pouco Provável|Entre 41% e 60% de chance de acontecer|3|
Muito provável|Entre 61% e 80% de chance de acontecer|4|
Quase Certo|Entre 81% e 100% de chance de acontecer|5|

<br>

|Impacto|Descrição|Valor|
|--|--|--|
|Nenhum|Nenhum impacto|0|
Muito pequeno|Praticamente sem impactos ao projeto|1|
Pequeno|Impacto pequeno ao projeto|2|
Médio|Impacto que começa a apresentar algumas consequências ao projeto|3|
Alto|Impacto que compromete o andamento saudável do projeto|4|
Altíssimo|Impacto que inviabiliza o andamento do projeto caso não seja corrigido ou minimizado|5|

## Burndown de Riscos

Os riscos são pontuados pela equipe em relação à **Probabilidade** e **Impacto** em uma planilha, atualizada toda sprint do projeto. Com essa pontuação é gerado gráficos de Burndown de Riscos, um geral, onde podemos ver o burndown acumulado de todos os riscos do projeto por sprint, e o individual de cada risco, onde podemos ver o andamento de um determinado risco ao longo das sprints do projeto.

Com essas informações, identificamos se a equipe está lidando com os riscos corretamente, verificando se os valores dos riscos estão diminuindo individualmente.

Abaixo é possível ver o gráfico de riscos gerais.

<iframe width="957" height="591" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQv0rxUufxF56EyZ9Rn5ihFpOzI3R5_JqG0o2LsCroy01X92DaF5tXtVKESXDxQS3g271G7Z-KAM4QG/pubchart?oid=1162260752&amp;format=interactive"></iframe>

Para ver os detalhes de cada risco e os gráficos individuais, acesse a [planilha de riscos](https://docs.google.com/spreadsheets/d/1YzzYUVwmzwEa2fGIQ8hpaLnNWbssrnSWwQ7mpCyi3-o/edit?usp=sharing).
