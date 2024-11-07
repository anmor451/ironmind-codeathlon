DROP TABLE IF EXISTS `billets`;
CREATE TABLE `billets` (
  `b_id` int(11) NOT NULL,
  `siege` varchar(255) NOT NULL,
  `prix` FLOAT NOT NULL
--   KEY `siege` (`siege`),
--   CONSTRAINT `billets_ibfk_1` FOREIGN KEY (`siege`) REFERENCES `sieges` (`numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

