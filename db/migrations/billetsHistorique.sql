DROP TABLE IF EXISTS `billet_historique`;
CREATE TABLE `billet_historique` (
  `action` varchar(255),
  `auteur` varchar(255),
  `date` DATETIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
