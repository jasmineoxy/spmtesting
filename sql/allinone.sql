SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+08:00";

--
-- Database: `allinone`
--
CREATE DATABASE IF NOT EXISTS `allinone` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `allinone`;

-- --------------------------------------------------------
--
-- Table structure for table `employee`
--
DROP TABLE IF EXISTS `Employee`;
CREATE TABLE IF NOT EXISTS `Employee` ( 
  `employeeId` varchar(64) NOT NULL,
  `employeeName` varchar(64) NOT NULL,
  `department` varchar(64) NOT NULL, -- hr, seniorEngineer, juniorEngineer
  `role` varchar(64) NOT NULL, -- admin, trainer, learner
  PRIMARY KEY (`employeeId`),
  INDEX(`employeeID`, `employeeName`)
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

-- --------------------------------------------------------
--
-- Table structure for table `course`
--
DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `courseId` varchar(1000) NOT NULL,
  `courseName` varchar(1000) NOT NULL,
  `courseDescription` varchar(1000) NOT NULL,
  `coursePrereq` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`courseID`),
  INDEX (`courseName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`courseId`, `courseName`, `courseDescription`, `coursePrereq`) VALUES
      ('X7845' , 'Fundamentals of Xerox WorkCentre 7845' , 'Fundamentals of Xerox work center' ,' '),
      ('X7846' , 'Programming for Xerox WorkCentre with Card Access and Integration' , 'Programming for Xerox WorkCentre with Card Access and Integration' ,'X7845');
COMMIT;

-- --------------------------------------------------------
--
-- Table structure for table `classes`
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
  `employeeId` varchar(64) DEFAULT NULL,
  `employeeName` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`classID`, `courseId`),
  FOREIGN KEY (`courseName`) REFERENCES course(`courseName`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`employeeID`,`employeeName`) REFERENCES Employee(`employeeID`,`employeeName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`classId`, `courseId`, `courseName`, `classStartDate`, `classEndDate`, `classStartTime`,`classEndTime`,`classDay`, `currentClassSize`, `maxClassSize`, `employeeID`, `employeeName`) VALUES
('G1', 'X7845', 'Fundamentals of Xerox WorkCentre 7845', '23/09/2021', '01/10/2021','0900','1200','Wednesday', 0, 45, '1', 'Ms Preethi'),
('G2', 'X7845', 'Fundamentals of Xerox WorkCentre 7845', '23/09/2021', '01/10/2021','0900','1200','Friday', 30, 50, '1', 'Ms Preethi'),
('G1', 'X7846', 'Programming for Xerox WorkCentre with Card Access and Integration', '27/09/2021', '07/11/2021','1400','1800','Friday', 44, 50, '2', 'Mr Alan');
COMMIT;

-- --------------------------------------------------------
--
-- Table structure for table `enrolledClassList`
--

