CREATE DEFINER=`root`@`localhost` PROCEDURE `author_is_member`(
	IN group_id iNT,
    IN author_id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in author_is_member"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM GroupMembers WHERE GroupMembers.group_id = group_id AND
			GroupMembers.author_id = author_id;
END