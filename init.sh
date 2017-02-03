sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/mysql start﻿
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start﻿
sudo gunicorn -b 0.0.0.0:8080 hello:app &
cd ask && sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &
