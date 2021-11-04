SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+08:00";

--
-- Database: `class`
--
CREATE DATABASE IF NOT EXISTS `class` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `class`;


-- --------------------------------------------------------
--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `classes`;
CREATE TABLE IF NOT EXISTS `classes` (
  `classId` varchar(64) NOT NULL,
  `courseId` varchar(64) NOT NULL,
  `courseName` varchar(500) NOT NULL,
  `classStartDate` varchar(50) NOT NULL,
  `classEndDate` varchar(50) NOT NULL,
  `classStartTime` varchar(50) NOT NULL,
  `classEndTime` varchar(50) NOT NULL,
  `classDay` varchar(50) NOT NULL,
  `currentClassSize` varchar(100) NOT NULL,
  `maxClassSize` varchar(100) NOT NULL,
  `acceptClassList` varchar(500) DEFAULT NULL,
  `enrolledClassList` varchar(1000) DEFAULT NULL,
  `employeeId` varchar(64) DEFAULT NULL,
  `employeeName` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`classID`, `courseId`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `class`
--

INSERT INTO `classes` (`classId`, `courseId`, `courseName`, `classStartDate`, `classEndDate`, `classStartTime`,`classEndTime`,`classDay`, `currentClassSize`, `maxClassSize`, `acceptClassList`, `enrolledClassList`, `employeeID`, `employeeName`) VALUES
('G1', 'X7845', 'Fundamentals of Xerox WorkCentre 7845', '23/09/2021', '01/10/2021','0900','1200','Wednesday', 0, 45, '', '', '1', 'Ms Preethi'),
('G2', 'X7845', 'Fundamentals of Xerox WorkCentre 7845', '23/09/2021', '01/10/2021','0900','1200','Friday', 30, 50, '', '3,4', '1', 'Ms Preethi'),
('G1', 'X7846', 'Programming for Xerox WorkCentre with Card Access and Integration', '27/09/2021', '07/11/2021','1400','1800','Friday', 44, 50, '', '4', '2', 'Mr Alan');

COMMIT;





