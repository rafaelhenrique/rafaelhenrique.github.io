Resolução exercício: 02 - Média de alunos - Grupo de Estudos Python
###################################################################

:date: 2016-03-16 21:56
:tags: exercício, python, grupo de estudos python, sorocaba, estruturas de repetição, for, lista, dicionários
:category: Python
:slug: resolucao-02-media-de-alunos-grupo-de-estudos-python
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Resolução do exercício média de alunos passado no Grupo de Estudos Python

Dia 07/03 postei um exercício para resolução, fazer um cálculo de média ponderada de notas de alunos, o post contendo o enunciado pode ser `visto aqui <http://blog.abraseucodigo.com.br/exercicio-02-media-de-alunos-grupo-de-estudos-python.html>`_.

O código lixo que eu fiz no Hangout
-----------------------------------

Lixo é um nome muito forte, vamos chamar de RUIM somente por favor. Quando brincamos de live coding as coisas todas são diferentes do seu mundo real, devido a pressão, ou alguma coisa que passa na sua cabeça.

No live coding que fiz no Hangout tentei focar em muitas técnicas para manipulação de dicionários e listas, espero que isso tenha ficado claro no vídeo da `aula 04 disponível neste post <http://blog.abraseucodigo.com.br/video-04-grupo-de-estudos-python.html>`_. 

Então vamos ao código que mencionei:

.. code-block:: python

    # -*- coding: utf-8 -*-

    bimestre_final = 6

    notas = {
        "aluno1": [],
        "aluno2": [],
    }

    notas = {}
    alunos = ["Alexsandro", "Arieh"]
    bimestres = ["{} Bim".format(numero) for numero in range(1, 7)]

    # esse é o for sem a list comprehenssion ai de cima
    #
    # bimestres = []
    # for numero in range(1, 7):
    #    bimestres.append("{} Bim".format(numero))
    #

    pesos = {
        "1 Bim": 2.0,
        "2 Bim": 3.0,
        "3 Bim": 3.0,
        "4 Bim": 4.0,
        "5 Bim": 5.0,
        "6 Bim": 5.0,
    }

    for aluno in alunos:
        print("Aluno: ", aluno)
        notas[aluno] = {}
        for bimestre in bimestres:
            nota = input("Digite a nota do {}: ".format(bimestre))
            nota = float(nota)
            notas[aluno][bimestre] = nota

    # (7*2 + 5*3 + 3*3 + 10*4 + 9*5 + 8*5) /
    # (2 + 3 + 3 + 4 + 5 + 5) = 7.40
    numerador = {}
    denominador = {}
    for aluno in alunos:
        numerador[aluno] = 0
        denominador[aluno] = 0
        for bimestre, nota in notas[aluno].items():
            peso = pesos[bimestre]
            numerador[aluno] += nota * peso
            denominador[aluno] += peso

    resultado_final = {}
    for aluno in alunos:
        resultado_final[aluno] = numerador[aluno] / denominador[aluno]

    # Nota maior que 9 teve menção A
    # Nota maior que 7 e menor ou igual a 9 teve menção B
    # Nota maior que 5 e menor ou igual a 7 teve menção C
    # Nota menor que 5 teve menção D

    for nome, nota in resultado_final.items():
        print("Nota final {}: {}".format(nome, nota))

        if nota > 9:
            print("Nota A")
        elif 9 >= nota > 7:
            print("Nota B")
        elif 7 >= nota > 5:
            print("Nota C")
        else:
            print("Nota D")

Vamos analisar os problemas deste código acima:

1. Tem muitos fors ai galera, isso vai ficar lento, bem lento mesmo;
2. As exceptions não estão tratadas de forma legal, mas você poderá estudar mais sobre isso lendo `este post <http://blog.abraseucodigo.com.br/resolucao-01-calculadora-basica-grupo-de-estudos.html>`_, considere isso um exercício;
3. O código não está pythônico, limpo e claro, tem muita coisa que faz muita coisa.

Refatorando as variáveis e dicionários
--------------------------------------

Começando do início:

.. code-block:: python

    # -*- coding: utf-8 -*-

    bimestre_final = 6

    notas = {
        "aluno1": [],
        "aluno2": [],
    }

    ... linhas omitidas ...

Este dicionário de ``notas`` não é muito necessário, pois quando eu recebo a nota do aluno eu já posso ir calculando durante a execução do primeiro for, isso é legal pois vai fazer com que a gente ganhe velocidade.

