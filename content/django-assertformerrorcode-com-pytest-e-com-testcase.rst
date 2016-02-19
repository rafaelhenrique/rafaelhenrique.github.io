Django assertFormErrorCode com py.test e com TestCase
#####################################################

:date: 2016-02-18 21:16
:tags: python, django, pytest, testcase, tdd
:category: Django
:slug: django-assertformerrorcode-com-pytest-e-com-testcase
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Pra que serve assertFormErrorCode do Django? Como utilizá-lo no py.test de forma tranquila?

Estive trabalhando em um teste hoje utilizando py.test e queria usar assertFormErrorCode padrão da suite de testes do Django, porém não queria extender meu teste de TestCase, como fazer?

Ta legal, se perdeu? Continue lendo abaixo que vou explicar o que é o assertFormErrorCode e também como utilizá-lo sem depender da suite de testes do Django.

Introdução
----------

Aprendi a usar recentemente vários asserts poderosos que o Django já te dá de presente na sua suite de testes. Quem me mostrou isso foi o `Henrique Bastos <https://twitter.com/henriquebastos>`_ no curso `Welcome to the Django <http://welcometothedjango.com.br/>`_ o qual recomendo a todos que façam, pois é um ótimo curso, e gostaria de fazer um agradecimento especial neste post! Parabéns Henrique pelo ótimo curso!

Códigos postados aqui
---------------------

Os códigos de exemplo deste post em sua maioria podem ser visualizados e estudados no github em um commit anterior ao atual do projeto wttd, clique `aqui para visualizar o projeto como um todo. <https://github.com/rafaelhenrique/wttd/tree/85c702631923cd3b47ec992c4cfcb06d9f172827>`_

Mas o que é assertFormErrorCode?
--------------------------------

Este assert é mais um dos asserts interessantíssimos que o Django tem na sua suite de testes. Vejamos um exemplo de como esse cara pode ser usado nos seus testes:

``Formulário básico de inscrição``

``wttd/eventex/subscriptions/forms.py``

.. code-block:: python

    from django import forms
    from django.core.exceptions import ValidationError


    def validate_cpf(value):
        if not value.isdigit():
            raise ValidationError('CPF deve conter apenas números', 'digits')

        if len(value) != 11:
            raise ValidationError('CPF deve ter 11 números', 'length')


    class SubscriptionForm(forms.Form):
        name = forms.CharField(label='Nome')
        cpf = forms.CharField(label='CPF',
                              validators=[validate_cpf])
        email = forms.EmailField(label='Email', required=False)
        phone = forms.CharField(label='Telefone', required=False)

        ... linhas omitidas ...

Perceba que este é um formulário bem básico onde podemos ver claramente que o campo ``cpf`` é validado com regras bem básicas onde somente verificamos 2 coisas: 

* se o cpf digitado não contem caracteres que não sejam números
* se o cpf tem 11 dígitos

O que eu acho mais interessante deste código é a questão do ``ErrorCode``! Em todo ``ValidationError`` de podemos passar um ``ErrorCode`` como parâmetro, que no caso das duas validações acima, podemos visualizar os códigos de erro ``digits`` e ``length``.

Ta legal, você não curtiu? É eu também não via sentido nisso antes de ver o que era possível fazer com isso.

Pra que especificar ``ErrorCodes`` nos seus ``ValidationError``?
----------------------------------------------------------------

Quando você cria um teste comumente você vai querer saber quais as mensagens de erro o seu formulário está exibindo para os usuários, porém ai vem a questão, se você tem milhares de formulários com milhares de mensagens de erro, como é o trabalho que você terá?

Se você mudar uma mensagem de erro você terá que sair garimpando no seu código onde você estava usando aquela mensagem para poder modificar para a nova e isso gasta TEMPO e consequentemente DINHEIRO! Fora que é chato pra caramba!

Pensando nisso você pode criar seus testes apontando para o ``ErrorCode`` assim se a mensagem mudar o ``ErrorCode`` permanecerá o mesmo e você não quebra nenhum teste! Sensacional isso!

Show me the code
----------------

Vejamos abaixo um teste criado no Django utilizando a verificação por ``ErrorCode``:

``Teste do formulário básico de inscrição``

``wttd/eventex/subscriptions/tests/test_form_subscription.py``

