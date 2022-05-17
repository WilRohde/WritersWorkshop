DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_groups`()
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_group_members"
		ROLLBACK;
	END;
    START TRANSACTION;
SELECT WritingGroups.*, Genres.name as GenreName FROM WritingGroups
                LEFT JOIN Genres ON WritingGroups.genre_id = Genres.id;
END$$
DELIMITER ;