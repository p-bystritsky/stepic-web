sudo /etc/init.d/mysql start﻿
mysql -uroot -e "create database stepic_web;"
cp ask/ask/default_settings.py ask/ask/local_settings.py
cp ask/qa/default_settings.py ask/qa/local_settings.py
ask/manage.py syncdb
ask/manage.py runserver 0.0.0.0:80 &