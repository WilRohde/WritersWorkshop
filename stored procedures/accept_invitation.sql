DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE accept_invitation(
	IN invitation_id INT
    )
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		ROLLBACK;
		SELECT 'Exception occurred in accept_invitiation';
	END;
    START TRANSACTION;
		SELECT invitee_id, group_id from Invitations
			WHERE id = invitation_id;
		INSERT INTO GroupMembers (group_id, author_id) 
        VALUES (group_id, invitee_id);
        DELETE FROM Invitations where id = invitation_id;
	COMMIT;

END $$
DELIMITER ;