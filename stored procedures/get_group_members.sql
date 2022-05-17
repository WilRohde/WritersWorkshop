DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_group_members`(
	IN id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_group_members"
		ROLLBACK;
	END;
    START TRANSACTION;
    SELECT Authors.firstname, Authors.lastname FROM Authors LEFT JOIN GroupMembers
                ON authors.id = GroupMembers.author_id LEFT JOIN WritingGroups 
                ON GroupMembers.Group_id = WritingGroups.id WHERE WritingGroups.id = id;
END$$
DELIMITER ;