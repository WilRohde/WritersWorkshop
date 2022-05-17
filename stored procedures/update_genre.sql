DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_genre`(
	IN id INT,
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
		UPDATE Genres SET short_description = short_description, 
			description = description WHERE Genres.id = id;
        SELECT * FROM Genres WHERE Genres.id = id;
	COMMIT;
END$$
DELIMITER ;