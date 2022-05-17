DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_group`(
	IN id INT,
    IN name VARCHAR(255),
    IN description VARCHAR(255),
    IN short_description VARCHAR(45),
    IN founding_date DATETIME
)
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_group_members"
		ROLLBACK;
	END;
    START TRANSACTION;
UPDATE WritingGroups SET name = name, description = description,
                 short_description = short_description, 
                 founding_date = founding_date
                 WHERE id = id;
END$$
DELIMITER ;