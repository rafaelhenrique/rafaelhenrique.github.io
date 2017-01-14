A importância de um log
#######################

:date: 2017-01-14 10:43
:tags: log, python
:category: Log
:slug: a-importancia-de-um-log
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: O que é log? E pra que logar?

Imagine que você criou uma aplicação Web (independente da linguagem de programação) e que durante o seu desenvolvimento você usou `TDD <https://pt.wikipedia.org/wiki/Test_Driven_Development>`_ bem certinho, como deve ser. Usando `testes de cobertura <https://en.wikipedia.org/wiki/Code_coverage>`_ junto ao TDD você consegue garantir que um determinado percentual do seu código está assegurado pelos testes que você escreveu, e isso é lindo!

Porém o que você não consegue garantir com TDD é se o teu usuário final está acessando sua aplicação da maneira que você programou para ele acessar, exceções sempre vão acontecer meu amigo! Esta é a vida dura de um desenvolvedor.

Seja por um desvio de comunicação entre quem programa e quem irá usar o programa, ou seja por um deslize qualquer que você como programador tenha cometido, exceções sempre irão acontecer, não adianta falar que não!

Agora cabe a você entender e tratar estas exceções, mas como? Sua aplicação está lá longe de você, rodando em alguma máquina em alguma Cloud XYZ e você está aqui "cego", você não vê as exceções acontecerem e quando elas acontecem, quem vê geralmente é o teu cliente, e provavelmente quando ele ver a exceção acontecer isso irá gerar insatisfação e até falta de segurança pra ele.

Como resolver isso? Como visualizar suas exceções para que elas não aconteçam mais? A resposta é simples meu amigo! Faça com que sua aplicação gere logs!

O que é um log?
---------------

Log por essência é um arquivo de texto puro, com linhas, onde cada linha tem hora e data de uma ação que tem determinada importância na aplicação.

Hoje existem formas mais legais do que simplesmente armazenar em um arquivo texto, dentre as opções que temos você pode mandar estes logs para o `Logentries <https://logentries.com/>`_, podemos mandar logs como se fossem mensagens para o `Slack <https://slack.com/>`_ ou `Telegram <https://telegram.org/>`_, mandar o arquivo de log para o `S3 <https://aws.amazon.com/pt/s3/>`_ e analisar com alguma ferramenta sua, ou pode usar a stack da `Elastic <https://www.elastic.co/>`_ (Logstash, Kibana e Elasticsearch) entre outras inúmeras opções.

O que eu preciso logar?
-----------------------

Você deve logar tudo que é importante para o bom funcionamento das operações que sua aplicação executa, entretanto, quando você não sabe o que é importante, tudo é importante.

Quando você não sabe o que logar, faça log de tudo! Sim, isso mesmo!

Isso vai ser chato no no começo, pois tudo que acontecer no sistema vai aparecer pra você e você terá que analisar, mas uma coisa é certa, a primeira vez que você ler um log que contêm tudo da sua aplicação algumas coisas vão acontecer com certeza:

1. Um entendimento melhor sobre o seu sistema: Quando você loga tudo, você consegue ver o comportamento real do seu sistema, como ele está funcionando de verdade, qual o fluxo das operações que ele faz e baseado nisso você consegue melhorar as operações e o fluxo como um todo de maneira que tenha um melhor desempenho para você e também para o seu cliente (até em termos de usabilidade);

2. Chateação: Quando você chega ao momento de se perguntar `Por que eu estou logando essa ação?` provavelmente essa linha de log não é importante pra você, pense sobre isso e veja se realmente faz diferença pra você, se não é importante, prontamente pare de logar isso, a leitura do log ficará mais fácil;

Ainda sobre `Chateação` existem algumas abordagens para resolver isso, uma delas é você separar os logs por nível de importância.

Separar por nível de importância
--------------------------------

No Python temos alguns loglevels que podemos usar:

