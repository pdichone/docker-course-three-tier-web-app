CREATE TABLE IF NOT EXISTS `quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quote` text NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO quotes(quote, author)
VALUES("Be the change you want to see in the world.", "Ghandi"), ("Master patterns in life, and  you'll never suffer is the secret","someone");



