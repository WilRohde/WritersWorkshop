DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_creator`(
	IN creator_id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_creator"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT id, email, firstname, lastname FROM Authors WHERE id=creator_id;
END$$
DELIMITER ;