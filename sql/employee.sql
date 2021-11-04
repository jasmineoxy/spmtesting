-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Employee`
--
CREATE DATABASE IF NOT EXISTS `Employee` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Employee`;

-- --------------------------------------------------------

--
-- Table structure for table `Employee'
--

DROP TABLE IF EXISTS `Employee`;
CREATE TABLE IF NOT EXISTS `Employee` ( 
  `employeeId` varchar(64) NOT NULL,
  `employeeName` varchar(64) NOT NULL,
  `department` varchar(64) NOT NULL, -- hr, seniorEngineer, juniorEngineer
    `role` varchar(64) NOT NULL, -- admin, trainer, learner
  PRIMARY KEY (`employeeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`employeeId`, `employeeName`, `department`, `role`) VALUES
    ('1', 'Ms Preethi', 'seniorEngineer', 'trainer'),
    ('2', 'Mr Alan', 'seniorEngineer', 'trainer'),
    ('3', 'John Doe', 'juniorEngineer', 'learner' ),
    ('4', 'Jane Goh', 'juniorEngineer', 'learner'),
    ('5', 'Jackson Ong', 'juniorEngineer', 'learner'),
    ('6', 'Nancy Drew', 'hr', 'admin'),
    ('7', 'Janet Jackson', 'juniorEngineer', 'learner');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
