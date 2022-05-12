CREATE DEFINER=`root`@`localhost` PROCEDURE `create_author`(
	IN username varchar(45),
	IN email varchar(45),
    IN firstname varchar(255),
    IN lastname varchar(255),
    IN password varchar(255)
)
BEGIN
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
	COMMIT;
END