DROP TABLE IF EXISTS `events`;
CREATE TABLE `events` (
  `e_id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `prix` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

INSERT INTO `events` (`e_id`, `nom`, `date`, `prix`) VALUES
(0,	'tailgate',	'2024-11-07',	5);

INSERT INTO `events` (`e_id`, `nom`, `date`, `prix`) VALUES
(1,	'match',	'2024-11-07',	20);