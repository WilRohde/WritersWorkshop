DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_genres`()
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_genres"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM Genres;
END$$
DELIMITER ;