DROP TABLE IF EXISTS `enrolledClassList`;
CREATE TABLE IF NOT EXISTS `enrolledClassList` (
  `classId` varchar(64) NOT NULL,
  `courseId` varchar(64) NOT NULL,
  `employeeId` varchar(64) NOT NULL,
  `employeeName` varchar(64) NOT NULL,
  PRIMARY KEY (`classID`, `courseId`, `employeeId`),
  FOREIGN KEY (`classId`) REFERENCES classes(`classId`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`courseId`) REFERENCES course(`courseId`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`employeeID`,`employeeName`) REFERENCES Employee(`employeeID`,`employeeName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `enrolledClassList`
--

INSERT INTO `enrolledClassList` (`classId`, `courseId`, `employeeId`, `employeeName`) VALUES
      ('G2', 'X7845', '3', 'John Doe'),
      ('G2', 'X7845', '4', 'Jane Goh'),
      ('G1', 'X7846', '4', 'Jane Goh');
COMMIT;

-- --------------------------------------------------------
--
-- Table structure for table `acceptClassList`
--

DROP TABLE IF EXISTS `acceptClassList`;
CREATE TABLE IF NOT EXISTS `acceptClassList` (
  `classId` varchar(64) NOT NULL,
  `courseId` varchar(64) NOT NULL,
  `employeeId` varchar(64) NOT NULL,
  `employeeName` varchar(64) NOT NULL,
  PRIMARY KEY (`classID`, `courseId`, `employeeId`),
  FOREIGN KEY (`classId`) REFERENCES classes(`classId`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`courseId`) REFERENCES course(`courseId`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`employeeID`,`employeeName`) REFERENCES Employee(`employeeID`,`employeeName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------
--
-- Table structure for table `learner`
--

DROP TABLE IF EXISTS `learner`;
CREATE TABLE IF NOT EXISTS `learner` ( 
  `employeeId` varchar(64) NOT NULL,
  `employeeName` varchar(64) NOT NULL,
  `learnerCoursesCompleted` varchar(64) NULL,
  `learnerCoursesInProgress` varchar(64) NULL,
  PRIMARY KEY (`employeeId`),
  FOREIGN KEY (`employeeID`,`employeeName`) REFERENCES Employee(`employeeID`,`employeeName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `learner` (`employeeId`, `employeeName`,`learnerCoursesCompleted`,`learnerCoursesInProgress`) VALUES
    ('3', 'John Doe', 'X7845','X7846'), 
    ('4', 'Jane Goh', 'X7846',''),
    ('5', 'Jackson Ong','', ''),
    ('7', 'Janet Jackson','X7845', 'X7846');
COMMIT;

-- --------------------------------------------------------
--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
CREATE TABLE IF NOT EXISTS `section` ( 
  `courseId` varchar(64) NOT NULL,
  `classId` varchar(64) NOT NULL,
  `sectionId` varchar(64) NOT NULL,
  `sectionTitle` varchar(200) NOT NULL,
  `estimatedTime` varchar(64) NOT NULL, 
  `content` text NULL,
  PRIMARY KEY (`courseId`, `classId`, `sectionId`),
  FOREIGN KEY (`courseId`) REFERENCES course(`courseId`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`classId`) REFERENCES classes(`classId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `section` (`courseId`, `classId`,`sectionId`, `sectionTitle`, `estimatedTime`, `content`) VALUES
    ('X7845', 'G1','S1', 'Section 1 - Introduction', '100', 'Integer faucibus massa augue, mollis ornare eros semper ut. Proin ac justo eget elit ornare consequat. Proin ac metus ac felis viverra aliquet. Vivamus maximus, lorem quis volutpat condimentum, mauris lacus placerat neque, et porta elit nulla vel enim. Quisque quam lacus, hendrerit et tempus at, elementum quis erat. Praesent vestibulum, ante et fringilla dictum, ante velit lacinia ex, ac sodales elit lacus non dolor. Nunc tincidunt elementum dolor vel ultrices. Nunc faucibus nisi vel turpis semper luctus. Etiam hendrerit feugiat ultricies.'), 
    ('X7845', 'G2','S1', 'Section 1 - Get to know the basics', '100',  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis venenatis nibh eget libero eleifend fermentum. Cras pulvinar molestie luctus. Mauris elementum odio ac facilisis mollis. Curabitur placerat scelerisque turpis sed rhoncus. Sed dapibus faucibus mi nec malesuada. Etiam posuere justo a dolor rutrum maximus vitae et est. Aliquam pretium lectus nisl, porta tincidunt nulla pellentesque eget. Donec sit amet elementum arcu. Sed scelerisque erat nec enim auctor, nec gravida sapien egestas. Donec id enim non velit tincidunt tincidunt. Suspendisse potenti. Suspendisse rhoncus fringilla libero. Pellentesque facilisis eros eget sapien dignissim feugiat. Duis fermentum lorem ut neque sagittis mattis. Duis in est augue. Integer aliquam pretium enim. Suspendisse vulputate nunc non efficitur feugiat. Nulla purus est, malesuada vel metus id, mattis posuere dolor. Cras fermentum nisl sed sem congue scelerisque. Cras suscipit aliquet lacus eu faucibus. Donec eget elit ipsum. Nam eros nisl, mollis vitae aliquet non, bibendum ac metus. Vivamus egestas, neque a eleifend malesuada, augue eros consectetur justo, et vestibulum magna metus vitae nisi. Ut eget finibus enim. Vivamus tincidunt tellus quis arcu cursus auctor. Integer nec consequat lorem. Quisque mi neque, pulvinar ut vestibulum eget, bibendum eu sem. Fusce bibendum nisl sed massa iaculis efficitur. In at viverra enim. Aenean egestas viverra magna quis blandit. In ac enim at diam lobortis sagittis. Fusce ornare interdum lectus eu dictum. Nulla vel ipsum hendrerit, molestie turpis eu, feugiat dui. Sed at vestibulum justo, id facilisis enim. Aenean euismod nisl ultricies, feugiat leo non, dignissim massa. Morbi purus magna, semper in dolor in, scelerisque tincidunt ipsum. Vivamus tincidunt sem ante, eget elementum purus rhoncus vel. Aenean risus odio, vulputate ac mi sed, ullamcorper faucibus odio. Donec eget fringilla tellus. Donec turpis est, suscipit eu porttitor vel, hendrerit vel ipsum. Etiam accumsan convallis metus, aliquam scelerisque tortor molestie nec. Cras elit sapien, fringilla nec lacinia tempus, gravida sit amet lectus. Nulla tempus tortor et mattis lobortis.'),
    ('X7845', 'G2', 'S2', 'Section 2 - Discover more about Xerox WorkCentre', '300',  'Mauris ornare molestie enim. Sed pulvinar at mi ut semper. Fusce feugiat eu turpis eu bibendum. Donec ut metus placerat, scelerisque risus ut, iaculis magna. Vivamus tortor arcu, faucibus eget luctus eu, hendrerit vel lorem. Nam at dui ac lacus dictum iaculis imperdiet ac turpis. Phasellus sit amet ex finibus, efficitur sem sed, scelerisque dui. Nullam sagittis velit nec neque porta, sit amet rhoncus magna molestie. Phasellus tempor risus sit amet sapien varius, vel consequat nunc iaculis. Sed a vehicula ipsum. Donec libero sem, eleifend a viverra eu, aliquam vel dui. Proin nec turpis interdum, maximus libero laoreet, imperdiet mauris. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec consectetur leo libero, eget consequat nisl vulputate eget. Maecenas vitae sapien orci. Fusce augue ante, dictum nec vulputate ac, gravida in est. Integer quis venenatis nunc. Mauris commodo nibh in lectus volutpat dapibus. Suspendisse magna enim, feugiat ut ipsum at, ultrices venenatis risus. Pellentesque et orci venenatis, ultrices erat et, ornare neque. Cras tincidunt varius elit, cursus tincidunt eros porttitor ac. Sed gravida sodales tempus. Aenean ultrices felis quam, vitae mollis lacus rhoncus nec. Donec feugiat felis malesuada magna volutpat sollicitudin. Duis scelerisque faucibus sapien sit amet ultrices. Nam vel vulputate tortor, nec condimentum magna. Curabitur vel nibh eget dui aliquet ornare. Quisque finibus accumsan egestas. Ut eu ex faucibus, efficitur erat vel, malesuada neque. Etiam vestibulum ac eros a aliquam.'),
    ('X7846', 'G1', 'S1', 'Section 1 - Introduction', '90', 'Aenean suscipit augue orci, sed imperdiet tortor sollicitudin molestie. Maecenas vulputate nibh semper leo egestas lacinia. Proin quis rutrum sapien. Aliquam non aliquet felis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam quis metus volutpat, porta ex sed, molestie sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.');
COMMIT;
