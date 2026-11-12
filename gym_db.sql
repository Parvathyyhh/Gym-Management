create database gym_db;
use gym_db;
create table member(id int primary key auto_increment,name varchar(100),place varchar(100),mobile varchar(15) unique,plan enum("1 month","2 months","3 months","6 months","8 months","1 year"),fee int,joined_date date);