.. code-block:: python

    from django.test import TestCase

    from eventex.subscriptions.forms import SubscriptionForm


    class SubscriptionFormTest(TestCase):
        ... linhas omitidas ...

        def test_cpf_is_digit(self):
            """CPF must only accept digits"""
            form = self.make_validated_form(cpf='ABCD5678901')
            self.assertFormErrorCode(form, 'cpf', 'digits')        

        ... linhas omitidas ...

Olha ai que bacana esse teste! Limpo! Se você mudar a mensagem de erro no form o teste independe da mensagem, ele sempre irá olhar para o ``ErrorCode``.

Tudo bonito e maravilhoso mas...
--------------------------------

Mas... se você não usar a suite de testes do Django (herdando a classe TestCase) você não ganha esse assert maravilhoso chamado ``assertFormErrorCode``. E agora?

Procurando uma solução que funciona independente do TestCase
-------------------------------------------------------------

Depois de garimpar algum tempo na internet (e amolar um amigo do trabalho) achei este post `aqui <http://stackoverflow.com/questions/18781492/forms-validationerror-and-error-code>`_ no stack overflow, o padroeiro dos desenvolvedores de software.

Neste post o cara colocou uma forma diferente de conseguir pegar o ``ErrorCode`` que está na exception do ``ValidationError``, ele usou:

.. code-block:: command

    >>> print(form.errors.as_json())
    {"__all__": [
        {"message": "Your account has not been activated.", "code": "inactive"}
    ]}

Desta forma o cara trouxe o erro do form em json e depois desta maneira ele consegue pegar uma key chamada "code" onde está o ``ErrorCode``. Achei bacana isso ai, porém não é tão simples como o cara postou (nunca é).

Minha solução
-------------

Criei uma classe de teste base minha chamada ``BaseTest``:

``Classe base de testes``

``este cara não está no github``

.. code-block:: python

    from django.test import Client


    class BaseTest(object):

        def setup(self):
            self.client = Client()

        def post(self, endpoint, data, field_name):
            """
            Send post to form.

                endpoint: url for endpoint to test
                data: data to send to form
                field_name: name of form field on Django.
            """        
            resp = self.client.post(endpoint, data=data)
            context = getattr(resp, 'context', None)
            errors = []
            if context:
                errors = resp.context['form'].errors.as_data()[field_name]
                errors = [error.code for error in errors]
            return resp, errors

Meu problema era fazer um post retornar os ``ErrorCodes`` de forma fácil, com essa classe ``BaseTest`` consegui atingir meu objetivo. Explicando de forma detalhada:

* Primeiro importei o ``Client`` do Django que é um cara que eu realmente queria usar para fazer meus requests;
* O ``setup`` do py.test é tudo em minúsculo mesmo (diferente do Django);
* Ao colocar criar o ``self.client`` consigo usar o mesmo client para o resto da classe em forma de atributo;
* Criei um método de post para ser usado pela classe filha, onde eu retorno resp que é o response do request que o ``self.client.post`` executa e também retorno uma lista contendo os meus ``ErrorCodes`` todos bonitos em uma única lista.

Bem feito isso é só usar esse cara! Código de exemplo de uso:

``Teste que usa a classe BaseTest, baseada na classe SubscriptionFormTest``

``este cara não está no github``

.. code-block:: python

    ...linhas omitidas...

    class TestSubscriptionForm(BaseTest):
        def test_post_error(self):
            resp, errors = self.post(ENDPOINT, {"cpf" : "ABC"}, 'cpf')
            assert resp.status_code == 200
            assert 'digits' in errors

    ...linhas omitidas...

Desta forma este teste só vai passar caso o ``ErrorCode`` ``digits`` sejá levantado como exceção do ``ValidationError``.

Basicamente foi essa a brincadeira de hoje, eu achei bem legal, mesmo sem extender o TestCase padrão do Django conseguimos fazer a mesma coisa. Neste caso foi um pouco diferente pois o meu teste era pra validar um post e não propriamente um form, mas creio que a idéia tenha ficado clara, caso não, se não entenderem alguma coisa não deixem de me contatar.

Conclusão
---------

Quando você não consegue usar um recurso padrão Django dentro do Django para fazer alguma coisa, nunca se esqueça que o Django é Python, e sempre você conseguirá fazer algo para contornar a situação de uma forma bacana.

Bom é isso espero que tenham gostado do post! Deixem seus comentários!