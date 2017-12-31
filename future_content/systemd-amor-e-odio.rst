
Conf do tsuru:

# cat /etc/systemd/system/tsuru-server-api.service

```
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
```

Fazer reload nos daemon todo:

systemctl daemon-reload


Startar ver status e parar o servico:

systemctl start <service>
systemctl status <service>
systemctl stop <service>

Listar dependências:

systemctl list-dependencies tsuru-server-api

Criar um custom:

https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sect-Managing_Services_with_systemd-Unit_Files.html#sect-Managing_Services_with_systemd-Unit_File_Create

https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sect-Managing_Services_with_systemd-Resources.html

https://superuser.com/questions/955922/enabled-systemd-unit-does-not-start-at-boot

Re-habilitar uma unit que foi modificada:

systemctl reenable <unit>