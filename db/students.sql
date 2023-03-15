CREATE DATABASE pbl;
use pbl;

CREATE TABLE `student` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `student_id` varchar(50) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `faculty` varchar(50) NOT NULL,
  `class` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `student`(`id`,`student_id`,`full_name`,`faculty`,`class`) values 
(1,'102200023','Van Phu Long',"CNTT",'20T1'),
(2,'102200024','Van Phu Long',"CNTT",'20T1'),
(3,'102200025','Van Phu Long',"CNTT",'20T1');