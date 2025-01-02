create database if not exists `test` default character set utf8 collate utf8_general_ci;
use `test`;

create table if not exists `user` (
    `id` int(11) not null auto_increment,
    `name` varchar(255) not null,
    `age` int(11) not null,
    primary key (`id`)
) engine=innodb default charset=utf8;