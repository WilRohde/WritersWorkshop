CREATE DEFINER=`root`@`localhost` PROCEDURE `create_group_request`(
	IN requestor_id INT,
    IN group_id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_group_request";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO GroupRequests (Requestor_id, Group_id) 
        VALUES (requestor_id, group_id);
	COMMIT;
END