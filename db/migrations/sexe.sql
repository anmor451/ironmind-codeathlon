DROP TABLE IF EXISTS `sexe`;
/* Sexe a 0 si homme, a 1 si femme
    Faire jointure avec profils
*/
CREATE TABLE `sexe` (
  `sexe` bit(1) NOT NULL,
  PRIMARY KEY (`sexe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;