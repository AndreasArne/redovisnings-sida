create database redovisa character set utf8 collate utf8_bin;
create user 'redovisa'@'localhost' identified by '<passwd>';
grant all privileges on redovisa.* to 'redovisa'@'localhost';
flush privileges;
