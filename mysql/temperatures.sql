DROP TABLE IF EXISTS `temperatures`;

CREATE TABLE IF NOT EXISTS `temperatures` (
  `room` varchar(25) NOT NULL ,
  `val` int(8) DEFAULT NULL,
  PRIMARY KEY (`room`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*LOCK TABLES `users` WRITE;*/

INSERT INTO temperatures (room) VALUES ('Camera'), ('Cameretta'), ('Cucina'), ('Sala');

UNLOCK TABLES;
