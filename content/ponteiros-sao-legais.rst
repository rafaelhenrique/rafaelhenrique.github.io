Ponteiros são legais
####################

:date: 2018-01-06 19:03
:tags: go, golang, ponteiros
:category: Golang
:slug: ponteiros-sao-legais
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Veja aqui como ponteiros em Golang são legais!

A pouco comecei a estudar a `linguagem Go <https://golang.org/>`_ e como comecei bem no nível iniciante eu estou estudando os tipos e as estruturas de dados da linguagem. Achei bem legal o funcionamento da passagem de valor para as funções, TODO valor passado por padrão para uma função não altera o "objeto" original. Hein? Não entendeu? Vamos lá...

Exemplo de passagem de valores para uma função
----------------------------------------------

Imagine que você vai fazer uma função bem bobinha que incrementa números, você teria algo assim:

.. code-block:: python

    package main

    import "fmt"

    func main() {
        number := 10
        fmt.Printf("number: %p - %+v\n", &number, number)

        number = increment(number, 10)

        fmt.Printf("number: %p - %+v\n", &number, number)
    }

    func increment(number int, numberIncrement int) int {
        number = number + numberIncrement
        return number
    }

Executando este código teríamos uma saída assim:

.. code-block:: command

    number: 0xc42001c0d0 - 10
    number: 0xc42001c0d0 - 20

Usei o `%p` para exibir o endereço de memória da variável number. Agora veja que curioso quando exibimos o endereço de memória dentro da função `increment`:

.. code-block:: python

    package main

    import "fmt"

    func main() {
        number := 10
        fmt.Printf("number: %p - %+v\n", &number, number)

        number = increment(number, 10)

        fmt.Printf("number: %p - %+v\n", &number, number)
    }

    func increment(number int, numberIncrement int) int {
        number = number + numberIncrement
        fmt.Printf("increment: %p\n", &number)
        return number
    }

Saída:

.. code-block:: command

    number: 0xc42001c0d0 - 10
    increment: 0xc42001c0e8
    number: 0xc42001c0d0 - 20

Ou seja, o compilador criará uma nova variável em um novo endereço de memória realizará o cálculo dentro da função `increment` SEM ALTERAR o valor original da variável `number` que está na função `main`. Bem interessante isso né?

Como fazer com que o Go use a mesma variável e economize memória?
-----------------------------------------------------------------

A resposta é simples, ponteiros! E o uso também é muito simples, apesar de o conceito de ponteiros assustar muita gente que aprendeu C no passado :D.

Vamos dar uma pequena mudada no programinha:

.. code-block:: python

    package main

    import "fmt"

    func main() {
        number := 10
        fmt.Printf("number: %p - %+v\n", &number, number)

        increment(&number, 10)

        fmt.Printf("number: %p - %+v\n", &number, number)
    }

    func increment(number *int, numberIncrement int) {
        *number = *number + numberIncrement
        fmt.Printf("increment: %p\n", number)
    }

Agora mudamos, não vamos mais mandar o valor de `number`, mas vamos mandar o endereço de memória de `number` para a função `increment`, ou seja, passamos um ponteiro de `number` para a função `increment`. Fazendo isso a função irá incrementar o valor diretamente em `number`, no mesmo da função `main`.

Veja a execução do código acima:

.. code-block:: command

    number: 0xc42009a000 - 10
    increment: 0xc42009a000
    number: 0xc42009a000 - 20

Bacana né? Gostou? Deixa seu comentário ai ;)

Flw!