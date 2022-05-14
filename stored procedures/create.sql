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
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `firstname` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`, `username`, `email`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`Genres`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Genres` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Genres` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `short_description` VARCHAR(45) NULL,
  `description` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`, `name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`WritingGroups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`WritingGroups` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`WritingGroups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255) NULL,
  `short_description` VARCHAR(45) NULL,
  `founding_date` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() on UPDATE NOW(),
  `Creator_id` INT NOT NULL,
  `Genre_id` INT NOT NULL,
  PRIMARY KEY (`id`, `name`),
  INDEX `fk_Groups_Authors1_idx` (`Creator_id` ASC) VISIBLE,
  INDEX `fk_WritingGroups_Genres1_idx` (`Genre_id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  CONSTRAINT `fk_Groups_Creator1`
    FOREIGN KEY (`Creator_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Groups_Genre1`
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
  `entry_description` VARCHAR(255) NULL,
  `entry_text` LONGTEXT NULL,
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
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`id`, `group_id`, `author_id`),
  INDEX `fk_Groups_has_Authors_Authors1_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_Groups_has_Authors_Groups_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_Groups_has_Authors_WritingGroups`
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
-- Table `workshop_schema`.`Reviews`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Reviews` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `review_text` LONGTEXT NULL,
  `rating` INT NULL,
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


-- -----------------------------------------------------
-- Table `workshop_schema`.`Invitations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`Invitations` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`Invitations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `invitee_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`, `invitee_id`, `group_id`),
  INDEX `fk_Authors_has_Authors_Authors2_idx` (`invitee_id` ASC) VISIBLE,
  INDEX `fk_Authors_has_Authors_WritingGroups1_idx` (`group_id` ASC) VISIBLE,
  CONSTRAINT `fk_Authors_has_Authors_Authors2`
    FOREIGN KEY (`invitee_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Authors_has_Authors_WritingGroups1`
    FOREIGN KEY (`group_id`)
    REFERENCES `workshop_schema`.`WritingGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `workshop_schema`.`GroupRequests`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `workshop_schema`.`GroupRequests` ;

CREATE TABLE IF NOT EXISTS `workshop_schema`.`GroupRequests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Requestor_id` INT NOT NULL,
  `Group_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Requestor_id`, `Group_id`),
  INDEX `fk_Authors_has_Groups_Groups1_idx` (`Group_id` ASC) VISIBLE,
  INDEX `fk_Authors_has_Groups_Authors1_idx` (`Requestor_id` ASC) VISIBLE,
  CONSTRAINT `fk_Authors_has_Groups_Authors1`
    FOREIGN KEY (`Requestor_id`)
    REFERENCES `workshop_schema`.`Authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Authors_has_Groups_Groups1`
    FOREIGN KEY (`Group_id`)
    REFERENCES `workshop_schema`.`WritingGroups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
