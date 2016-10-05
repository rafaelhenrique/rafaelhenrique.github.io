Python uma linguagem de tipagem dinâmica e forte
################################################

:date: 2016-02-23 22:43
:tags: python, tipagem dinâmica, tipagem forte
:category: Python
:slug: python-uma-linguagem-de-tipagem-dinamica-e-forte
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: O que significa tipagem dinâmica? E tipagem forte?

Todos que começam a estudar Python lêem que "Python é uma linguagem de tipagem dinâmica e forte" mas o que isso significa?

Tipagem dinâmica
----------------

Assim como Python hoje existem inúmeras linguagens no mercado que são dinamicamente tipadas. 

Referenciando especificamente o Python para explicar a questão: Tipagem dinâmica significa que o próprio interpretador do Python infere o tipo dos dados que uma variável recebe, sem a necessidade que você, o usuário da linguagem diga de que tipo determinada variável é. Exemplo de um script Python:

.. code-block:: python

    i, j = 10, 20
    print("O resultado é: ", i + j)

Vamos melhorar esta explicação com um exemplo de tipagem estática, a linguagem C. A linguagem C é estaticamente tipada, isso significa que deveremos sempre determinar qual o tipo de dados uma variável irá receber, exemplo de um programa em C:

.. code-block:: python

    #include <stdio.h>

    int main(){
       int i = 10, j = 20;
       printf("O resultado é: %d\n", i+j);
    }

Ambos os programas acima fazem a mesma coisa, somam 10 e 20 e mostram um resultado na tela, a diferença é que em C os tipos são estáticos então é necessário que o programador diga quais os tipos que ``i`` e ``j`` receberão como valores aceitáveis.

Tipagem forte
-------------

Assim como Python hoje existem inúmeras linguagens no mercado que são fortemente tipadas. 

Referenciando especificamente o Python para explicar a questão: Tipagem forte significa que o interpretador do Python avalia as expressões (evaluate) e não faz coerções automáticas entre tipos não compatíveis (conversões de valores), ou seja:

.. code-block:: python

    i, j = 10, "Rafael"
    print(i)
    print(j)
    print("O resultado é: ", i + j)

Neste código acima definimos ``i`` como ``10`` e ``j`` como ``"Rafael"``, desta forma temos um inteiro em ``i`` e uma string em ``j``, ao executar este código veja o que acontece:

.. code-block:: code

    $ python3 teste.py
    10
    Rafael
    Traceback (most recent call last):
      File "teste", line 4, in <module>
        print("O resultado é: ", i + j)
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

Recebo uma exception chamada ``TypeError`` ou seja, ao fazer operações com tipos incompatíveis, o Python não converte automaticamente esses tipos pra você, ele vai dar erro! Isso é bom, pois assim você terá a certeza que o seu resultado é mais consistente.

Agora assim como temos linguagens com tipagem forte, temos também linguagens com tipagem fraca como por exemplo Javascript, vejamos o código Javascript a seguir:

.. code-block:: python

    var i = 10;
    var j = "Rafael";
    console.log(i + j);

Executando o código anterior obteríamos o resultado ``10Rafael``. Isso prova que o Javascript diferente do Python converte (faz coerção de tipos) ao executar operações de forma automática, isso faz com que seja uma linguagem de tipagem fraca.

Conclusão
---------

Espero que tenha ficado claro para você como é essa questão da tipagem do Python. Em caso de dúvidas/sugestão não deixe de fazer seu comentário abaixo do post.

Referências
-----------

Livro: Python para desenvolvedores 2.a edição.
Autor: Luiz Eduardo Borges
Distribuição gratuita no `site <http://ark4n.wordpress.com/python/>`_.

Também tem um `vídeo <https://www.destroyallsoftware.com/talks/wat>`_ muito interessante (e bem curtinho) que mostra mais coisas a respeito de como outras linguagens tratam alguns casos bem bizarros (alguns envolvendo tipagem fraca/forte estática/dinâmica).