A variável ``bimestre_final`` é inútil também, pois como tenho uma lista com todos os bimestres abaixo deste trecho eu sei o número de bimestres que eu tenho a partir do dicionário intitulado como ``bimestres``.

Só ai já eliminei duas coisas inúteis no script. Continuando:

.. code-block:: python

    ... linhas omitidas ...

    bimestres = ["{} Bim".format(numero) for numero in range(1, 7)]

    ... linhas omitidas ...

O que acham deste `list comprehenssion <https://docs.python.org/3.5/tutorial/datastructures.html#list-comprehensions>`_? Este cara está mais ou menos bacana. Existem outras formas mais simples de escrever este cara, justamente porque são somente 6 bimestres. Soluções aceitáveis:

* Primeira forma: Mais legível

.. code-block:: python

    ... linhas omitidas ...

    bimestres = [
        "1 Bim",
        "2 Bim",
        "3 Bim",
        "4 Bim",
        "5 Bim",
        "6 Bim",
    ]

    ... linhas omitidas ...

* Segunda forma: Mais "chata"

.. code-block:: python

    ... linhas omitidas ...

    bimestres = []
    for numero in range(1, 7):
       bimestres.append("{} Bim".format(numero))

    ... linhas omitidas ...

* Terceira forma: "Splitada"

.. code-block:: python

    ... linhas omitidas ...

    bimestres = "1-Bim 2-Bim 3-Bim 4-Bim 5-Bim 6-Bim".split()

    ... linhas omitidas ...

Eu particularmente opto pela ``Primeira forma`` ou pela ``Terceira forma`` como estou optando por legibilidade e sem muita complexidade para este post vou escolher a primeira.

A ``Terceira forma`` achei legal mostrar, pois o bacana disso é que o `split <https://docs.python.org/3/library/stdtypes.html#str.split>`_ (que pode ser usado com strings) irá dividir a string onde tem os espaços, transformando assim essa string comprida em uma lista, que praticamente daria o mesmo resultado também (exceto pelo sinal do hífen).

O caso do dicionário ``pesos`` achei bacana, não vou mexer, mas aceito sugestões, se acharem uma solução mais legal me contem por favor.

Depois dessa primeira refatorada, comecei a criar um novo script, que ficou com o começo deste jeito:

.. code-block:: python
    
    # -*- coding: utf-8 -*-

    alunos = [
        "Rafael1",
        "Rafael2"
    ]
    bimestres = [
        "1 Bim",
        "2 Bim",
        "3 Bim",
        "4 Bim",
        "5 Bim",
        "6 Bim",
    ]
    pesos = {
        "1 Bim": 2.0,
        "2 Bim": 3.0,
        "3 Bim": 3.0,
        "4 Bim": 4.0,
        "5 Bim": 5.0,
        "6 Bim": 5.0,
    }
    numerador = {}
    denominador = sum(pesos.values())

Eu particularmente achei bem mais bonito e claro de entender as coisas. Só tem uma coisa diferente ai, que a é função ``sum`` que já é padrão do Python e faz soma de valores de um iterador, vamos ver como isso funciona:

