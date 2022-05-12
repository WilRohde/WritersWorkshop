CREATE DEFINER=`root`@`localhost` PROCEDURE `create_review`(
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
END