DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_group_member_count`(
	IN id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_group_member_count"
		ROLLBACK;
	END;
    START TRANSACTION;
    SELECT COUNT(*) as member_count FROM Authors LEFT JOIN GroupMembers
                ON authors.id = GroupMembers.author_id LEFT JOIN WritingGroups 
                ON GroupMembers.Group_id = WritingGroups.id WHERE WritingGroups.id = id;
END$$
DELIMITER ;