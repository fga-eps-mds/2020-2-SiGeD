# Documento de Visão

## 1. Introdução

Este documento tem o propósito de apresentar de forma geral e clara, o objetivo do projeto, algumas definições e formas de resolver os problemas propostos.

### 1.1. Propósito

O projeto tem o intuito de auxiliar no trabalho da DPSS. Na data de escrita deste documento, as demandas que chegam para a DPSS são todas processadas e acompanhadas usando planilhas ou outros meios que facilitam o erro humano e podem atrasar o trabalho a ser feito, por isso o intuito é facilitar e agilizar esse processo de trabalho da DPSS.

### 1.2. Escopo

O escopo do projeto está associado a necessidade da DPSS em armazenar dados e acompanhar servidores que necessitam de algum serviço oferecido pela DPSS, sem a necessidade de vasculhar planilhas ou pastas todos os dias para dar sequência a uma demanda que chegue até a DPSS.

### 1.3. Definições, acrônimos e abreviações
- SiGeD - Sistema de Gerenciamento de Demandas 
- FGA - Faculdade do Gama.
- UnB - Universidade de Brasília.
- MDS - Métodos de Desenvolvimento de Software.
- EPS - Engenharia de Projeto de Software.
- DPSS - Divisão de Proteção à Saúde do Servidor.
- Demandas - Formas a qual se solicita um serviço oferecido pela DPS, sendo um serviço administrativo (Retirada do porte de arma, afastamento por calamidade pública...), ou algum atendimento (Fisioterapia, Psicologia.... )
- Plataforma - Referência para o produto que está sendo desenvolvido.
- Front-end - É a camada do software no qual o cliente tem contato, no caso é o website que será utilizado pelo usuário final
- Back-end - É a camada do software no qual o usuário não terá acesso diretamente, esta camada é onde será guardado os dados, e é consumida pelo Front-end
- framework - O framework é um conjunto de códigos genéricos e básicos usados como um pacote por desenvolvedores.
- ReactJs - framework utilizado para o desenvolvimento do Front-end
- NodeJs - framework utilizado para o desenvolvimento do Back-end
- PO's - Donos do produto (Product Owners) são os usuários que estão em contato direto com o grupo de gestão e de desenvolvimento


### 1.4. Visão geral
Esse documento é dividido em 7 sessões. A introdução compõem o escopo e o propósito do projeto dado a situação da DPSS.

A sessões do posicionamento revela as oportunidades de negócio por trás do produto e explica o problema a ser solucionado.

O terceiro tópico, visa passar pelas necessidades dos usuários e elaborar a definição de requisitos.

A visão geral do produto fornece uma visão em alto nível das capacidades do produto, mostrando uma perspectiva do produto e suas funções.

Na quinta sessão, o recursos do produto lista os recursos do produto. Cada subtópico dessa sessão  inclui uma descrição e o problema que deve solucionar.
A sexta sessão, observam-se as restrições de design e as retrições externas, como requisitos operacionais ou regulamentares.

O último e o sétimo tópico, aprensenta nossas referências que ajudaram no processo de elaboração do documento.

## 2. Posicionamento

### 2.1. Oportunidade de negócio
O SiGeD ,tem como objetivo principal atenuar as chances de erro causados pelos servidores da atual DPSS, agregando no rendimento dos funcionários.Além disso, digitalizar os processos de registro e agendamento, conseguimos evitar possíveis perdas de dados e documentos importantes. provendo uma melhora de agilidade e facilidade para acompanhamentos e atendimentos.


### 2.2. Instrução do problema
Os servidores da DPSS, no presente momento, sofrem com o processo de organização das demandas e a verificação dos dados do cliente. Ambos os processos ainda são feitos a partir de fichas escritas em papel ou mensagens de texto, faltando padronização e mecanismo de busca para aquisição de dados.

Visto que o problema está ligado principalmente ao acesso e a perda de dados. O SiGeD gerência e padroniza a forma que o serviço é feito. Assim, nosso produto simplifica e acelera o trabalho do oficial.

### 2.3. Instrução de Posição do produto

Para os servidores que trabalham na DPSS, que constantemente fazem consultas de demandas, e acompanhamento de serviços que são oferecidos, porém o departamento não conta com nenhum serviço próprio para realização desse trabalho, que provoca certa demora para a conclusão de demandas simples, ou dificuldade na recuperação de dados. atualmente é utilizado uma tabela na internet para fazer alguns acompanhamentos, além de documentos físicos em papel, o produto proposto tem o objetivo de centralizar as demandas, e facilitar o acesso a esses dados posteriormente.

