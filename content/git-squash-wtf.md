Title: Git squash?? WTF?
Date: 2015-03-24 10:16
Tags: git, squash, github
Category: GIT
Author: Rafael Henrique da Silva Correia
Email: rafael@abraseucodigo.com.br
Slug: git-squash-wtf
Summary: Como fazer e pra que serve esse tal de git squash?

Galera conforme mencionei no post anterior.. estou contribuindo com o [puppetboard](https://github.com/puppet-community/puppetboard/) (mais informações no post abaixo desse :P). E fiz meu primeiro Pull Request e talz resolvendo uma questão que estava na issue para acrescentar uma nova funcionalidade ao projeto. Porém quando eu fiz meu PR (Pull Request) teve um cara que me disse o seguinte:

![comment-github-image](/images/git-squash-wtf_01.png "comment-github-image")
**[squash](http://www.git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Squashing-Commits)

Ai eu pensei como qualquer ótimo conhecedor do Git que porras é essa de squash?

O squash é uma prática utilizada para combinar mais de um commit em um commit só, desta forma eliminando "lixos" do projeto. Agora aqui neste post explicarei como raios você faz isso, pois não achei uma documentação simples que explicasse a uma pessoa normal como fazer isso, e após aprender, decidi TENTAR explicar de uma forma simples :smile:.

O projeto 
---------

Primeiro obviamente você precisa ter um repositório git, para isso eu criei um repositório BEEEM simples:  

```
$ mkdir teste  
$ cd teste  
$ git init  
$ echo "Rafael" >> README  
$ git add README  
$ git commit -m "Adicionado Rafael" 

$ echo "Henrique" >> README  
$ git add README  
$ git commit -m "Adicionado Henrique" 

$ echo "da" >> README
$ git add README  
$ git commit -m "Adicionado da" 

$ echo "Silva" >> README  
$ git add README  
$ git commit -m "Adicionado Silva" 

$ echo "Correia" >> README  
$ git add README  
$ git commit -m "Adicionado Correia"
```

Feito isso terei o seguinte histórico de commits:

```
$ git log --oneline  
4c03027 Adicionado Correia  
e23576b Adicionado Silva  
769bda9 Adicionado da  
2a71622 Adicionado Henrique  
5ebadcd Adicionado Rafael
```

O squash
---------

Agora vamos imaginar que eu quero fazer um squash a partir de Henrique, ou seja quero que os commits 2a71622, 769bda9, e23576b e 4c03027 sejam um só, pois todos tratam da adição do sobrenome no arquivo README. Para isso precisarei usar o comando rebase do git no commit que eu desejo, no caso a partir do Henrique (como é a partir do Henrique deveremos pegar 1 commit antes):

```
$ git rebase -i 5ebadcd
```

Após executar este comando será aberto um arquivo temporário para podermos fazer as alterações desejadas, o arquivo será similar a este abaixo:

```
pick 2a71622 Adicionado Henrique  
pick 769bda9 Adicionado da  
pick e23576b Adicionado Silva  
pick 4c03027 Adicionado Correia 

# Rebase 5ebadcd..4c03027 onto 5ebadcd  
#  
# Commands:  
#  p, pick = use commit  
#  r, reword = use commit, but edit the commit message  
#  e, edit = use commit, but stop for amending  
#  s, squash = use commit, but meld into previous commit  
#  f, fixup = like "squash", but discard this commit's log message  
#  x, exec = run command (the rest of the line) using shell  
#  
# These lines can be re-ordered; they are executed from top to bottom.  
#  
# If you remove a line here THAT COMMIT WILL BE LOST.  
#  
# However, if you remove everything, the rebase will be aborted.  
#  
# Note that empty commits are commented out
```

Neste mesmo arquivo já podemos visualizar algumas opções do que fazer com esses commits, para este post utilizaremos somente o squash, mas vale a pena conhecer as outras opções descritas abaixo de commands. Agora altere este arquivo da seguinte maneira:

```
pick 2a71622 Adicionado Henrique  
squash 769bda9 Adicionado da  
squash e23576b Adicionado Silva  
squash 4c03027 Adicionado Correia 

# Rebase 5ebadcd..4c03027 onto 5ebadcd  
#  
# Commands:  
#  p, pick = use commit  
#  r, reword = use commit, but edit the commit message  
#  e, edit = use commit, but stop for amending  
#  s, squash = use commit, but meld into previous commit  
#  f, fixup = like "squash", but discard this commit's log message  
#  x, exec = run command (the rest of the line) using shell  
#  
# These lines can be re-ordered; they are executed from top to bottom.  
#  
# If you remove a line here THAT COMMIT WILL BE LOST.  
#  
# However, if you remove everything, the rebase will be aborted.  
#  
# Note that empty commits are commented out
```

As linhas dos commits 769bda9, e23576b e 4c03027 foram mudadas para squash, portanto serão combinados ao commit que possui a o nome pick, então o commit 2a71622 agora será unido aos 3 commits abaixo dele. É importante comentar que o squash não remove os logs (mensagens dos commits) conforme a descrição do "Commands" já a opção fixup descarta os logs. Feita esta alteração basta salvar o arquivo e sair. Feito isso será apresentado outro arquivo similar a este abaixo:

```
# This is a combination of 4 commits.  
# The first commit's message is:  
Adicionado Henrique  
# This is the 2nd commit message:  
Adicionado da  
# This is the 3rd commit message:  
Adicionado Silva  
# This is the 4th commit message:  
Adicionado Correia  
# Please enter the commit message for your changes. Lines starting  
# with '#' will be ignored, and an empty message aborts the commit.  
#  
# Date:      Tue Mar 24 11:08:29 2015 -0300  
#  
# rebase in progress; onto 5ebadcd  
# You are currently editing a commit while rebasing branch 'master' on '5ebadcd'.  
#
```

Neste arquivo você poderá mudar as mensagens de log (mensagens dos commits) caso desejar, se desejar mude alguma coisa e salve e saia do arquivo. Terminada a edição/salvamento deste arquivo você acabou o squash! Podemos ver no log como ficou a nova estrutura:

```
$ git log --oneline  
f4c9d80 Adicionado Henrique  
5ebadcd Adicionado Rafael 
```

Ou:  

```
$ git log  
commit f4c9d80a089ee35fca0eb7c6e5aabcb435fb9bb4  
Author: Rafael Henrique da Silva Correia <rafael@abraseucodigo.com.br>  
Date:   Tue Mar 24 11:08:29 2015 -0300  
    Adicionado Henrique  

    Adicionado da  

    Adicionado Silva  

    Adicionado Correia

commit 5ebadcde3eb8c006bd33ee4c62f9cbb359822d6e  
Author: Rafael Henrique da Silva Correia <rafael@abraseucodigo.com.br>  
Date:   Tue Mar 24 11:08:14 2015 -0300  
    Adicionado Rafael
```

Conclusão
---------

Esta prática é bem interessante e deixa o repositório do git mais limpo, é MUITO válida principalmente em projetos grandes onde se tem muitos contribuidores (principalmente em projetos open source :smile:).
