-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema workshop_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema workshop_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `workshop_schema` DEFAULT CHARACTER SET utf8 ;
USE `workshop_schema` ;

-- -----------------------------------------------------
-- Table `workshop_schema`.`Authors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Authors` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL,
  `firstname` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`Genres`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Genres` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Genres` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `short_description` VARCHAR(45) NULL,
  `description` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

INSERT INTO Genres (name, short_description, description)
	VALUES ('open','Open to all genres','Groups using this genre are open to all entries');
INSERT INTO Genres (name, short_description, description)
	VALUES ('Science Fiction','Anything Sci-Fi related','Hard and soft Sci-Fi entries are welcome here.');
INSERT INTO Genres (name, short_description, description)
	VALUES('Fantasy','Here there be dragons','Classic fantasy, urban fantasy, pretty much anything you can think of will work here.');
INSERT INTO Genres (name, short_description, description)
	VALUES('Horrid Teenage Vampire Fiction','You know if your work belongs here','If it will make you cringe looking back in five years, you have found where you belong.');


-- -----------------------------------------------------
-- Table `workshop_schema`.`WritingGroups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`WritingGroups` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`WritingGroups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `short_description` VARCHAR(45) NULL,
  `founding_date` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  `Creator_id` INT NOT NULL,
  `Genre_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Creator_id`, `Genre_id`),
  INDEX `fk_Groups_Authors1_idx` (`Creator_id` ASC) VISIBLE,
  INDEX `fk_WritingGroups_Genres1_idx` (`Genre_id` ASC) VISIBLE,
  CONSTRAINT `fk_Groups_Authors1`
    FOREIGN KEY (`Creator_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_WritingGroups_Genres1`
    FOREIGN KEY (`Genre_id`)
    REFERENCES `workshop_schema`.`Genres` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`Submissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Submissions` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Submissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `filename` VARCHAR(255) NULL,
  `filesize` VARCHAR(45) NULL,
  `filetype` VARCHAR(45) NULL,
  `data` LONGBLOB NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  `Group_id` INT NOT NULL,
  `Author_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Group_id`, `Author_id`),
  INDEX `fk_Submissions_Groups1_idx` (`Group_id` ASC) VISIBLE,
  INDEX `fk_Submissions_Authors1_idx` (`Author_id` ASC) VISIBLE,
  CONSTRAINT `fk_Submissions_Groups1`
    FOREIGN KEY (`Group_id`)
    REFERENCES `workshop_schema`.`WritingGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Submissions_Authors1`
    FOREIGN KEY (`Author_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`GroupMembers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`GroupMembers` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`GroupMembers` (
  `id` INT NOT NULL,
  `group_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`group_id`, `author_id`, `id`),
  INDEX `fk_Groups_has_Authors_Authors1_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_Groups_has_Authors_Groups_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_Groups_has_Authors_Groups`
    FOREIGN KEY (`group_id`)
    REFERENCES `workshop_schema`.`WritingGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Groups_has_Authors_Authors1`
    FOREIGN KEY (`author_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`Review`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Review` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `text` LONGTEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  `Submission_id` INT NOT NULL,
  `Reviewer_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Submission_id`, `Reviewer_id`),
  INDEX `fk_Review_Submissions1_idx` (`Submission_id` ASC) VISIBLE,
  INDEX `fk_Review_Authors1_idx` (`Reviewer_id` ASC) VISIBLE,
  CONSTRAINT `fk_Review_Submissions1`
    FOREIGN KEY (`Submission_id`)
    REFERENCES `workshop_schema`.`Submissions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Review_Authors1`
    FOREIGN KEY (`Reviewer_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
