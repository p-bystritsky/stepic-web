mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"