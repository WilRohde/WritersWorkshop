CREATE DEFINER=`root`@`localhost` PROCEDURE `get_author_by_username`(
	IN username VARCHAR(45)
    )
BEGIN
	DECLARE exit handler for sqlexception, sqlwarning
	BEGIN
		SELECT "Exception occurred in get_author_by_email"
		ROLLBACK;
	END;
    START TRANSACTION;
		SELECT * FROM authors WHERE authors.username = username;
END