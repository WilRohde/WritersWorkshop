DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_group_by_name`(
	IN name VARCHAR(255)
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_group_by_name"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT WritingGroups.*, Genres.name as GenreName FROM WritingGroups 
        LEFT JOIN Genres ON WritingGroups.genre_id = Genres.id 
        WHERE WritingGroups.name = name;
END$$
DELIMITER ;