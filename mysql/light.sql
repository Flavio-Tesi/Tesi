/*DROP TABLE IF EXISTS `lights`;*/

CREATE TABLE IF NOT EXISTS `lights` (
  `room` varchar(25) NOT NULL ,
  `status` BIT(1) NOT NULL,
  PRIMARY KEY (`room`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*LOCK TABLES `intrusion` WRITE;*/

INSERT INTO lights (room,status) VALUES, ('Camera','0'), ('Cameretta','0'), ('Cucina','0'), ('Sala','0');

UNLOCK TABLES;
