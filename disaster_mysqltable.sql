CREATE DATABASE IF NOT EXISTS emergps;
USE emergps;

CREATE TABLE disaster(
id INT UNSIGNED NOT NULL auto_increment,
disaster_name text,
graphic_url text,
href text,
location text,
created_at DATE,
active BOOLEAN,
PRIMARY KEY(id)
);


DROP TABLE disaster;
SHOW tables;
SHOW FIELDS FROM disaster;

SELECT * FROM disaster ORDER BY id DESC LIMIT 50 OFFSET 0;
INSERT INTO disaster (disaster_name, graphic_url,href, location, created_at, active) 
VALUES ("Ejemplo","algo mas bonito" , "href", "Por alla",ADDDATE('2008-01-02', INTERVAL 31 DAY), true);

