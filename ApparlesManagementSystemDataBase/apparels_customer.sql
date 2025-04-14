-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: apparels
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `user_id` varchar(15) NOT NULL DEFAULT '',
  `user_name` varchar(45) NOT NULL,
  `user_mobl` varchar(11) DEFAULT NULL,
  `user_email` varchar(45) NOT NULL,
  `user_address` varchar(50) NOT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('1234567890','Soham Jadhav','1234567890','soham@gmail.com','Mumbai','$2b$12$cJfm4MbvPgxRStJh4oFCr.u5fjbzm6v1r7aTg6t7hT3IaRN.jzs4S'),('7447487455','Sunayna Kamble','7447487455','Sunayna@gmail.com','Nashik','$2b$12$lymtWxUtM2FAEVPvszOF/e8qJpEIJBnliGmkTUKbcT6zo1kgRpy6m'),('7447497455','Mayuresh','7447497455','kamblesunayna65@gmail.com','nashik','$2b$12$V2wjTWDv9a.JAoe.zWFrAOIG0l2vSmne4SN5K3Xk6mhbpe06aEIgO'),('9284939555','Sakshi Kate','9284939555','vidyeshmit@outlook.com','Nashik, Pathrdi Phata','$2b$12$jMK6bAUitovr1hHUPrcnwOr5duySU.o38Xrq4qvlMI1f6Vbo7wpgG'),('9284939599','Vidyesh Kamble','9284939599','vidyeshmy@gmail.com','Pune','$2b$12$X570MCwCSvKD575izamxmObLeRsSa6NGmeybIfltauRzksDzk0Kra'),('9987561131','kamble','9987561131','kamble@gmail.com','Nashik','$2b$12$05clWdrvAxjIy8qonWxVxOyUjirJI0RS.ugkOq.id6ei1L0JR0ebm'),('9999999999','demo','9999999999','99@gmail.com','demo','$2b$12$l8ywZ6RwwTFCic2EZaAEcuo/A18D.ghL7uJdV.DBjOCrFIeE1E4wS'),('vidyesh_17','Kamble Vidyesh','1231231234','vidyeshmit@outlook.com','Pune ','$2b$12$loNqK8UxkXF339iblLhbcOFLaP7KJ15lFX/Yvjg97MqVRGE1SeoOK');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-13 13:50:05
