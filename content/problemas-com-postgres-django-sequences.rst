Problemas com sequences no PostgreSQL usando Django
###################################################

:date: 2016-12-22 10:58
:tags: python, django, postgresql, sequences
:category: Django
:slug: problemas-com-postgres-django-sequences
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Sua sequence não incrementa corretamente, este post pode te ajudar

Tive um problema bem estranho estes dias, fui criar um novo objeto de model Django e persistí-lo no banco com o método `.save()` (como todos vocês devem fazer milhares de vezes por dia), porém isso não aconteceu e recebi um erro deste tipo:

.. code-block:: command

    IntegrityError: duplicate key value violates unique constraint "core_pessoa_pkey"
    DETAIL:  Key (id)=(2) already exists.

Vamos entender por que isso aconteceu.

Qual a causa para isso ter acontecido?
--------------------------------------

Você sempre se faz essa pergunta quando se depara com uma situação bizarra? Bem, eu também. A uns dias atrás precisei rodar um script no Django que inseria vários objetos no banco de dados, porém como esta operação já havia sido testada e retestada em outra máquina os objetos já tinham uma pk associada, então imagine um model do Django hipotético com esta estrutura:

.. code-block:: python
    ... linhas omitidas ...

    class Pessoa(models.Model):
        nome = models.CharField(max_length=50)
        idade = models.IntegerField()

E para persistir um novo objeto no banco você faz:

.. code-block:: command

    >>> from django-test.core.models import Pessoa
    >>> p = Pessoa(id=1, nome="Rafael", idade=28)
    >>> p.save()

Desta maneira iríamos persistir esta pessoa na nossa base de dados PostgreSQL tranquilamente. Porém!!! Porém!!! Porém!!! Isso tem um problema. Quando criamos um objeto novo já com uma pk (o id do nosso exemplo) associada e persistimos este objeto a sequence dele NÃO É INCREMENTADA! Ou seja, quando você for persistir um outro objeto sem passar a pk o Django te mandará esta exception abaixo bem no meio da sua cara:

.. code-block:: command

    IntegrityError: duplicate key value violates unique constraint "core_pessoa_pkey"
    DETAIL:  Key (id)=(1) already exists.

Como consigo ver este efeito acontecer? Simples, basta tentar persistir uma pessoa sem passar a pk:

.. code-block:: command

    >>> from pessoa.models import Pessoa
    >>> p1 = Pessoa(id=2, nome="Rafael", idade=28)
    >>> p1.save()
    >>> p2 = Pessoa(nome="Rafael", idade=28)
    >>> p2.save()
    django.db.utils.IntegrityError: duplicate key value violates unique constraint "core_pessoa_pkey"
    DETAIL:  Key (id)=(1) already exists.

Este efeito foi observado no PostgreSQL e não sei se aconteceria usando MySQL ou outros SGBDs por exemplo... é questão de experimentar e ver o efeito.

Como eu resolvo isso?
---------------------

Você conseguirá resolver este problema setando um valor NA MÃO para a sua sequence que não foi incrementada. No PostgreSQL até que foi simples, primeiro fiz uma query para descobrir quais eram TODAS as minhas sequences:

.. code-block:: command

    SELECT c.relname FROM pg_class c WHERE c.relkind = 'S';

          relname
    -----------------------------------
     django_migrations_id_seq
     django_content_type_id_seq
     auth_permission_id_seq
     auth_group_id_seq
     auth_group_permissions_id_seq
     auth_user_id_seq
     auth_user_groups_id_seq
     auth_user_user_permissions_id_seq
     django_admin_log_id_seq
     core_pessoa_id_seq
    (10 registros)

Neste caso a sequence que queremos é a do `id` que está na app chamada `core` e no model `Pessoa`, que se chama `core_pessoa_id_seq` no meu exemplo. Vamos dar uma olhada como esta sequence está no momento:

.. code-block:: command

    SELECT * FROM core_pessoa_id_seq;

       sequence_name    | last_value | start_value | increment_by |      max_value      | min_value | cache_value | log_cnt | is_cycled | is_called 
    --------------------+------------+-------------+--------------+---------------------+-----------+-------------+---------+-----------+-----------
     core_pessoa_id_seq |          1 |           1 |            1 | 9223372036854775807 |         1 |           1 |      32 | f         | t
    (1 registro)

Perceba que nossa sequence possui o valor `last_value` igual a 1, o que não é verdade pois já temos 2 objetos na nossa tabela `pessoa`, como podemos ver na query abaixo:

.. code-block:: command

    SELECT * FROM core_pessoa;

     id |  nome  | idade 
    ----+--------+-------
      1 | Rafael |    28
      2 | Rafael |    28
    (2 registros)

Para verificar isso mais facilmente (em caso de muitos registros) também podemos usar um count nesta query:

.. code-block:: command

    SELECT count(*) FROM core_pessoa;

     count
    -------
         2
    (1 registro)

Agora o próximo passo é setar o `last_value` de maneira correta, para isso vamos executar o comando abaixo:

.. code-block:: command

    SELECT setval('core_pessoa_id_seq', 2);

     setval
    --------
          2
    (1 registro)

Depois podemos consultar o valor da nossa sequence de novo:

.. code-block:: command

    SELECT * FROM core_pessoa_id_seq;

       sequence_name    | last_value | start_value | increment_by |      max_value      | min_value | cache_value | log_cnt | is_cycled | is_called 
    --------------------+------------+-------------+--------------+---------------------+-----------+-------------+---------+-----------+-----------
     core_pessoa_id_seq |          2 |           1 |            1 | 9223372036854775807 |         1 |           1 |       0 | f         | t
    (1 registro)

Podemos ver que foi alterado de fato! Agora vamos tentar inserir um objeto sem id novamente:

.. code-block:: command

    >>> from pessoa.models import Pessoa
    >>> p = Pessoa(nome="Rafael", idade=28)
    >>> p.save()

E tudo funcionou normalmente de novo como deveria ser!! Dúvidas/sugestões e críticas?? Use essa caixinha mágica ai em baixo :)