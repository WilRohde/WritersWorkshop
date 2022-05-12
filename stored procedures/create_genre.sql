CREATE DEFINER=`root`@`localhost` PROCEDURE `create_genre`(
	IN name VARCHAR(255),
    IN short_description VARCHAR(45),
    IN description VARCHAR(255)
)
BEGIN
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
	COMMIT;
END