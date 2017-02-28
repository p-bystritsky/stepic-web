sudo /etc/init.d/mysql start﻿
mysql -uroot -e "create database stepic_web;"
ln -s ask/default_settings.py ask/local_settings.py
ln -s qa/default_settings.py qa/local_settings.py
ask/manage.py syncdb
ask/manage.py runserver 0.0.0.0:80 &