Usando vetores em Shell Script
##############################

:date: 2018-01-09 20:33
:tags: shell script, bash, shell
:category: Shell Script
:slug: usando-vetores-em-shell-script
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Como usar vetores em Shell Script e como eles podem me ajudar?

Eu assumo! Eu sou um shelleiro!

Gosto muito de Shell Script e já cheguei a trabalhar cerca de 2 anos programando com Shell Script em uma empresa muito massa chamada `Automalógica <http://www.automalogica.com.br/>`_, onde eu desenvolvia scripts em Shell para geração de bases de um sistema `SCADA <https://pt.wikipedia.org/wiki/Sistemas_de_Supervis%C3%A3o_e_Aquisi%C3%A7%C3%A3o_de_Dados>`_ em específico chamado `SAGE <http://www.cepel.br/produtos/sage-sistema-aberto-de-gerenciamento-de-energia.htm>`_, muitos e muitos parsers desenvolvidos.

Como eu gosto muito de Shell sempre vejo algumas vantagens no seu uso como:

- Ser uma ótima linguagem de programação (me desculpem os puristas que não gostam que fale que Shell é uma linguagem) para administração de sistemas GNU/Linux, pois você consegue usar todos os comandos disponíveis dentro da programação;
- Ser rápida para codificar coisas simples;
- Funciona em todo sistema operacional Linux e até alguns que não são Linux, pois geralmente a galera usa `Bash (Bourne again Shell) <https://pt.wikipedia.org/wiki/Bash>`_ para codificar.

Porém cuidado! Muito Shell pode dificultar sua vida. Shell não tem estruturas complexas de dados e muito menos orientação a objeto e coisas do tipo o que faz com que programas muito grandes fiquem impossíveis de serem mantidos.

Para que você pode usar vetores em Shell Script?
------------------------------------------------

Vetores ou arrays são conhecidos em muitas linguagens de programação principalmente para a finalidade de iterar sobre um conjunto de elementos usando alguma estrutura de iteração (for, while, do/while, etc), e em Shell Script não é diferente.

Vamos a um exemplo didático disso, imagine que eu gostaria de pegar a primeira coluna de um csv e criar pastas/diretórios com esses nomes:

.. code-block:: bash

    #!/bin/bash

    FIRST_COLUMN=( $(awk -F"," '(NR>1){print $1}' arquivo.csv) )

    for((cont=0;cont<${#FIRST_COLUMN[@]};cont++)); do
        mkdir ${FIRST_COLUMN[$cont]}
    done


Considerando que a estrutura do meu arquivo csv fosse algo parecido com isso abaixo:

.. code-block:: command

    $ cat arquivo.csv
    diretorios,status
    teste1,false
    teste2,false

Ao executar este script eu teria os seguintes diretórios criados: `teste1` e `teste2`.


Como essa mágica acontece?
--------------------------

Para entender como isso acontece primeiro temos que entender como criamos um vetor em Shell Script, vamos criar um vetor que contem as strings `a`, `b` e `c` em nosso terminal:

.. code-block:: command

    $ MEU_VETOR=('a' 'b' 'c')

Estou usando `$` somente para representar que estou digitando um comando em meu terminal do sistema, não é necessário você escrever este `$`. Repare que nem preciso criar um arquivo de Shell Script (.sh) para fazer isso, posso fazer diretamente no terminal.

Os elementos do vetor são separados por espaços, para pegar cada elemento separadamente podemos fazer assim:

.. code-block:: command

    $ echo ${MEU_VETOR[0]}
    a
    $ echo ${MEU_VETOR[1]}
    b
    $ echo ${MEU_VETOR[2]}
    c

Para pegar todos os elementos de uma vez podemos fazer:

.. code-block:: command

    $ echo ${MEU_VETOR[@]}
    a b c

E por fim para pegar a quantidade de elementos que temos neste vetor podemos fazer:

.. code-block:: command

    $ echo ${#MEU_VETOR[@]}
    3

Sabendo desses conceitos separadamente fica fácil iterar no vetor, veja só:

.. code-block:: command

    $ for ((cont=0; cont<${#MEU_VETOR[@]}; cont++)); do echo "-> ${MEU_VETOR[$cont]}"; done
    -> a
    -> b
    -> c

Coloquei uma setinha `->` no comando `echo` só para ficar mais bonito :), mas não é necessário.

Entendendo o awk que foi usado no primeiro exemplo
--------------------------------------------------

O `awk <http://tldp.org/LDP/abs/html/awk.html>`_ é um comando muito poderoso do GNU/Linux e novamente me desculpem os puristas, mas pra mim é uma outra linguagem de programação, pois tem loops, condicionais e etc apesar de ter uma característica similar ao Shell Script em ser muito ruim para criar sistemas grandes, pois não possui estruturas de dados complexas.

No primeiro exemplo usei 0,00000001% do que o awk oferece, ele até é digno de outro post no futuro. Vamos as explicações, se você executar o awk de forma bem simplista no arquivo exemplo olhe o que vai acontecer:

.. code-block:: command

    $ cat arquivo.csv # somente para vcs lembrarem da estrutura do arquivo
    diretorios,status
    teste1,false
    teste2,false

    $ awk -F"," '{print $1}' arquivo.csv
    diretorios
    teste1
    teste2

Bem simples né? Ele usa como delimitador dos campos a vírgula devido ao parâmetro `-F` e faz um `print` da primeira coluna. Agora o legal é que da pra ignorar a primeira linha com o `NR` que é um nome reservado do awk que significa `NUMBER ROW`, veja só:

.. code-block:: command

    $ awk -F"," '(NR>1) {print $1}' arquivo.csv
    teste1
    teste2

Agora é simples! É só jogar o resultado deste comando em um vetor e é só alegria.... veja:

.. code-block:: command

    $ MEU_VETOR=( $(awk -F"," '(NR>1) {print $1}' arquivo.csv) )
    teste1
    teste2

O `$(<comando>)` é uma sintaxe do bash para executar um comando e trazer seu resultado para uma variável, que no caso nossa variável é o nosso vetor e justamente por isso preciso dos parênteses para especificar que é um vetor.

Conclusão
---------

Este foi apenas um exemplo simples de como os vetores em Shell Script podem lhe ajudar no dia a dia, exemplos de outras coisas em que já precisei usá-los:

- Rodar vários comandos de banco de dados iterando comando a comando;
- Copiar arquivos para diversas máquinas ao mesmo tempo por ssh iterando pelas máquinas;
- Criar backup de diversos diretórios iterando um a um para realizar o backup.

As opções são infinitas!

Como recomendações finais, se você gostou desse post `clique aqui veja esta palestra do Aurélio Jargas no FISL 17 <https://www.youtube.com/watch?v=XBkBnKmu94U>`_, é muito massa! Também deixo a dica do Canivete Suíço do Shell (Bash) também do Aurélio, `clique aqui <http://aurelio.net/shell/canivete/>`_ para dar uma conferida.

Conta aqui pra nós depois nos comments pra que você precisou usar ou está afim de usar Shell Script e seus vetores ;)

Flw!