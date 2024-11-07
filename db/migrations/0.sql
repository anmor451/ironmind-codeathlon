-- # Ceci est un test de migration SQL
-- # Les migrations sont exécutées en ordre alphabétique sur les fichiers du répertoire db/migrations
DROP DATABASE IF EXISTS codeathlon;
CREATE DATABASE codeathlon;
USE codeathlon;

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

/*
J'ai créer les tables, avec les colonnes que je pense peuvent être util.
Peut etre faire mettre des clés, j'ai aussi commencé un trigger (fonction appelé quand on insere sur une table) 

TYPES:
VARCHAR: Équivalent a string, la parenthese signifie bit prise, mettre 255
integer
float
double
date

Vous pouvez lier des tables avec des clés. Une clé primaire peut etre une clé
étrangere(foreign) dans une autre table, c'est pourquoi c'est bien avoir id
*/

CREATE OR REPLACE TABLE items (
    name VARCHAR(255) PRIMARY KEY,
    description TEXT,
    price FLOAT
);

INSERT INTO items VALUES ('Item 1', 'This is item 1', 1);
INSERT INTO items VALUES ('Item 2', 'This is item 2', 2);
INSERT INTO items VALUES ('Item 3', 'This is item 3', 3);
INSERT INTO items VALUES ( 'Item 5 (where the fuck is 4)', 'This is WHAT', 100);