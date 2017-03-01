sudo /etc/init.d/mysql start﻿
mysql -uroot -e "create database stepic_web;"
mv ask/ask/default_settings.py local_settings.py
mv ask/qa/default_settings.py local_settings.py
ask/manage.py syncdb
ask/manage.py runserver 0.0.0.0:80 &