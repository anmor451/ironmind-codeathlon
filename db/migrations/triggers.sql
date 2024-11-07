-- SET @compteur = 0;

-- DELIMITER //
-- CREATE TRIGGER billet_vendu AFTER INSERT ON vendus
-- AS
-- BEGIN
-- IF MOD(@compteur, 20) = 0
-- UPDATE billets SET prix = prix * (1 + (RAND() * (0.05 - 0.01) + 0.01))
-- END//
-- DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER billet_historique_ajout AFTER INSERT ON billets
-- INSERT INTO 'billets_Historique' ('Action', 'Auteur', 'Date')




