# Guia de Contribuição

Este é um documento para auxiliar a como contribuir para o projeto **2020.2 - G4**. O projeto é constituido de vários repositórios e esse guia é aplicado em todos eles. 

Orientamos que antes de começar a contribuir veja as [issues já abertas](https://github.com/fga-eps-mds/2020-2-G4/issues).

## Como contribuir

Para contribruir com o projeto o processo é bem simples:

1. [Crie uma issue](#politica-de-issues) descrevendo a feature ou o problema a ser resolvido.
2. [Crie sua branch](#politica-de-branches) para trabalhar, ou faça um fork do projeto, caso seja um desenvolvedor externo.
3. Desenvolva a sua solução fazendo [commits](#politica-de-commits) frequentes.
4. [Faça um PR](#politica-de-pull-requests) com o trabalho feito.

Lembre-se de seguir as políticas do projeto para a criação de issues, PRs, branches e commits.

## Politica de issues

As issues do projetos devem ser completas e explicativas, seguindo o template de issue do repositório:

```
## Descrição da issue

- Descrição da funcionalidade a ser feita

## Tasks:

[ ] - Passos a serem seguidos pela issue

## Critérios de aceitação:

[ ] - Critérios para a issue ser concluída
```

As issues devem seguir a seguinte estrutura:

- Um título conciso e descritivo;
- Uma descrição, seguindo o template do repositório, que deve incluir uma descrição completa da issue, uma lista de tasks para concluí-la e criterios para a aceitação da issue;
- Um *Assignee* responsável pela issue;
- *Labels* signaficativas;
- *Milestone* (sprint) em que a issue deve ser concluiída;
- *Estimated* (pontuação) atribuida a issue;

## Politica de branches

### Repositórios de desenvolvimento

Nos repositórios do código do projeto temos duas branches principais, a **master** e a **development**. 

#### master
A branch **master** é a branch mais estável do projeto, que estará em produção. Essa branch é protegida de commits e deve receber Pull Requests somente da brach **development**.

#### development
A branch **development** é a branch de desenvolvimento, onde as novas features desenvolvidas serão adicionadas. Os Pull Requests das novas branches devem ser feitos a ela, para depois de que a estabilidade do código estiver garantida, ser adicionada a **master**.

#### Novas branches
As branches para o desenvolvimento de novas features devem ser criadas a partir da branch **development** e devem seguir o padrão **x-nome-da-issue**, onde x é o número da issue que será resolvida na branch, acompanhado pelo nome da issue.

Os Pull Requests das novas branches devem ser feitos para a branch **development**.

Em casos de correções rápidas de bugs, a branch  deve seguir o padrão **FIX-x-problema-a-ser-resolvido**, onde x é o número da issue, caso tenha.

### Repositório de documentação

No repositório de documentação temos as branches **master** e **gh-pages**. Onde na **master** está o código da página de documentação do github pages e na branch **gh-pages** está o site compilado e em produção.

Assim como nos repositórios de desenvolvimento do projeto, no repositório de documentação a branch **master** está protegida e só deve aceitar modificações por Pull Requests, entretanto não há a branch **development** de forma que os Pull Requests devem ser feitos diretamente na **master**.

As novas branches, assim como nos repositórios de desenvolvimento devem seguir a estrutura **x-nome-da-issue**.

## Politica de commits

Os commits no durante o desenvolvimento do código devem frequentes, descritivos e concisos.

Os commits devem ser feitos utilizando o parametro **-s** para ter a assinatura do autor do commit. Caso o commit tenha sido feito em pareamento, deve constar no commit os co-autores.

O commit deve começar com `[x]`, sendo x o número da issue que está sendo desenvolvida.

Exemplo de commit:

```
git commit -sm "[7] Adicionando o guia de contribuição

Co-authored-by: Nome da dupla <emaildadupla@email.com>"
```
 
## Politica de Pull Requests (PRs)

Nos repositórios de desenvolvimento os PRs devem ser feitos para a branch **development**, enquanto no repositório de documentação, os PRs devem ser feitos a branch **master**.

Os Pull Requests devem ser feitos seguindo o template:

```
**Issue:** #X (sendo x o número da issue)

## Descrição
Descrição completa do que foi feitoo

```

Em casos de PRs em que ainda estão sendo desenvolvidos, deve ser acrescentado a sigla **WIP** antes do título do PR.

Os PRs devem conter:
- Um título conciso e descritivo;
- Um *Assignee* responsável pelo PR;
- Um *Reviewer* responsável pela revisão do PR;
- *Labels* signaficativas;
- Uma issue associada;
- Uma descrição, seguindo o template do repositório, que deve incluir uma descrição completa do que foi feito e a issue relacionada.

Os PRs só serão aceitos após passarem por uma revisão.