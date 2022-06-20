DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_genre_by_id`(
	IN id INT
    )
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_genre_by_id"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM Genres WHERE Genres.id = id;
END$$
DELIMITER ;