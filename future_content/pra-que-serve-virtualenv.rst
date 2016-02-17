Uma prévia de como começar a brincar com projetos Python no Windows
-------------------------------------------------------------------

Abra o ``Prompt de comando``` normalmente ele terá uma cara similar a esta:

.. image:: images/instalando-python35-no-windows-7_07.png
   :alt: prompt de comando

Provavelmente seu nome de usuário estará maiúsculo, mas como eu sou um user/admin linux viciado justamente por este motivo o meu sempre estará minúsculo.

Agora vamos criar uma pasta que seria a pasta do seu projeto:

.. code-block:: command

    C:\Users\rafael> mkdir myproject

Vamos entrar nesta pasta:

.. code-block:: command

    C:\Users\rafael> cd myproject
    C:\Users\rafael\myproject>

Posteriormente vamos criar um virtualenv:

.. code-block:: command

    C:\Users\rafael\myproject> python -m venv .venv

Pronto criamos um virtualenv onde este cara ficará armazenado em uma pasta nomeado como `.venv`, como podemos ver abaixo:

.. code-block:: command

    C:\Users\rafael\myproject> dir
    ... linhas omitidas ...

    02/16/2016   10:36 PM   <DIR>        .venv

    ... linhas omitidas ...

Para começar a usar esse virtualenv temos que ativá-lo para isso execute:

.. code-block:: command

    C:\Users\rafael\myproject> .venv\Scripts\activate.bat
    (.venv) C:\Users\rafael\myproject>

Perceba que o seu prompt vai ser modificado e o prefixo (.venv) será acrescentado no começo dele.

