DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_invitation`(
	IN group_leader_id INT,
    IN invitee_id INT,
    IN group_id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_invitation";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO Invitations (group_leader_id, invitee_id, group_id) 
        VALUES (group_leader_id, invitee_id, group_id);
	COMMIT;
END$$
DELIMITER ;