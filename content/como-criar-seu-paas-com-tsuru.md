Title: Como criar seu PaaS com Tsuru
Date: 2015-09-22 22:48
Tags: deploy, tsuru, paas
Category: Deploy
Author: Rafael Henrique da Silva Correia
Email: rafael@abraseucodigo.com.br
Slug: como-criar-seu-paas-com-tsuru
Summary: Como criar um PaaS simples para deploy de aplicações com Tsuru

Começo este post dizendo que gostei bastante da proposta do Tsuru. 

Mas o que é o Tsuru?
--------------------

Tsuru é um software que você pode criar seu próprio [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) explicando de forma simples, você tem um [Heroku](https://www.heroku.com/)/[Openshift](https://www.openshift.com) pessoal onde você tem controle completo na máquina e você pode fazer o que bem entender.

E pra que serve esse tal Tsuru?
-------------------------------

Serve para você fazer deploy de suas aplicações de forma BRUTALMENTE RÁPIDA, com a vantagem de não pagar nada para o Openshift nem para o Heroku, mesmo que seja uma aplicação grande e pesada, quem vai gerenciar os recursos é você mesmo, então se sua máquina "explodir" a culpa será sua, pois você tem controle absoluto sobre os recursos da máquina em que você irá instalar o Tsuru.

Quem é o pai do Tsuru?
----------------------

O pai do Tsuru (pelo que eu sei pelo menos) é o Andrews Medina, e este cara começou a desenvolver o Tsuru dentro da Globo.com. Podemos ver até na doc do Tsuru o Copyright da Globo.com, isso fica bem evidente que a Globo.com tem um dedinho ai.

O Andrews Medina também fez inúmeros vídeos no YouTube muito bons explicando mais sobre o Tsuru, recomendo TODOS.. principalmente os três abaixo:

- [tsuru - fazendo deploys de forma simples e divertida](https://www.youtube.com/watch?v=YD3iNEBb4t0)
- [Garoa Hacker | Entrevista: Andrews Medina (possui 3 partes)](https://www.youtube.com/watch?v=h68DCFFXGW0)
- [Garoa Hacker Club | Andrews Medina - Tsuru Live Code](https://www.youtube.com/watch?v=dC79RpifEQI)

Por que raios eu estou falando do Tsuru?
----------------------------------------

Volto a dizer... achei SENSACIONAL o deploy realizado pelo Tsuru, extremamente rápido e seguro. Então ontem eu subi o meu PaaS utilizando o Tsuru :raised_hands:.

Procedimentos básicos
---------------------

A doc do Tsuru é excelente e pode ser lida [aqui](http://docs.tsuru.io/en/stable/understanding/index.html), mas tem um porém, caso você seja apenas um xereta (assim como eu), não recomendo fazer a instalação através dessa doc, pois você irá travar assim como eu no passo [Adding Nodes](http://docs.tsuru.io/en/stable/installing/adding-nodes.html) muito provavelmente. 

Neste "Adding Nodes" é o passo onde você terá que adicionar uma *instância de IaaS da [Amazon EC2](https://aws.amazon.com/pt/ec2/) ou de [Apache CloudStack](https://cloudstack.apache.org/), por isso eu disse que você provavelmente vai travar se for um curioso, por que?

- pois no EC2 você terá que pagar a instância, que é uma coisa que provavelmente você não vai querer fazer a princípio
- e o CloudStack não é pago, porém extremamente complexo, pelo menos eu achei

Portanto minha escolha óbvia foi fazer o "procedimento mais fácil" (dica do @rpedigoni) que é usar o [Tsuru Now](https://github.com/tsuru/now).

\* Não sei se o nome certo para o CloudStack é instância, se eu estiver errado me desculpem

Procedimento "mais fácil"
-------------------------

Cara por que eu coloquei essas aspas ai? 

Meu, o Tsuru Now é um script em Shell bem antiguinho (pelo menos ao meu ver) e ele não é tão intuitivo como promete, creio que na época que ele foi criado ele deveria ser mais fácil de usar, mas agora devido ao tempo e versões mais novas de sistema operacional ele se tornou meio obsoleto.

Mas mesmo obsoleto galera, eu ainda recomendo esse cara, pois se você aprender a domá-lo você consegue subir o Tsuru bem tranquilão.

Ferramentas utilizadas
----------------------

Para subir o meu Tsuru estou utilizando:

- [Tsuru Now](https://github.com/tsuru/now)
- [Um droplet da Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-digitalocean-droplet-virtual-server)
    - S.O. Ubuntu 14.04 x64
    - 512MB Ram 
    - 20GB SSD Disk 
    - New York 3
    - Neste droplet a configuração default da Digital Ocean é vir 2 interfaces de rede, uma eth0 que será o ip externo e a lo que representa o loopback
    - Valor desse cara $5 por mês

Caso você não queira pagar absolutamente NADA também é possível, você só terá o trabalho de configurar as interfaces da sua máquina física (ou virtual, sei lá) e instalar o Ubuntu 14.04 x64 (o x32 eu não testei e não sei se funciona bem!).

Problemas encontrados logo no começo
------------------------------------

No repositório do [github do Tsuru Now](https://github.com/tsuru/now) tem algumas informações faltantes a respeito da compatibilidade com os Sistemas operacionais. Lá no README ele menciona que este script funciona em Debian e Ubuntu, mas não diz a versão :pensive:.

Eu como um bom paranóico amante de Debian, fui logo criando um droplet na Digital Ocean com o Debian mais novo que encontrei o 8.1~8.2 (Jessie Stable), ai rodei o script conforme manda o README:

```
# curl -sL https://raw.githubusercontent.com/tsuru/now/master/run.bash | bash
```

Coisa linda pra se ver.... massss... não consegui nem ir até 50% da instalação, logo de cara falta o pacote linux-image-extras-* no Debian, e adicionar repositórios começa a ficar meio impraticável pois eu como um bom paranóico, acredito, que se ele não está no repositório main alguma razão deve ter.

Eis que pensei *"pooo... se não vai Debian, os caras devem gostar de Ubuntu... vamos de Ubuntu"*, ai novamente como um bom paranóico fui logo escolhendo a versão MAIS NOVA do Ubuntu, a versão 15.04 x64.... e adivinhem?? Problema de novo.... se não me engano com o mesmo pacote.

Ai novamente como um bom brasileiro que não desiste nunca fui de novo agora pensei *"poooo.... se os caras não gostam desse Ubuntu vou usar o Ubuntu que está referenciado na doc oficial do Tsuru"* que vem a ser o 14.04 ! 

E desta vez fiz progressos significativos, MUITO SIGNIFICATIVOS e consegui concluir cerca de 80% da instalação e o script foi dar pau lá pelo finalzinho próximo da `linha 671` quando ele chama a função `config_tsuru_post`.

Ai começa meu instinto de programador maluco e fui depurando a parada. Pelo que pude ver o script não estava pegando meu ip externo adequadamente.

Variáveis/adaptação e funcionamento completo
--------------------------------------------

Como o Tsuru Now não conseguia pegar meu ip corretamente fui lá e comecei a testar coisas de modo que fizesse o filho da mãe funcionar. Eis que por fim eu consegui, e vou dar a receita de bolo pra vocês. Clone o repositório do Tsuru Now inicialmente:

```
# git clone git@github.com:tsuru/now.git
```

Nas primeiras linhas do script chamado `run.bash` tem algumas variáveis interessantes:

```
1  #!/bin/bash -ue
2 
3  # Copyright 2015 tsuru-now authors. All rights reserved.
4  # Use of this source code is governed by a BSD-style
5  # license that can be found in the LICENSE file.
6 
7  set -eu
8
9  release=""
10 codename=""
11 host_ip=""
12 private_ip=""
13 host_name=""
14 set_interface=""
15 is_debug=""
16 docker_node=""
17 set_interface=""
```

Destas 17 linhas as variáveis que resolveram minha vida foram `host_ip` e `private_ip`, nestas duas eu setei meu ip **EXTERNO (ou seja o ip que a galera de fora da sua rede vê)**, caso você tenha dúvidas qual é seu ip externo recomendo olhar no site [What Is My Ip?](https://www.whatismyip.com/) que lá ele vai te mostrar o seu ip externo(mas faz o favor de olhar da máquina que você está instalando o Tsuru :joy:).

Feito isso rodei o script novamente da seguinte maneira (você precisará executar como root, ou usando sudo):

```
# bash run.bash --host-ip <meu ip externo> | tee log_run.log
```

Troque <meu ip externo\> pelo seu ip externo. 

Executando esse comando vá tomar banho, comer, tomar café ou outra coisa desse tipo, pois vai demorar um pouco (calculo pelo menos uns 15 minutos caso você não use um hd SSD).

Usei o comando `| tee log_run.log` para que ele gere um arquivo contendo todo output (erros e não erros) do script, se você quiser analisar depois como foi a instalação ficará mais fácil você ler este arquivo.

Finish him!
-----------

Se tudo correr bem ao fim dessa execução seu Tsuru já vai estar funcionando de forma básica pronta para testes bacaninhas. É importante em um primeiro momento alterar a senha do admin e rodar `source ~/.bashrc` conforme manda o próprio Tsuru Now:

```
######################## DONE! ########################

Some information about your tsuru installation:

Admin user: admin@example.com
Admin password: admin123 (PLEASE CHANGE RUNNING: tsuru change-password)
Target address: http://<meu ip externo>:8080
Dashboard address: http://<meu ip externo>:32768

You should run `source ~/.bashrc` on your current terminal.
```

Para alterar a senha você poderá usar o comando `tsuru change-password`. Após você ter seu PaaS instalado e funcional recomendo assistir o vídeo do Andrews para dar seus primeiros passinhos utilizando o tsuru-cli, um vídeo ótimo para começar é este [tsuru - fazendo deploys de forma simples e divertida](https://www.youtube.com/watch?v=YD3iNEBb4t0).

Espero que tenha gostado do post, deixe seus comentários ali embaixo :point_down:.

Flw!
