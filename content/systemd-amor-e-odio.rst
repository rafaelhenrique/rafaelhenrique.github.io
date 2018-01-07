systemd um caso de amor e ódio
##############################

:date: 2018-01-07 12:04
:tags: linux, systemd
:category: Linux
:slug: systemd-amor-e-odio
:author: Rafael Henrique da Silva Correia
:email:  rafael@abraseucodigo.com.br
:summary: Por que amar e odiar o systemd?

Um fato é que na computação tudo muda a todo instante e mudanças sempre devem ser analisadas e estudadas antes de termos uma opinião.

Eu já odiei systemd pois não tinha parado para estudar e sempre tentava fazer as coisas utilizando o SysV Init e pensava que tudo ia funcionar, porém OS DOIS SÃO MUITO DIFERENTES! Não adianta ficar com raiva do systemd, basta entender que ele é uma outra coisa e que ele não é o SysV Init ai você começará a gostar dele :D.

Quando estudei para a minha primeira certificação `LPI <http://www.lpi.org/>`_ as distribuições GNU/Linux como um todo usavam o padrão de inicialização do sistema SysV Init, hoje isso mudou e a maioria das distribuições usam o padrão systemd.

Qual a diferença?
-----------------

Em termos técnicos de baixo nível eu não sei a diferença por que nunca parei para estudar profundamente isso (se alguém quiser rolar um papo a gente conversa nos comments abaixo do post), mas no nível superficial o que mudou foi:

- Arquivos de configuração;
- Comandos.

Achei umas referências bacanas nestes links para quem quiser se aprofundar mais o assunto:

- `Comparativo: upstart, sysvinit, systemd, openrc <https://www.ibm.com/developerworks/community/blogs/752a690f-8e93-4948-b7a3-c060117e8665/entry/comparativo_upstart_sysvinit_systemd_openrc?lang=en>`_
- `Bê-á-bá do Systemd, parte 1 <https://www.ibm.com/developerworks/mydeveloperworks/blogs/752a690f-8e93-4948-b7a3-c060117e8665/entry/systemd_parte_1?lang=pt_br>`_
- `Understanding Systemd Units and Unit Files <https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files>`_
- `Systemd versus SysVinit <http://stato.blog.br/wordpress/systemd-versus-sysvinit/>`_

Como criar um serviço?
----------------------

A um tempinho atrás precisei criar um serviço para o tsurud que é o `daemon (se não sabe o que é daemon clica neste link) <https://pt.wikipedia.org/wiki/Daemon_(computa%C3%A7%C3%A3o)>`_ do `Tsuru PaaS <http://blog.abraseucodigo.com.br/como-criar-seu-paas-com-tsuru.html>`_ pois quando fui subir o PaaS ele não iniciava esse processo sozinho e não achei isso muito legal. Para criar o serviço eu comecei criando o arquivo `tsuru-server-api.service` da seguinte forma:

.. code-block:: command

    # vim /etc/systemd/system/tsuru-server-api.service

    [Unit]
    Description=Tsuru (tsuru-server-api)
    After=network.target
    Requires=mongod.service redis.service
    Documentation=https://tsuru.io/

    [Service]
    Type=simple
    ExecStart=/usr/bin/tsurud api --config=/etc/tsuru/tsuru.conf
    PIDFile=/var/run/tsuru-server-api.pid
    Restart=always
    User=tsuru
    Group=tsuru

    [Install]
    WantedBy=default.target

Cada serviço é atrelado a uma Unit do systemd. Dito isso vamos a explicação.

Explicando:

- Unit: Define metadados sobre a Unit;
- Description: Apenas uma descrição da sua Unit;
- After: Diz que este serviço só subirá depois que subir network.target, pois é um serviço que precisa de rede funcionando;
- Requires: Diz que se mongod.service ou redis.service falhar esse serviço também irá falhar, e ficará parado (não será iniciado);
- Documentation: Uma url de documentação para o serviço;
- Service: Define o serviço daquela unit;
- Type: O tipo `simple` faz com que systemd considere que o serviço deve ser iniciado imediatamente (mais `opções aqui <https://wiki.archlinux.org/index.php/Systemd_(Portugu%C3%AAs)#Tipo>`_)
- ExecStart: Comando que deve iniciar o daemon em questão;
- PIDFile: Arquivo que armazenará o `PID (não sabe o que é PID clique aqui) <https://pt.stackoverflow.com/questions/191815/o-que-seria-um-pid>`_ do processo;
- Restart: Seguir a tabelinha contida `aqui <https://www.freedesktop.org/software/systemd/man/systemd.service.html#Restart=>`_ para entender melhor essa configuração.
- User: Usuário dono do processo;
- Group: Grupo dono do processo;
- Install: Esta seção é opcional e é usada para definir o comportamento de uma unit;
- WantedBy: Especifica como a unit deve ser habilitada, no caso está configurada da maneira default pelo valor `default.target`.

Preferi colocar esse exemplo mais realista para vocês entenderem melhor, porém qualquer serviço pode ser criado baseado neste do Tsuru que eu criei, basta trocar os valores das configurações.

Comandos
--------

Depois de criar a sua unit com o seu service basta fazer reload do daemon do systemd para ele conseguir "enxergar" esse novo service:

.. code-block:: command

    systemctl daemon-reload


Outros comandos úteis:

.. code-block:: command

    # iniciar um service
    systemctl start <service>

    # ver status do service
    systemctl status <service>

    # parar um service
    systemctl stop <service>

    # listar dependências de um service
    systemctl list-dependencies tsuru-server-api

    # re-habilitar uma unit que foi modificada
    systemctl reenable <service>

    # visualizar todos os services do sistema
    systemctl -a

Últimas referências:

- `9.6.2. Creating Custom Unit Files <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sect-Managing_Services_with_systemd-Unit_Files.html#sect-Managing_Services_with_systemd-Unit_File_Create>`_
- `enabled systemd unit does not start at boot <https://superuser.com/questions/955922/enabled-systemd-unit-does-not-start-at-boot>`_

Gostou? Deixa seu comment ai ;)

Flw!