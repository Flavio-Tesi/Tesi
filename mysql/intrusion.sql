/*DROP TABLE IF EXISTS `intrusion`;*/

CREATE TABLE IF NOT EXISTS `intrusion` (
  `room` varchar(25) NOT NULL ,
  `status` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`room`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*LOCK TABLES `intrusion` WRITE;*/

INSERT INTO intrusion (room,status) VALUES, ('Camera','regular'), ('Cameretta','regular'), ('Cucina','regular'), ('Sala','regular');

UNLOCK TABLES;
