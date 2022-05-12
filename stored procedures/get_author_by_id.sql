CREATE DEFINER=`root`@`localhost` PROCEDURE `get_author_by_id`(
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
END