## 3. Descrições da Parte Interessada e do Usuário

### 3.1 Resumo da Parte Interessada:

Grupo     | Descrição   | Responsabilidade 
:-------: | :------: | :------:
Equipe de Gestão do Projeto | Alunos da disciplina de EPS, FGA-UnB | Gerenciar e direcionar a equipe de desenvolvimento e documentar o projeto.
Equipe de Desenvolvimento   | Alunos da disciplina de MDS, FGA-UnB | Desenvolver, testar e documentar um produto final que supra as necessidades do cliente.
Professor | Professor das disciplinas EPS e MDS FGA-UnB | Avaliar e orientar os trabalhos desenvolvidos pela Equipe de MDS e EPS.
DPSS   | Servidores que trabalham na DPSS | Orientar e dar a visão sobre o produto.


### 3.2 Resumo do Usuário:
Grupo     | Descrição   | Responsabilidade 
:-------: | :------: | :------:
Funcionário DPSS | Servidores da DPSS | Resolver demandas administrativas ou não.
Atendentes | Recepcionistas | Cria demandas e registra servidores externos.
DPSS | Representa o departamento | Administra e tem acesso a todas as demandas em andamento e históricos. 


## 4. Visão Geral do Produto

### 4.1 Perspectiva do Produto:
Os funcionários da DPSS não possuem um software de uso próprio para auxiliá-los em todas suas necessidades e para este fim o SiGeD foi criado. Ele é um website que auxilia os funcionários da DPSS a realizar os atendimentos, salvamento de dados e prontuário dos pacientes, agilizar a realização de tarefas e criar estatísticas baseadas nos dados da plataforma.

### 4.2 Resumo das capacidades:

**Benefícios para o Usuário**     | **Recursos de Suporte**
----------------------------------|--------------------
Padronizar o forma de trabalho    | Aplicação com várias funcionalidades que cobrem suas necessidades
Maior comodidade do usuário       | O servidor da DPSS pode fazer trabalho remoto
Evitar perda de dados             | Banco de dados para armazenar documentos
Agilizar a análise de dados       | Mecanismo de busca no site

&nbsp;

**Benefícios para o Cliente**     | **Recursos de Suporte**
----------------------------------|--------------------
Maior satisfação do Cliente       | Atendimento mais rápido
Cliente não precisa reenviar os dados       | Os dados estão salvos com rápido acesso


## 5. Recursos do Produto

### 5.1. Controle de dados do cliente
É uma das principais funções da aplicação, o usuário pode cadastrar o cliente no site e acessar os dados cadastrados. 

### 5.2. Histórico de Processos e Pacientes
Essa funcionalidade permite ao usuário um controle mais amplo dos clientes para elaborar estatísticas e confirmar eventos posteriormente.

### 5.3. Anexo Documentos
Anexar documentos ao realizar um agendamento é essencial para o desenvolvimento do projeto. Uma vez que estamos substituindo o papel por telas digitais, precisamos anexar arquivos no envio de documentos.

### 5.4. Estatísticas dos Atendimentos
As estatísticas de atendimentos são necessárias para o relatório de informações a respeito dos agendamentos. Esse relatório é de responsabilidade da DPSS para avaliar as condições dos clientes.

### 5.5. Filtragem de solicitações
A filtragem de solicitações é um mecanismo de busca para facilitar o acesso de informações feitas pelo usuário.

### 5.6. Cadastro de Agendamentos/Solicitações
O usuário pode cadastrar agendamentos e solicitações pelo site e evitando o uso de papel e padronizando o serviço da DPSS.

## 6. Restrições

Para o design, a equipe de gestão do projeto em conjunto com a equipe de desenvolvimento deverão seguir a paleta de cores e o protótipo que foram validados que os PO 's do projeto.
Para restrição de segurança e até de uso, a plataforma permite que usuários sejam cadastrados por administradores, os usuários que serão cadastrados como funcionários da DPSS poderão cadastrar o público de servidores externos como clientes, que de alguma forma irão precisar dos serviços da DPSS com algum tipo de demanda. Restrição para implementação, o grupo em conjunto decidiu centralizar as plataformas usando Javascript, com os frameworks Reactjs para o Front-end e Nodejs para o Back-end.

## 7. Referências
IBM Knowledge Center - Documento de Visão: Estruturas de um Documento de Visão.

Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html

Acesso em: 17 de Março de 2021.