- info / debug: Usado para propósitos informativos, onde info é para informações menos detalhadas e debug para informações mais detalhadas;
- warning: Usado para logar uma ação que precisa ser notada, mas não é algo crítico ainda;
- error / exception / critical: Erros e problemas críticos no geral, usamos error para problemas que não são críticos, critical para problemas críticos e exception para logar exceptions juntamente ao Traceback.

Porém é mais fácil entender isso na prática.

Saindo um pouco da teoria e indo para a prática
-----------------------------------------------

Vamos imaginar que já temos um programa que é nada mais nada menos do que uma calculadora:

.. code-block:: python

    def add(x, y):
        return x + y


    def mul(x, y):
        return x * y


    def sub(x, y):
        return x - y


    def div(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            print("Impossível dividir por 0!")

    if __name__ == '__main__':
        print(add(8, 4))
        print(mul(8, 4))
        print(div(8, 4))
        print(div(8, 0))
        print(sub(8, 4))

Ao executar este nosso programinha teríamos a seguinte saída:

.. code-block:: command

    $ python calc.py
    12
    32
    2.0
    Impossível dividir por 0!
    None
    4

Até ai tudo bem certo? Tudo bem pois não vamos executar cálculos "ilegais", agora se você fosse um usuário desavisado com certeza você tentaria fazer operações deste tipo:

.. code-block:: python

    ... linhas omitidas ...

    if __name__ == '__main__':
        print(add('a', 4))
        print(mul(0, 'a'))

Ou seja, este cálculo resultaria em uma exceção não tratada por você o que resultaria em problema e insatisfação por parte do usuário.

Como logar as ações da nossa calculadora?
-----------------------------------------

Para isso vamos usar o módulo `logger <https://docs.python.org/3/howto/logging.html>`_ embutido (built-in) no Python.

Vamos ver como fica:

.. code-block:: python

     1  import logging
     2  logging.basicConfig(filename='mycalculator.log', level=logging.DEBUG,
     3                      format='%(asctime)s %(levelname)s %(funcName)s => %(message)s')
     4
     5
     6  def add(x, y):
     7      logging.debug('paramethers: x={}, y={}'.format(x, y))
     8      return x + y
     9
    10
    11  def mul(x, y):
    12      logging.debug('paramethers: x={}, y={}'.format(x, y))
    13      return x * y
    14
    15
    16  def sub(x, y):
    17      logging.debug('paramethers: x={}, y={}'.format(x, y))
    18      return x - y
    19
    20
    21  def div(x, y):
    22      try:
    23          logging.debug('paramethers: x={}, y={}'.format(x, y))
    24          return x / y
    25      except ZeroDivisionError:
    26          logging.exception('paramethers: x={}, y={}'.format(x, y))
    27          print("Impossível dividir por 0!")
    28
    29  if __name__ == '__main__':
    30      print(add(8, 4))
    31      print(mul(8, 4))
    32      print(div(8, 4))
    33      print(div(8, 0))
    34      print(sub(8, 4))

Explicando separadamente:

- Linha 1: Faço o import do módulo de logging;
- Linha 2: Defino como será o meu log:
    - `filename`: Qual será o nome do meu arquivo de log;
    - `format`: Qual o formato as linhas do meu log serão gravadas.
- Linha 7, 12, 17: Ao chamar a função `add` será gravado um log de debug com os parâmetros que usamos para chamar a função;
- Linha 26: Quando a função `div` causar `ZeroDivisionError` esta exceção será gravada no log juntamente com o traceback.

Ao executar este programinha um arquivo `mycalculator.log` será gerado com o log das operações executadas, veja só:

.. code-block:: command

    $ python calc.py
    12
    32
    2.0
    Impossível dividir por 0!
    None
    4
    $ cat mycalculator.log
    2017-01-14 14:06:44,351 DEBUG add => paramethers: x=8, y=4
    2017-01-14 14:06:44,351 DEBUG mul => paramethers: x=8, y=4
    2017-01-14 14:06:44,351 DEBUG div => paramethers: x=8, y=4
    2017-01-14 14:06:44,351 DEBUG div => paramethers: x=8, y=0
    2017-01-14 14:06:44,351 ERROR div => paramethers: x=8, y=0
    Traceback (most recent call last):
      File "calc.py", line 24, in div
        return x / y
    ZeroDivisionError: division by zero
    2017-01-14 14:06:44,352 DEBUG sub => paramethers: x=8, y=4

Repare que o traceback da função `div` foi gravado quando a exceção ocorreu.

Como mitigar exceções desconhecidas?
------------------------------------

Um pouco mais acima eu havia dito que se você não sabe o que é importante é legal fazer log de tudo e com o tempo remover o que você achar desnecessário.

Esta prática é muito útil quando você não tem pleno conhecimento do funcionamento da aplicação em que você vai trabalhar (supondo que ela não tenha log de nada).

Podemos logar todas as exceções não tratadas para irmos resolvendo ao longo do tempo, para fazer isso é simples, vamos ver como isso ficaria na nossa função `add`:

.. code-block:: python

    ...linhas omitidas...

    def add(x, y):
        try:
            logging.debug('paramethers: x={}, y={}'.format(x, y))
            return x + y
        except:
            logging.exception('Unknown exception')
            raise

    ...linhas omitidas...

    if __name__ == '__main__':
        print(add(8, 4))
        print(add(8, 'a'))
        print(add('a', 4))

    ...linhas omitidas...

O que aconteceu agora? Todas as exceções "genéricas" serão gravadas no nosso log para fazermos uma análise do que aconteceu. Vamos observar o efeito disso:

.. code-block:: command

    $ python calc.py
    12
    Traceback (most recent call last):
      File "calc.py", line 33, in <module>
        print(add(8, 'a'))
      File "calc.py", line 9, in add
        return x + y
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    $ cat mycalculator.log
    2017-01-14 14:15:10,939 DEBUG add => paramethers: x=8, y=4
    2017-01-14 14:15:10,939 DEBUG add => paramethers: x=8, y=a
    2017-01-14 14:15:10,939 ERROR add => Unknown exception
    Traceback (most recent call last):
      File "calc.py", line 9, in add
        return x + y
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

Cuidado que você deve ter ao logar as exceções genericamente
-------------------------------------------------------------

Perceba que usamos o `raise` após logar a exceção para propagar a exceção, pois quando ela é uma exceção desconhecida não podemos ignorá-la, o código abaixo é considerado uma má prática:

.. code-block:: python

    # ISSO NÃO DEVE SER FEITO

    def add(x, y):
        try:
            logging.debug('paramethers: x={}, y={}'.format(x, y))
            return x + y
        except:
            logging.exception('Unknown exception')

    # ISSO NÃO DEVE SER FEITO

Desta forma acima quando o nosso código levantar uma exceção irá retornar `None` seja ela qual for! Isso é horrível! Dificulta a programação e a depuração em diversos aspectos.

Se você tomar esta precaução não terá problema você fazer logs para exceções genéricas e isso te ajudará muito (principalmente quando você não conhece o sistema como um todo), e você poderá ir criando exceções mais claras posteriormente quando você já tiver um entendimento legal do código :).

Conclusão
---------

Criar logs te ajuda a entender mais sobre o sistema e não é uma tarefa complexa, comece aos poucos e logo você estará viciado em fazer logs pois você verá por si a vantagem que te proporciona no dia a dia.

Dúvidas, sugestões e críticas deixe seu comentário abaixo!

Espero que tenham gostado! ;)

Referências
-----------

- `When to use logging <https://docs.python.org/3/howto/logging.html#when-to-use-logging>`_
- `Logging HOWTO <https://docs.python.org/3/howto/logging.html>`_
