CREATE DEFINER=`root`@`localhost` PROCEDURE `join_group`(
    IN group_id INT,
	IN author_id INT
)
BEGIN
    DECLARE new_identity INT DEFAULT 0;
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in join_group";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO GroupMembers (group_id, author_id) 
        VALUES (group_id, author_id);
        SET new_identity = LAST_INSERT_ID();
        SELECT * FROM GroupMembers WHERE id = new_identity;
	COMMIT;
END