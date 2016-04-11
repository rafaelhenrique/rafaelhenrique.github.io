Exercício: 04 - Agenda Pythônica - Grupo de Estudos Python
############################################################

:date: 2016-04-10 23:14
:tags: exercício, python, grupo de estudos python, sorocaba
:category: Python
:slug: exercicio-04-agenda-pythonica-grupo-de-estudos-python
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Exercício para resolução

Vamos fazer uma agenda!

Passo a passo...
----------------

* Passo 1: Primeiro receberemos os campos que o usuário vai querer na agenda. O usuário poderá digitar uma quantidade variável de campos. Exemplo de campos: data, nome, compromisso, observação, prioridade e etc.
    * Após receber estes campos você deverá criar as chaves respectivas de um dicionário usando estes nomes;
* Passo 2: Salve o formato (as keys do seu dicionário) da sua agenda em um arquivo texto (se quiser inovar pode ser um banco de dados também);
* Passo 3: Faça seu sistema ler o formato do dicionário e criar as keys quando ele rodar, caso ele não ache o arquivo com o formato ele deverá executar o passo 1 e 2 de novo;
* Passo 4: Depois que seu sistema leu o formato, receba as informações de compromisso (respeitando as keys do dicionário) do usuário e salve essas informações em outro arquivo (ou pode ser no mesmo apesar de eu achar isso mais complexo);
* Passo 5: Crie uma opção para que o usuário possa ler os compromissos cadastrados.

Para facilitar a resolução pense em dicionários, listas, tuplas e estruturas de repetição (for e while).

Importante
----------

**TODOS os passos devem ser feitos utilizando TDD, sempre pensando no teste primeiro e codificar depois! Esse exercício serve para ajudar a fixar a prática do TDD!**

Pode ser usado doctest e/ou unittest ou outra ferramenta qualquer que vocês queiram estudar/aprender. Entre doctest e unittest prefiro que vocês desenvolvam com unittest, pois é uma ferramenta melhor/mais usada (vocês conseguem vagas de emprego com isso) para vocês aplicarem no "mundo real".

Se ainda não se sentem confortáveis com o unittest é melhor entender bem o funcionamento dele antes de estudar novas ferramentas para teste.

Se vocês quiserem "inovar" e aprender ferramentas novas para teste recomendo algumas:

* `Pytest <http://pytest.org/latest/>`_
* `Nose <http://nose.readthedocs.org/en/latest/>`_
* `Behave <http://pythonhosted.org/behave/tutorial.html>`_
* `Lettuce <http://lettuce.it/tutorial/simple.html>`_

Não estou tirando o crédito do unittest, pelo contrário, acho uma ótima ferramenta, porém caso queiram estudar MAIS ou caso estejam com tempo sobrando convêm dar uma olhada nessas outras ferramentas.

Dicas extras
------------

Você poderá estudar o módulo `json <https://docs.python.org/3/library/json.html>`_ e o `file object <https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects>`_ do Python 3 para te ajudar na resolução.

A saída do seu sistema deverá ser algo similar a esta abaixo:

.. code-block:: console

        $ ls
        agenda.py

        $ python agenda.py
        Digite um campo novo [c=cancelar]: nome
        Digite um campo novo [c=cancelar]: dia
        Digite um campo novo [c=cancelar]: compromisso
        Digite um campo novo [c=cancelar]: ano
        Digite um campo novo [c=cancelar]: mes
        Digite um campo novo [c=cancelar]: c

        $ ls
        agenda.py  structure.json

        $ python agenda.py
        O que deseja fazer?
        1. Acrescentar compromissos
        2. Ler compromissos
        3. Sair
        2
        Nenhum compromisso cadastrado!
        O que deseja fazer?
        1. Acrescentar compromissos
        2. Ler compromissos
        3. Sair
        1
        Digite um novo valor para nome: Rafael
        Digite um novo valor para mes: Abril
        Digite um novo valor para ano: 2016
        Digite um novo valor para compromisso: Ir dormir
        Digite um novo valor para dia: 10
        O que deseja fazer?
        1. Acrescentar compromissos
        2. Ler compromissos
        3. Sair
        2
        nome: Rafael
        mes: Abril
        ano: 2016
        compromisso: Ir dormir
        dia: 10
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        O que deseja fazer?
        1. Acrescentar compromissos
        2. Ler compromissos
        3. Sair
        3

        $ ls
        agenda.py  structure.json  tasks.json

** Preste atenção ao ``ls`` que executei, em um primeiro momento criei somente o arquivo de estrutura (structure.json) e depois criei o arquivo contendo as tarefas (tasks.json)

Semana que vem posto a resolução!

That's all folks!
