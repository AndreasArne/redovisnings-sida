create database redovisa character set utf8 collate utf8_bin;
create user 'redovisa'@'localhost' identified by 'aaaa';
grant all privileges on redovisa.* to 'redovisa'@'localhost';
flush privileges;
