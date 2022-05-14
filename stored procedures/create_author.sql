CREATE DEFINER=`root`@`localhost` PROCEDURE `create_author`(
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
END