CREATE DEFINER=`root`@`localhost` PROCEDURE `get_author_groups`(
	IN id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_genre";
		ROLLBACK;
	END;
    START TRANSACTION;
SELECT * from WritingGroups LEFT JOIN GroupMembers ON WritingGroups.id = GroupMembers.group_id 
	WHERE GroupMembers.author_id = id;
END