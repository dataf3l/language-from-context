
-- create database lfc;
-- use lfc;

create table knowledge(
  id int(10) not null auto_increment,
  student_id int(10),
  word_id int(10),
  date_learned datetime,
  primary key(id));

create table word(
  id int(10) not null auto_increment,
  language_id int(10),
  word  varchar(255),
  word_index int,
  category varchar(255),
  primary key(id));
-- insert into word(id,word) values(1,'hola');
-- insert into knowledge(id,word_id) values(1,1);


-- select word.word,knowledge.id,knowledge.date_learned from knowledge,word where word_id = word.id;

