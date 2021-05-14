# Guia de Contribuição

Este é um documento para auxiliar a como contribuir para o projeto **2020.2-SiGeD**. O projeto é constituido de vários repositórios e esse guia é aplicado em todos eles. 

Orientamos que antes de começar a contribuir veja as [issues já abertas](https://github.com/fga-eps-mds/2020-2-SiGeD/issues).

## Como contribuir

Para contribruir com o projeto o processo é bem simples:

1. [Crie uma issue](#politica-de-issues) descrevendo a feature ou o problema a ser resolvido.
2. [Crie sua branch](#politica-de-branches) para trabalhar, ou faça um fork do projeto, caso seja um desenvolvedor externo.
3. [Desenvolva](#politica-de-desenvolvimento) a sua solução.
4. [Faça commits](#politica-de-commits) frequentes.
5. [Faça um PR](#politica-de-pull-requests) com o trabalho feito.

Lembre-se de seguir as políticas do projeto para a criação de issues, PRs, branches e commits.

## Politica de issues

As issues devem ser criadas no [repositório de documentação do projeto](https://github.com/fga-eps-mds/2020-2-SiGeD/).

As issues do projetos devem ser completas e explicativas, seguindo o template de issue do repositório.

As issues devem conter:

- Um título conciso e descritivo;
- Uma descrição, seguindo o template do repositório, que deve incluir uma descrição completa da issue e criterios para a aceitação;
- Um *Assignee* responsável pela issue;
- *Labels* signaficativas;
- *Milestone* (sprint) em que a issue deve ser concluiída;
- *Estimated* (pontuação) atribuida a issue;

## Politica de branches

### Repositórios de desenvolvimento

Nos repositórios do código do projeto temos uma branch principal, a **master**. 

#### master
A branch **master** é a branch mais estável do projeto, que estará em produção. Essa branch é protegida de commits e para o desenvolvimento de novas funcionalidades, deve receber Pull Requests (PRs).

#### Novas branches
As branches para o desenvolvimento de novas features devem ser criadas a partir da branch **master** e devem seguir o padrão **x-nome-da-issue**, onde x é o número da issue que será resolvida na branch, acompanhado pelo nome da issue.

Os Pull Requests das novas branches devem ser feitos para a branch **master**.

Em casos de correções rápidas de bugs, a branch  deve seguir o padrão **FIX-x-problema-a-ser-resolvido**, onde x é o número da issue, caso tenha.

### Repositório de documentação

No repositório de documentação temos as branches **master** e **gh-pages**. Onde na **master** está o código da página de documentação do github pages e na branch **gh-pages** está o site compilado e em produção.

Assim como nos repositórios de desenvolvimento do projeto, no repositório de documentação a branch **master** está protegida e só deve aceitar modificações por Pull Requests..

As novas branches, assim como nos repositórios de desenvolvimento devem seguir a estrutura **x-nome-da-issue**.

## Politica de desenvolvimento

O código deve ser escrito em Inglês, utilizando de camel case para a nomenclatura de variáveis.

O código deve estar no padrão do [guia de estilo do AirBnb](https://github.com/airbnb/javascript).

## Politica de commits

Os commits durante o desenvolvimento do código devem frequentes, descritivos e concisos.

Os commits devem ser feitos em inglês utilizando os verbos no imperativo.

Os commits devem ser feitos utilizando o parametro **-s** para ter a assinatura do autor do commit. Caso o commit tenha sido feito em pareamento, deve constar no commit os co-autores.

O commit deve começar com `[x]`, sendo x o número da issue que está sendo desenvolvida.

Exemplo de commit:

```
git commit -sm "[7] Add contributing guide

Co-authored-by: Nome da dupla <emaildadupla@email.com>"
```
 
## Politica de Pull Requests (PRs)

Os PRs devem ser feitos a branch **master**.

Os Pull Requests devem ser feitos seguindo o template:

```
**Issue:** closes #X (sendo #x o link para a issue x)

## Descrição
Descrição completa do que foi feito

```

Onde só deve ser utilizado o *closes* antes do link da issue, caso o PR resolva completamente a issue citada.

Caso o PR seja feito em um dos repositórios de desenvolvimento, o link para a issue do repositório de documentação é feito da seguinte forma: `fga-eps-mds/2020-2-SiGeD#x`, onde x é o número da issue. E no lugar de *closes* deve ser utilizado  ***resolves***.

Em casos de PRs em que ainda estão sendo desenvolvidos, deve ser acrescentado a sigla **WIP** antes do título do PR.

Os PRs devem conter:

- Um título conciso e descritivo;  
- Um *Assignee* responsável pelo PR;  
- Um *Reviewer* responsável pela revisão do PR;  
- *Labels* signaficativas;  
- Uma issue associada;  
- Uma descrição, seguindo o template do repositório, que deve incluir uma descrição completa do que foi feito e a issue relacionada.  

Os PRs só serão aceitos após passarem pelo CI estabelecido e por duas revisões.