.. code-block:: console

    $ python
    Python 3.5.1 (default, Feb 22 2016, 23:22:06) 
    [GCC 4.9.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> pesos = {
    ...         "1 Bim": 2.0,
    ...         "2 Bim": 3.0,
    ...         "3 Bim": 3.0,
    ...         "4 Bim": 4.0,
    ...         "5 Bim": 5.0,
    ...         "6 Bim": 5.0,
    ...     }
    >>> pesos.values()
    dict_values([5.0, 2.0, 4.0, 5.0, 3.0, 3.0])
    >>> type(pesos.values())
    <class 'dict_values'>
    >>> sum(pesos.values())
    22.0
    >>> lista = [1, 2, 3, 4, 5, 6]
    >>> sum(lista)
    21
    >>> sum(range(1,100))
    4950
    >>> pesos.keys()
    dict_keys(['5 Bim', '1 Bim', '4 Bim', '6 Bim', '3 Bim', '2 Bim'])
    >>> sum(pesos.keys())
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

Olhe que curioso esse teste acima, quando uso ``pesos.values()`` pego todos os valores do dicionário pesos em forma de iterável (assunto pra outra hora o que é um iterável), ai quando uso ``sum`` somo todos esses valores e o resultado é 22. 

Consigo somar também listas, e também consigo somar um range de números gerados a partir da função ``range``. Porém quando tento somar strings (que são minhas keys do dicionário pesos) isso me retorna um erro dizendo que não consigo somar int e strings, essa soma não é possível. Espero que com esse exemplo tenha ficado claro o uso da função ``sum``. Mais informações na `documentação do Python <https://docs.python.org/3/library/functions.html#sum>`_.

Refatorando os loops
--------------------

Depois de organizar melhor as variáveis/dicionários e listas que vamos trabalhar fica mais fácil organizar os nossos loops, vamos ver como ficou o script completo:

.. code-block:: python

    # -*- coding: utf-8 -*-

    alunos = [
        "Rafael1",
        "Rafael2"
    ]
    bimestres = [
        "1 Bim",
        "2 Bim",
        "3 Bim",
        "4 Bim",
        "5 Bim",
        "6 Bim",
    ]
    pesos = {
        "1 Bim": 2.0,
        "2 Bim": 3.0,
        "3 Bim": 3.0,
        "4 Bim": 4.0,
        "5 Bim": 5.0,
        "6 Bim": 5.0,
    }
    numerador = {}
    denominador = sum(pesos.values())

    for aluno in alunos:
        print("Aluno: ", aluno)
        numerador[aluno] = 0
        for bimestre in bimestres:
            nota = input("Digite a nota do {}: ".format(bimestre))
            nota = float(nota)
            numerador[aluno] += nota * pesos[bimestre]

        media = numerador[aluno] / denominador
        print("Nota final {}: {:.2f}".format(aluno, media))

        if media > 9:
            print("Nota A")
        elif 9 >= media > 7:
            print("Nota B")
        elif 7 >= media > 5:
            print("Nota C")
        else:
            print("Nota D")

        print("*"*20)

Agora sim! Ficou um script clean, mais pythônico do que era antes. De 6 loops reduzi para 2 loops somente.

A criação de um dicionário dinamicamente ainda é usada na linha ``numerador[aluno] = 0`` porém de forma bem mais simples, somente é inicializado com 0 para poder ir somando as notas do aluno no numerador da nossa equação. Para entender como ficou a estrutura do nosso dicionário numerador veja o exemplo abaixo:

.. code-block:: console
    
    $ python media_alunos_dict.py 
    Aluno:  Rafael1
    Digite a nota do 1 Bim: 7
    Digite a nota do 2 Bim: 5
    Digite a nota do 3 Bim: 3
    Digite a nota do 4 Bim: 10
    Digite a nota do 5 Bim: 9
    Digite a nota do 6 Bim: 8
    > /home/rafael/Dropbox/Grupo de estudos Python/nivel_mediano/media_ponderada/media_alunos_dict.py(35)<module>()
         34     import ipdb; ipdb.set_trace()
    ---> 35     media = numerador[aluno] / denominador
         36     print("Nota final {}: {:.2f}".format(aluno, media))

    ipdb> numerador
    {'Rafael1': 163.0}

O numerador terá uma chave para cada nome de aluno contendo a soma total realizada. Neste exemplo foi realizado o seguinte cálculo no numerador do aluno ``Rafael1``: ``(7*2 + 5*3 + 3*3 + 10*4 + 9*5 + 8*5) = 163.0``

Quando continuo a execução do script temos:

.. code-block:: console
    ipdb> c
    Nota final Rafael1: 7.41
    Nota C
    ********************
    Aluno:  Rafael2
    Digite a nota do 1 Bim: 5
    Digite a nota do 2 Bim: 4
    Digite a nota do 3 Bim: 6
    Digite a nota do 4 Bim: 7
    Digite a nota do 5 Bim: 8
    Digite a nota do 6 Bim: 10
    > /home/rafael/Dropbox/Grupo de estudos Python/nivel_mediano/media_ponderada/media_alunos_dict.py(34)<module>()
         33 
    ---> 34     import ipdb; ipdb.set_trace()
         35     media = numerador[aluno] / denominador

    ipdb> numerador
    {'Rafael1': 163.0, 'Rafael2': 158.0}

Neste caso cálculo realizado para o aluno ``Rafael2`` é: ``(5*2 + 4*3 + 6*3 + 7*4 + 8*5 + 10*5) = 158.0``

Conclusão
---------

Espero que ao final dessa solução refatorada do live coding que rolou na `aula 04 <http://localhost:8000/video-04-grupo-de-estudos-python.html>`_, você tenha entendido mais coisas sobre listas, dicionários e estruturas de repetição. Caso tenha alguma dúvida/sugestão/crítica comenta ai.

That's all folks!
