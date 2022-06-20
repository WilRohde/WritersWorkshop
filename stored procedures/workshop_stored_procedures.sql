DELIMITER $$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE accept_invitation(
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
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_author`(
	IN username VARCHAR(45),
	IN email VARCHAR(45),
    IN firstname VARCHAR(255),
    IN lastname VARCHAR(255),
    IN password VARCHAR(255)
)
BEGIN
	DECLARE new_identity INT DEFAULT 0;
	DECLARE exit handler for 1062
    BEGIN
		SELECT "This username and/or email address already exists in the database.";
    END;
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO Authors (username, email, firstname, lastname, password) 
        VALUES (username, email, firstname, lastname, password);
        SET new_identity = LAST_INSERT_ID();
        SELECT * FROM Authors WHERE id = new_identity;
	COMMIT;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_genre`(
	IN name VARCHAR(255),
    IN short_description VARCHAR(45),
    IN description VARCHAR(255)
)
BEGIN
    DECLARE new_identity INT DEFAULT 0;
	DECLARE exit handler for 1062
    BEGIN
		SELECT "This group name already exists in the database.";
    END;
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_genre";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO Genres (name, short_description, description) 
        VALUES (name, short_description, description);
        SET new_identity = LAST_INSERT_ID();
        SELECT * FROM Genres WHERE id = new_identity;
	COMMIT;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_group`(
	IN name VARCHAR(255),
    IN description VARCHAR(255),
    IN short_description VARCHAR(45),
    IN creator_id INT,
    IN genre_id INT
)
BEGIN
		DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_group";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO Reviews (name, description, short_description, founding_date, Creator_id, Genre_id) 
        VALUES (name, description, short_description, Now(), creator_id, genre_id);
	COMMIT;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_group_request`(
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
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_invitation`(
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
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `create_review`(
	IN reviewer_id INT,
    IN submission_id INT,
    IN title VARCHAR(45),
    IN review_text LONGTEXT,
    IN rating INT)
BEGIN
		DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in create_review";
		ROLLBACK;
	END;
    START TRANSACTION;
		INSERT INTO Reviews (title, review_text, rating, Submission_id, Reviewer_id) 
        VALUES (title, review_text, rating, reviewer_id, submission_id);
	COMMIT;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `get_author_by_email`(
	IN email VARCHAR(45)
    )
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_author_by_email"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM authors WHERE authors.email = email;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `get_author_by_id`(
	IN id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_author_by_id"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM authors WHERE authors.id = id;
END$$
$$CREATE DEFINER=`root`@`localhost` PROCEDURE `get_creator`(
	IN creator_id INT
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_creator"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT id, email, firstname, lastname FROM Authors WHERE id=creator_id;
END$$
