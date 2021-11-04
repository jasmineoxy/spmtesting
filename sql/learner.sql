SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `learner` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `learner`;

DROP TABLE IF EXISTS `learner`;
CREATE TABLE IF NOT EXISTS `learner` ( 
  `employeeId` varchar(64) NOT NULL,
  `learnerCoursesCompleted` varchar(64) NULL,
  `learnerCoursesInProgress` varchar(64) NULL,

  PRIMARY KEY (`employeeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `learner` (`employeeId`, `learnerCoursesCompleted`,`learnerCoursesInProgress`) VALUES
    ('3', 'X7845','X7846'), 
    ('4', 'X7846',''),
    ('5', ''),
    ('7', 'X7845, X7846');
COMMIT;