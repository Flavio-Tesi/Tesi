/*DROP TABLE IF EXISTS `users`;*/

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `users` WRITE;

INSERT INTO users (name,code) VALUES ('Sergio','12345'), ('Flavio','01010'), ('Simona','54321');

UNLOCK TABLES;
