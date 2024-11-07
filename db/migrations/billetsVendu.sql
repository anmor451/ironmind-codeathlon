DROP TABLE IF EXISTS `vendus`;
CREATE TABLE `vendus` (
  `prix` int(11) NOT NULL,
  `numero` int(11) NOT NULL,
  `section` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;