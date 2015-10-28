Title: Grupo de Estudos Python - Aula 01 - Resposta do Exercício
Date: 2015-10-28 19:49
Tags: python, grupo de estudos python, sorocaba
Category: Python
Author: Rafael Henrique da Silva Correia
Email: rafael@abraseucodigo.com.br
Slug: grupo-de-estudos-python-sorocaba-01_resposta
Summary: Grupo de estudos Python em Sorocaba aula 01... resposta do exercício 

Ao final da aula 01 foi passado um exercício bem básico, o qual agora vou mostrar passar a resposta, decidi fazer em post separado pois caso você ainda não tenha feito, você poderá ler o post da aula 02 sem spoilers.

## Relembrando

Faça uma calculadora de soma conforme abaixo:

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

Simples!? Conseguiram fazer!?

## Explicação prévia

Basicamente você terá que receber dois números do usuário e mostrar a resposta na tela, existe a forma simples (e fácil) de resolver este exercício e a forma mais complexa.

## Forma simples (o mundo ideal)

Você soma os números sempre esperando que o usuário seja bonzinho com você e realmente só digite números...

```python
1 # -*- coding: utf-8 -*-
2 try:
3     raw_input
4 except:
5     raw_input = input
6 
7 x = float(raw_input("Digite operando1: "))
8 y = float(raw_input("Digite operando2: "))
9 
10 print("Resultado: {}".format(x+y))
```

Este código é compatível com python2 e python3. A forma simples pode dar alguns problemas:

```bash
$ python resposta_blog.py 
Digite operando1: a
Traceback (most recent call last):
  File "resposta_blog.py", line 7, in <module>
    x = float(raw_input("Digite operando1: "))
ValueError: could not convert string to float: a
```

Tentei somar a letra 'a', porém quando vou converter 'a' para float recebo um erro de conversão.

## Forma mais complexa (o mundo real)

Você soma os números porém valida se realmente o que o usuário digitou é um número, pois eventualmente ele vai ser malandro e não digitar :troll:...

```python
1 # -*- coding: utf-8 -*-
2 import sys
3 
4 try:
5     raw_input
6 except:
7     raw_input = input
8 
9 try:
10    x = float(raw_input("Digite operando1: "))
11    y = float(raw_input("Digite operando2: "))
12 except ValueError:
13    print("Digite somente números!")
14    sys.exit(1)
15 
16 print("Resultado: {}".format(x+y))
```

Desta forma mostrada acima não mostramos um exception tão feia para o usuário, caso o usuário informe uma letra esta saída ficará mais legível:

```bash
$ python resposta_blog.py 
Digite operando1: 1
Digite operando2: a
Digite somente números!
```

E ai o que achou? Bem mais bonito né!? Caso tenha alguma dúvida (qualquer que seja ela) dos exemplos postados, por favor entre em contato. E logo sairá a aula 2 :wink:
