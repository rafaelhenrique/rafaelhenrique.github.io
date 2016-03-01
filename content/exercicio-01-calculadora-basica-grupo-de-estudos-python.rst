Exercício: 01 - Calculadora básica - Grupo de Estudos Python
############################################################

:date: 2016-02-29 23:43
:tags: exercício, python, grupo de estudos python, sorocaba
:category: Python
:slug: exercicio-01-calculadora-basica-grupo-de-estudos-python
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Exercício para resolução passado no Grupo de Estudos Python

Baseado no script abaixo:

.. code-block:: python
    
    # -*- coding: utf-8 -*-

    primeiro = input("Digite o primeiro número: ")
    segundo = input("Digite o segundo número: ")
    operacao = input("Digite a operação: ")

    if operacao == "+":
        primeiro = float(primeiro)
        segundo = float(segundo)
        print("Resultado: {}".format(primeiro + segundo))
    else:
        print("Você digitou a operação errada! Digite: + - / *")

Vamos terminar a calculadora básica (com as 4 operações pelo menos) em Python?
Se precisar de ajuda para resolver o exercício me contate ou assista o vídeo (que está upando neste momento) da aula 02 do Grupo de Estudos Python.

Se você quiser estudar um pouquinho mais e não somente resolver o exercício você poderá acrescentar novas funcionalidades a nossa calculadora, tais como: fazer exponenciação, calcular seno, calcular coseno ... etc

Para facilitar seu divertimento use a biblioteca `math <https://docs.python.org/3.5/library/math.html>`_ padrão do Python.

Semana que vem posto a resolução (todas as resoluções que conseguirmos).
