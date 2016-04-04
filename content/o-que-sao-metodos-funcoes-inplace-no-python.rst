O que são métodos/funções in-place no Python?
#############################################

:date: 2016-04-04 16:36
:tags: python, inplace, metodos, builtin, in-place
:category: Python
:slug: o-que-sao-metodos-funcoes-inplace-no-python
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: O que são estes métodos in-place? Onde vivem? Do que se alimentam?

Métodos/funções in-place no Python são carinhas que alteram o objeto original ao executar determinada funcionalidade.

IN PLACE
--------

Vamos a um exemplo prático:

.. code-block:: console

    $ ipython
    Python 3.5.1 (default, Feb 10 2016, 10:59:15) 
    Type "copyright", "credits" or "license" for more information.

    IPython 4.1.2 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: teste = ['a', 'b', 'c']

    In [2]: teste.reverse
    teste.reverse

    In [2]: teste.reverse?
    Docstring: L.reverse() -- reverse *IN PLACE*
    Type:      builtin_function_or_method

    In [3]: reversed?
    Init signature: reversed(self, /, *args, **kwargs)
    Docstring:
    reversed(sequence) -> reverse iterator over values of the sequence

    Return a reverse iterator
    Type:           type

** Neste exemplo (utilizando o ipython) usei um recurso bem bacana do ipython que mostra a docstring de um método/função python utilizando o caractere ``?``, usem isso é bem legal :)

Podemos ver que de acordo com a docstring do método ``reverse`` de uma lista chamada ``teste`` o método ``reverse`` é IN PLACE, ao contrário da função `reversed <https://docs.python.org/3/library/functions.html#reversed>`_ (builtin do Python) que não é IN PLACE. Bem ai já temos uma ideia de como começar nossos estudos. Vamos ver o que o método ``reverse`` da lista ``teste`` é capaz de fazer:

.. code-block:: console

    In [6]: id(teste)
    Out[6]: 140323076029960

    In [7]: teste
    Out[7]: ['a', 'b', 'c']

    In [8]: teste.reverse()

    In [9]: id(teste)
    Out[9]: 140323076029960

    In [10]: teste
    Out[10]: ['c', 'b', 'a']

* execução [6]: eu usei uma função também builtin do Python chamada `id <https://docs.python.org/3/library/functions.html#id>`_ que retorna a identidade de um objeto Python, o endereço retornado é o endereço do objeto em memória, um objeto diferente não possui o mesmo endereço de id NUNCA;

* execução [7]: podemos visualizar quais dados temos na lista ``teste``;

* execução [8]: aplico o reverse na lista ``teste`` e podemos ver que este método não retorna dados pois não temos a linha Out após sua execução;

* execução [9]: podemos ver que o id continua o mesmo, logo podemos concluir que nosso objeto ainda é o mesmo objeto (em memória);

* execução [10]: nossa lista chamada ``teste`` foi modificada IN PLACE, ou seja, no mesmo objeto em que foi chamado o método reverse.

Observação importante: Nem todo IN PLACE mantêm o id do objeto original, a regra é o método/função alterar o objeto dentro dele mesmo, mas isso não significa que o id será sempre o mesmo, pois ele poderá criar um novo objeto e depositar esse objeto SOBRESCREVENDO sua variável antiga.

O que não é IN PLACE
--------------------

Um método/função não IN PLACE não modifica o objeto original para aplicar suas funcionalidades, mas sim cria um novo objeto! Vamos ao exemplo, pegando o gancho do exemplo acima:

.. code-block:: console

    In [15]: teste
    Out[15]: ['c', 'b', 'a']

    In [16]: id(teste)
    Out[16]: 140323076029960

    In [17]: reversed(teste)
    Out[17]: <list_reverseiterator at 0x7f9f8313c9b0>

    In [18]: teste
    Out[18]: ['c', 'b', 'a']

    In [19]: id(teste)
    Out[19]: 140323076029960

    In [20]: teste2 = list(reversed(teste))

    In [21]: teste2
    Out[21]: ['a', 'b', 'c']

    In [22]: id(teste)
    Out[22]: 140323076029960

    In [23]: id(teste2)
    Out[23]: 140323075691656

    In [24]: teste
    Out[24]: ['c', 'b', 'a']

    In [25]: teste2
    Out[25]: ['a', 'b', 'c']

* execução [15]: temos a nossa mesma lista com os mesmos elementos, na mesma ordem;

* execução [16]: temos o mesmo id da nossa lista original;

* execução [17]: executamos o ``reversed`` na lista ``teste`` e o resultado de Out é outro tipo de objeto chamado ``list_reverseiterator``, um objeto em diferente do que tínhamos anteriormente;

* execução [18]: nossa lista ``teste`` continua com os elementos na mesma posição após a execução da função;

* execução [19]: o id da nossa lista ``teste`` também continua sendo o mesmo;

* execução [20]: agora vou guardar o resultado da função ``reversed`` aplicar outra função ``list`` para criar um novo objeto ``teste2`` a partir da lista ``teste``;

* execução [21]: aqui temos uma nova lista ordenada de forma diferente da ``teste``;

* execução [22]: o id da lista ``teste`` ainda permanece o mesmo;

* execução [23]: o id da lista ``teste2`` é outro, pois ele é outro objeto;

* execução [24][25]: por fim vemos que os resultados das duas listas são diferentes.

Conclusão
---------

Entender o que é um método/função IN PLACE e como isso funciona no Python é muito importante para o aprendizado da linguagem e também evita o aparecimento de bugs :P.

That's all folks
