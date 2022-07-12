-- DDL-комманды: CREATE, DROP, ALTER


/* Данная БД нужна для решения проблем с хранением ировой информации. Так как листов персонажей не достаточно, 
 * а приложений в play market и app store с подобной функцией для НРИ системы Genesys найдено не было,
 * было принято решение создать свое приложение, работающее с БД и позволяющее мастеру создавать и отправлять
 * игрокам созданных им заклинания, монстров, предметов и так далее.
*/

DROP DATABASE IF EXISTS tanysha;
CREATE DATABASE IF NOT EXISTS tanysha_love_DnD;
USE tanysha_love_DnD;


-- Таблица для хранения кастомных заклинаний по НРИ системе GENESYS

CREATE TABLE genesys_magic_list(
	id SERIAL PRIMARY KEY,
	magic_type VARCHAR(130) NOT NULL,
	name VARCHAR(150) NOT NULL,
	skill VARCHAR(150) NOT NULL,
	concentration VARCHAR(3) NOT NULL DEFAULT FALSE,
	skill_rank VARCHAR (130) NOT NULL,
	damage VARCHAR(130) NOT NULL
);

INSERT genesys_magic_list VALUES (1, 'атака', 'огненный шар', 'магия', 'нет', '1', 'инт + dice');
INSERT genesys_magic_list VALUES (2, 'атака', 'огненный поток', 'магия', 'да', '2', 'инт + 1 + dice');
INSERT genesys_magic_list VALUES (3, 'атака', 'огненная стена', 'магия', 'да', '3', 'инт + 2 + dice');
INSERT genesys_magic_list VALUES (4, 'атака', 'разряд тока', 'природа', 'нет', '1', 'инт + dice');
INSERT genesys_magic_list VALUES (5, 'атака', 'разряд молнии', 'природа', 'нет', '2', 'инт + 1 + dice');

SELECT * FROM genesys_magic_list;

-- Таблица для хранения брони, оружия и других предметов

CREATE TABLE genesys_item_list(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	
);

CREATE TABLE genesys_monstrum(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	characteristic 
	health_and_protection
	skills
	talents
	aptitudes
	equipment
);