CREATE DEFINER=`root`@`localhost` PROCEDURE `create_group`(
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
END