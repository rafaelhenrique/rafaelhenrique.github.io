Title: Grupo de Estudos Python - Aula 01
Date: 2015-10-14 22:53
Tags: python, grupo de estudos python, sorocaba
Category: Python
Author: Rafael Henrique da Silva Correia
Email: rafael@abraseucodigo.com.br
Slug: grupo-de-estudos-python-sorocaba-01
Summary: Grupo de estudos Python em Sorocaba aula 01... primeiros passos 

Olá! Já expliquei um pouco da história do Grupo de Estudos Python Sorocaba [aqui](http://blog.abraseucodigo.com.br/grupo-de-estudos-python-sorocaba.html), então nos próximos posts sobre o Grupo vou abordar o que andamos falando por lá. 
Na primeira aula de nivelamento Python foram abordados os seguintes tópicos chave:

- Por que Python se chama Python?
- Por que Python? O que podemos fazer com Python?
- Filosofia Pythônica
- Instalando Python
- Usando Python
- input vs raw_input
- Cuidado com eval (usado no input do Python2.X)
- Python2 e Python3

Alguns assuntos desses eu apenas mandei links para a galera ler, pois o tempo de 1h era muito pequeno pra ver tudo isso, e existem coisas muito "batidas" que eu não queria focar tanto, minha ideia era mais fazer o pessoal sair da primeira aula programando. Maassss como em um blog não existe tempo :raised_hands: pretendo explicar e mostrar coisas sobre estes assuntos todos neste post da Aula 01.

Let's start...

## Por que Python se chama Python?

Copiando literalmente as palavras da [Wiki Python Brasil](http://wiki.python.org.br/PerguntasFrequentes/SobrePython#De_onde_surgiu_esse_nome.3F):
```
Ao contrário do que normalmente se pensa, a origem do nome da linguagem não é a espécie de serpente "Pitón" e sim o grupo inglês de humoristas "Monty Python". 
O uso da serpente como símbolo da linguagem se difundiu depois da publicação do ProgrammingPython da editora O'Reilly.
```

## Por que Python? O que podemos fazer com Python?

Python é uma linguagem de altíssimo nível, extremamente poderosa e versátil. Maiores vantagens:

- Muito fácil de ser aprendida
- Comunidade muito grande
- Os grandes mestres na comunidade são muito acessíveis para conversar/tirar dúvidas
- É uma linguagem limpa e tem isso como filosofia
- Por ser uma linguagem limpa fica fácil de você ler os códigos fonte de outras pessoas e entender o que está rolando ali
- Muitas bibliotecas para TUDO!
- Quantidade enorme de frameworks para os mais variados usos
- Não é Java ! Isso pra mim é uma vantagem :trollface: ! (me desculpem javeiros)

É difícil definir um limite entre o que é possível fazer com Python e o que não é possível, mas não vou mentir, vou usar uma frase que é comumente utilizada por todos: **Não existe bala de prata! Use o que for melhor para o seu projeto!** Python provavelmente tem um limite de alcance... proponho aos conhecedores mais avançados comentar sobre estas limitações nos comentários deste post. Mas eu como conhecedor nível médio em Python, digo que não encontrei algo que seja impossível fazer com Python.

Tópicos da computação que estão muito na "moda" usando Python (e empregam muita gente):

- Aplicações Web
- Computação científica
- Computação de Alto Desempenho 
- IoT
- Análise de dados
- Sistemas de recomendações
- Aplicações Desktop (sim! ainda existem!)

Links bacanas falando mais sobre por que usar Python:

- [Full Stack Python](https://www.fullstackpython.com/why-use-python.html)
- [Wiki Python Brasil](http://wiki.python.org.br/PerguntasFrequentes/SobrePython) (tem umas coisas meio defasadas, cuidado)
- [Abrindo o Apetite](http://python.pro.br/pydoc/2.7/tutorial/appetite.html)

## Filosofia Pythônica

O Python é regido por um "mantra" chamado Zen do Python, se você seguir esse "mantra" na hora de programar tudo seguirá de forma maravilhosamente bem... apresento-lhes o "mantra" Pythônico:

```
The Zen of Python
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
   
    Tim Peters <tim.peters at gmail.com>
```
Fonte: [PEP-20](https://www.python.org/dev/peps/pep-0020/)

Existem muitas derivações e interpretações a partir deste mantra na internet, vou citar os que achei mais legais:

- [Zen of Python em ilustrado](http://hacktoon.com/log/2015/programming-comics-3/) - [@hacktoon](https://twitter.com/hacktoon)
- [Cordel do Python](https://github.com/luanfonceca/oxente) - [luanfonseca](https://github.com/luanfonceca)
- [Minerin do Python](https://github.com/vsouza/Minerin-do-Python) - [vsouza](https://github.com/vsouza)

## Instalando Python

Em sistemas operacionais Linux o Python 2.6 já é a versão default. Mas deixo aqui dicas de como instalar outras versões. Seria legal ter instalado pelo menos uma versão >= 2.7 e uma versão >= 3.4, para que assim você possa comparar algumas pequenas coisas que serão comentadas mais a frente. Caso leia os procedimentos/tutoriais passados abaixo e não consiga instalar Python em seu PC mesmo assim por favor me diga qual problema você encontrou nos comentários abaixo deste Post.

## Instalando Python em sistemas operacionais Linux Debian-Like

Todo sistema operacional Debian-like (Debian, Ubuntu, Xubuntu, Linux Mint... etc) possui apt-get, então isso já facilita muito a instalação, basta digitar (estando logado como root) os seguintes comandos:

```
# apt-get update
# apt-get install python3.4 python3.4-venv python2.7 python-virtualenv
```

Dúvidas sobre como usar o apt-get!? Consulte a [Wiki do Ubuntu-BR](http://wiki.ubuntu-br.org/AptGet).

## Instalando Python em sistemas operacionais Linux Red Hat-Like

Existe um tutorial muito bom pra isso [aqui no tutorial da Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4) no momento estou sem tempo de criar uma VM de CentOS só para fazer esta instalação e documentar, mas achei muito bom este tutorial criado pela Digital Ocean. 

## Instalando Python em sistemas operacionais Apple

Eu não tenho afinidade nenhuma com sistemas Apple mas achei [esse tutorial](http://www.ime.usp.br/~mac2166/python/macos.html) bem convincente, se vocês testarem e funcionar me avisem :smirk:.
Também temos o tutorial da documentação oficial [aqui](https://docs.python.org/2/using/mac.html).

## Instalando Python em sistemas operacionais Microsoft Windows

Se eu não tenho afinidade com Apple .... tenho muito menos afinidade com Windows :confused:.
Mas creio que para este cara temos alguns tutoriais bem bacanas também:

- [Tutorial Oficial](https://docs.python.org/2/using/windows.html)
- [How to install Python, Setuptools, Pip and Virtualenv on Windows in 5 minutes (XP / 7 / 8)](https://www.youtube.com/watch?v=Es_kdnPUgDg)
- [Instalando e Configurando o Python e Django no Windows](http://pythonclub.com.br/instalacao-python-django-windows.html)

## Usando Python

Agora que você já instalou o Python então vamos conhecê-lo né!?

No seu terminal (seja windows/linux/mac) digite python e tecle enter conforme mostrado abaixo (o `$` é apenas uma indicação que estou digitando o comando no terminal, não precisa digitar ok!?):
```
$ python
Python 2.7.9 (default, Mar  1 2015, 12:57:24) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Uma saída similar será apresentada para você, para sair do terminal interativo do python você poderá teclar `Ctrl + D` ou digitar o comando `exit()` (os parênteses são necessários), faça isso para sair do terminal interativo para você ir se acostumando :wink:. 

Se você já instalou mais de uma versão do Python neste passo (o que é extremamente recomendável) você poderá abrir o terminal interativo das diferentes versões que você instalou, conforme mostrado abaixo:
```
$ python2.7
Python 2.7.9 (default, Mar  1 2015, 12:57:24) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

$ python3.4
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```
Seria legal abrir os interpretadores das diferentes versões instaladas para ver se correu tudo bem com sua instalação.

## Vamos fazer continhas!?

Agora que você está com Python instalado e o interpretador de comandos Python funcionando, vamos dar uma brincada, você sabia que o interpretador de comandos Python também pode ser usado como uma calculadora!? Não!? Pois é, deixa eu te mostrar:
```
$ python
Python 2.7.9 (default, Mar  1 2015, 12:57:24) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> (400 / 3) + 2
135
>>> (400 / 3) + 2 * 4
141
>>> (400 / 3) + (2 * 4)
141
>>> ((400 / 3) + 2) * 4
540
>>> 4 + 4
8
>>> 5 - 4
1
>>> 10 - 1
9
>>> 2 ** 2
4
>>> 2 ** 3
8
```
Perceba que os parênteses fazem diferença assim como nas equações matemáticas, e aqui números reais devem ser escritos com um `.` como separador de casas:
```
>>> 3.4 + 5.4
8.8
>>> 3,4 + 5,5
(3, 9, 5)
>>> 5.7 + 4.5
10.2
```
Perceba aqui que a `,` serve pra outra coisa! Outra hora volto nesse assunto da vírgula ai, por enquanto só guarde na sua cabeça que contas com números reais (float) devem ser feitas com `.`, beleza!?

## Quer fazer continhas mais loucas!?

Sempre olhe a documentação oficial do Python antes de procurar em qualquer outro lugar, então a documentação dos tipos numéricos básicos pode ser lida [aqui](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). 

Outra dica é sempre ler a documentação de acordo com a versão do Python que você está usando no momento, perceba que no canto superior esquerdo da documentação oficial sempre terá a versão que você está lendo, esta que eu passei acima é do Python3.

## Como escrever coisas!?

Bom, para escrever coisas na tela (stdout) é bem simples também... vamos lá:
```
$ python3.4
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Olá amigo!")
Olá amigo!
```
Feito!

## Como escrever coisas dentro de coisas!? (ou melhor.. concatenar strings)

Hãm!? Como assim!? É cara... as vezes eu também não entendo o que eu escrevo, mas explicando acho que melhora:
```
$ python3.4
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> nome = "Rafael"
>>> print("Meu nome é ", nome)
Meu nome é Rafael
```
Opa! Gravei uma string Rafael dentro de uma variável nome e escrevi ela na tela! Puts ... bem legal em!? Isso começa a parecer um programa de verdade!

## Montando um programinha "completo"

Vamos agora capturar uma entrada de usuário (stdin) no nosso programinha. Vamos lá:
```
$ python3.4
Python 3.4.2 (default, Oct  8 2014, 10:45:20) 
[GCC 4.9.1] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> nome = input("Qual seu nome? ")
Qual seu nome? Rafael
>>> print(nome)
Rafael
>>> print("Meu nome é", nome)
Meu nome é Rafael
```
Testa ai! Veja se funciona bem! E vamos melhorar isso ai! :joy:

## Interpretadores, comandos, wtf é tudo isso!?

O que fizemos até agora foi usando o interpretador interativo do Python, mas o que é isso?

Python é uma linguagem interpretada (talvez eu já deveria ter falado isso no começo do post). Nas palavras do Henrique Bastos (um dos grandes mestres Python que andei conhecendo em minhas jornadas):

>"Na computação, a compilação é o processo que reúne o código fonte e o transforma em algo que faça mais sentido para o computador. Do ponto de vista do código fonte, toda linguagem de programação é compilada.

>O produto final do processo de compilação de uma linguagem diz muito sobre seu design. Linguagens como C e C++ são compiladas estaticamente, e seus códigos fontes são transformados diretamente em linguagem de máquina. Enquanto as linguagens mais modernas como Java, C# e Python têm seus códigos fontes transformados em uma linguagem intermediária (específica de cada linguagem), que será interpretada pela máquina virtual da linguagem quando o programa for executado.

>Este processo de interpretação da linguagem intermediária durante a execução do programa, consiste na tradução dos comandos da linguagem intermediária para linguagem de máquina. Sendo assim, em tempo de execução, o código intermediário pode ser encarado como um “código fonte” que será compilado dinamicamente pelo interpretador da linguagem em código de máquina."

>Fonte: [Diferenças entre linguagem compilada e linguagem interpretada](http://henriquebastos.net/diferencas-entre-linguagem-compilada-e-linguagem-interpretada/)

Então como Python é uma linguagem interpretada os criadores tiveram a brilhante ideia de fazer um interpretador interativo onde podemos testar nossos programas antes de sair fazendo por ai, isso torna muito mais fácil desenvolver qualquer coisa em Python (não desmerecendo outras linguagens que também tem interpretadores interativos, tal como [o irb do Ruby](https://www.ruby-lang.org/pt/documentation/quickstart/)). O que fizemos até o momento foi testar alguns comandos (functions) embutidos (built-in) do Python para simplesmente conhecê-los.

## Eai!? Vamos fazer um script de verdade ou não!?

Vamos lá... 
Utilizando um editor de texto que use UTF-8 para salvar os arquivos (se não conhecer nenhum recomendo o [Sublime](http://www.sublimetext.com/)) crie o seguinte programinha:

```python
print("Este é o exemplo mais besta do mundo! Mas é melhor que Hello World!")
print(":-o -- "*20)
```

Salve este cara como `hello_world.py` e execute este cara assim (o `$` é apenas uma indicação que estou digitando o comando no terminal, não precisa digitar ok!?):

```bash
$ python hello_world.py

Saída:
Este é o exemplo mais besta do mundo! Mas é melhor que Hello World!
:-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o --
```

Esse exemplo é bem legal pois no Python2.X ele vai dar ERROOOOO, erros são ótimos para o aprendizado! E qual o erro!? Veja a saída abaixo:

```bash
$ python hello_world.py

Saída:
  File "hello_world.py", line 1
SyntaxError: Non-ASCII character '\xc3' in file hello_world.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
``` 

Vishhhh! E agora!?

O Python2.X trabalha por padrão com caracteres ASCII (leia-se aski e não asc2 por favor), então quando colocamos um mínimo acento temos que especificar que trabalharemos com utf-8, pois o utf-8 não é o padrão do Python2.X, no caso o nosso acento é o do `é`, removendo este acento este programinha funcionaria perfeitamente, veja:

```bash
$ python hello_world.py 

Saída:
Este e o exemplo mais besta do mundo! Mas e melhor que Hello World!
:-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o -- :-o --
```

## Você quer dizer que o Python2.X não suporta ACENTOS!?????

Não não amigo! Você entendeu mal... eu disse que o Python2.X trabalha por padrão com ASCII, para que ele entenda que deve trabalhar com utf-8 para ler seus lindos acentos do print você deverá especificar isso no código fonte conforme abaixo:

```python
# -*- coding: utf-8 -*-
print("Este é o exemplo mais besta do mundo! Mas é melhor que Hello World!")
print(":-o -- "*20)
```

Pronto! Arrume seu programinha ai (voltando também o `é` caso você o tenha removido) e execute novamente conforme mostrado acima.

## Um programinha mais legal

Programinha... nome estranho esse :joy:, mas eu tenho costume de escrever coisas estranhas as vezes, não fiquem chateados comigo se eu escrever script, programinha, sistema, softwarezinho e coisas do tipo, na verdade todas elas vão significar um sistema feito em Python ok!?

Continuando...

Agora crie o seguinte programinha abaixo:

```python
1 # -*- coding: utf-8 -*-
2 numero = input("Digite um número: ")
3 
4 print("O número é {0}".format(numero))
5 print("O número é", numero)
6 print("O número é " + str(numero))
```

- Linha 1: Especificamos nossa codificação do programinha;
- Linha 2: Recebemos um número do usuário, o input espera o usuário digitar alguma coisa e digitar enter em seguida para continuar o programa
- Linha 3: Não tem nada :trollface:
- Linha 4: Mostra o número na tela usando o format
- Linha 5: Mostra o número na tela concatenando string com o número por meio de `,` esta saída ficará bem estranha se você rodar no Python2.X, essa sintaxe representa coisas diferentes no Python2.X e no Python3.X
- Linha 6: Mostra o número na tela concatenando string com o número por meio de `+` e conversão (cast) do número para string, você não precisará converter se estiver usando Python3.X

Explicando algo um pouco mais aprofundado, tenha ciência que Python2.X e Python3.X são diferentes, algumas coisas mudam de significado MESMO, mas a diferença é pouca, é legal sempre testar o mesmo código no 2 e no 3 enquanto se aprende Python, mas caso você não tenha muito saco pra isso dê maior foco ao Python3.X. Algumas diferenças são listadas [aqui](http://python3porting.com/differences.html) e podem ser consultadas durante a leitura destas aulas que postarei.

## input vs raw_input

Caso vocês executem o script acima utilizando Python2.X poderão notar algumas diferenças. No Python2.X quando usamos o input na verdade estamos utilizando por baixo uma função bem importante chamada `eval` junto a esse input, vamos entender isso:

```bash
$ python2.7 numero.py 

Saída:
Digite um número: 2+2
O número é 4
('O n\xc3\xbamero \xc3\xa9', 4)
O número é 4
```

Quando passamos uma expressão para o input ele vai fazer um `evaluate` (em português acho que a tradução melhor seria calcular/avaliar) daquela expressão! Ou seja, ele vai resolver a expressão para depois guardar o resultado dela na variável especificada que no nosso caso se chama `numero`. Isso parece lindo em um primeiro momento, mas quando se usa `eval` em qualquer lugar não somente em Python sempre devemos tomar MUITO cuidado, vamos analisar o código abaixo:

```python
# -*- coding: utf-8 -*-

minha_senha = 'rafael123'
numero = input("Digite um número: ")
print("O número é: {}".format(numero))
```

Executando este script temos:

```bash
$ python2.7 numero.py

Saída:
Digite um número: minha_senha
O número é: rafael123
```

Então amiguinhos!!! Vocês acabam de capturar uma variável do seu script!!! Isso pode ser extremamente perigoso em um ambiente real!! Para isso você pode usar no Python2.X a função built-in chamada `raw_input` que não faz eval por baixo dos panos e torna sua vida muito mais segura:

```python
# -*- coding: utf-8 -*-

minha_senha = 'rafael123'
numero = raw_input("Digite um número: ")
print("O número é: {}".format(numero))
```

Execução:

```bash
$ python2.7 numero.py

Saída:
Digite um número: minha_senha
O número é: minha_senha
```

Para que a gente consiga compatibilidade entre Python2.X e Python3.X neste script acima poderíamos fazer algo bem simples:

```python
1 # -*- coding: utf-8 -*-
2 try:
3     raw_input
4 except:
5     raw_input = input
6 
7 minha_senha = 'rafael123'
8 numero = raw_input("Digite um número: ")
9 print("O número é: {}".format(numero))
```

- Linha 2 e 3: Tenta verificar se existe a palavra `raw_input` neste Python que chamará o script
- Linha 4 e 5: Caso não exista raw_input o raw_input será o mesmo que o input

Vale lembrar que o input no Python3.X não usa `eval` por baixo dos panos, sendo assim ele é bem tranquilo de ser usado no Python3.X.

## Fim de aula - Exercício para aula 02

Bom ... não quero perder o ritmo que foi feito no Grupo de Estudos Python Sorocaba, então vou seguir a mesma dinâmica onde todo final de aula rola um exercício! O primeiro exercício será fazer uma calculadora que faça soma, conforme mostrada a saída abaixo:

```bash
$ python3 calculadora_soma.py
Digite operando1:
10
Digite operando2:
40
Resultado: 50.0

$ python3 calculadora_soma.py
Digite operando1:
10
Digite operando2:
-2
Resultado: 8.0

$ python3 calculadora_soma.py
Digite operando1:
10
Digite operando2:
20
Resultado: 30.0
```

Eai!? Aceita o desafio!? A resposta para este problema está no que eu disse/mostrei neste post inicial, basta ler com atenção. Se você estiver com dúvidas por favor me avise, ai a gente bate um papo, pode usar o comentário abaixo deste post pra isso ou me mandar e-mail, twitter e etc, meus contatos estão a esquerda do blog.

Espero que tenham gostado da primeira aula, e se viram algo que não gostaram muito me avisem :wink:

Abraço!