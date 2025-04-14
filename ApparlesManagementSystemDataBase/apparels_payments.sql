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
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `transaction_id` varchar(50) NOT NULL,
  `upi_id` varchar(100) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `status` enum('pending','success','failed') DEFAULT 'pending',
  PRIMARY KEY (`id`),
  UNIQUE KEY `transaction_id` (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (1,'1741687736','vidyeshym@ybl',10.00,'pending'),(2,'1741688132','vidyeshym@ybl',10.00,'pending'),(3,'1741690782','vidyeshym@ybl',10.00,'pending'),(4,'1741690802','vidyeshym@ybl',1.00,'pending'),(5,'1741692971','vidyeshym@ybl',10.00,'pending'),(7,'1741693566','vidyeshym@ybl',10.00,'pending'),(8,'1741693567','vidyeshym@ybl',10.00,'pending'),(9,'1741693570','vidyeshym@ybl',10.00,'pending'),(10,'1741693573','vidyeshym@ybl',10.00,'pending'),(11,'1741693576','vidyeshym@ybl',10.00,'pending'),(12,'1741693579','vidyeshym@ybl',10.00,'pending'),(13,'1741693582','vidyeshym@ybl',10.00,'pending'),(14,'1741693585','vidyeshym@ybl',10.00,'pending'),(15,'1741693588','vidyeshym@ybl',10.00,'pending'),(16,'1741693591','vidyeshym@ybl',10.00,'pending'),(17,'1741693594','vidyeshym@ybl',10.00,'pending'),(18,'1741693597','vidyeshym@ybl',10.00,'pending'),(19,'1741693600','vidyeshym@ybl',10.00,'pending'),(20,'1741693603','vidyeshym@ybl',10.00,'pending'),(21,'1741693606','vidyeshym@ybl',10.00,'pending'),(22,'1741693609','vidyeshym@ybl',10.00,'pending'),(23,'1741693612','vidyeshym@ybl',10.00,'pending'),(24,'1741693615','vidyeshym@ybl',10.00,'pending'),(25,'1741693619','vidyeshym@ybl',10.00,'pending'),(26,'1741693623','vidyeshym@ybl',10.00,'pending'),(27,'1741693627','vidyeshym@ybl',10.00,'pending'),(28,'1741693631','vidyeshym@ybl',10.00,'pending'),(29,'1741693635','vidyeshym@ybl',10.00,'pending'),(30,'1741693639','vidyeshym@ybl',10.00,'pending'),(31,'1741693643','vidyeshym@ybl',10.00,'pending'),(32,'1741693647','vidyeshym@ybl',10.00,'pending'),(33,'1741693651','vidyeshym@ybl',10.00,'pending'),(34,'1741693655','vidyeshym@ybl',10.00,'pending'),(35,'1741693659','vidyeshym@ybl',10.00,'pending'),(36,'1741693663','vidyeshym@ybl',10.00,'pending'),(37,'1741693667','vidyeshym@ybl',10.00,'pending'),(38,'1741693671','vidyeshym@ybl',10.00,'pending'),(39,'1741693675','vidyeshym@ybl',10.00,'pending'),(40,'1741693679','vidyeshym@ybl',10.00,'pending'),(41,'1741693683','vidyeshym@ybl',10.00,'pending'),(42,'1741693687','vidyeshym@ybl',10.00,'pending'),(43,'1741693691','vidyeshym@ybl',10.00,'pending'),(44,'1741693695','vidyeshym@ybl',10.00,'pending'),(45,'1741693699','vidyeshym@ybl',10.00,'pending'),(46,'1741693703','vidyeshym@ybl',10.00,'pending'),(47,'1741693708','vidyeshym@ybl',10.00,'pending'),(48,'1741693711','vidyeshym@ybl',10.00,'pending'),(49,'1741693714','vidyeshym@ybl',10.00,'pending'),(50,'1741693717','vidyeshym@ybl',10.00,'pending'),(51,'1741699904','vidyeshym@ybl',10.00,'pending'),(53,'1741699923','vidyeshym@ybl',1.00,'pending'),(55,'1741699955','vidyeshym@ybl',0.14,'pending'),(56,'1741699956','vidyeshym@ybl',0.14,'pending'),(57,'1741699959','vidyeshym@ybl',0.14,'pending'),(58,'1741699962','vidyeshym@ybl',0.14,'pending'),(59,'1741699965','vidyeshym@ybl',0.14,'pending'),(60,'1741699968','vidyeshym@ybl',0.14,'pending'),(61,'1741699973','vidyeshym@ybl',1.00,'pending'),(62,'1741699974','vidyeshym@ybl',1.00,'pending'),(64,'1741700128','vidyeshym@ybl',1.00,'pending'),(66,'1741700415','vidyeshym@ybl',1.00,'pending'),(68,'1741700449','vidyeshym@ybl',1.00,'pending'),(70,'1741700475','vidyeshym@ybl',1.00,'pending'),(72,'1741700490','vidyeshym@ybl',1.00,'pending'),(74,'1741700509','vidyeshym@ybl',1.00,'pending'),(76,'1741700548','vidyeshym@ybl',1.00,'pending'),(77,'1741700549','vidyeshym@ybl',1.00,'pending'),(79,'1741700552','vidyeshym@ybl',1.00,'pending'),(80,'1741700555','vidyeshym@ybl',1.00,'pending'),(81,'1741700592','vidyeshym@ybl',1.00,'pending'),(83,'1741700642','vidyeshym@ybl',1.00,'pending'),(85,'1741700697','vidyeshym@ybl',1.00,'pending'),(87,'1741776480','vidyeshym@ybl',1.00,'pending'),(88,'1741776597','vidyeshym@ybl',1.00,'pending'),(89,'1741777559','vidyeshym@ybl',1.00,'pending'),(90,'1742306671','vidyeshym@ybl',1.00,'pending'),(91,'1742306837','vidyeshym@ybl',1.00,'pending'),(92,'1742307934','vidyeshym@ybl',2999.00,'pending'),(93,'1742308913','vidyeshym@ybl',999.00,'pending'),(94,'1742308920','vidyeshym@ybl',999.00,'pending'),(95,'1742308974','vidyeshym@ybl',999.00,'pending'),(96,'1742308997','vidyeshym@ybl',2498.00,'pending'),(97,'1742309055','vidyeshym@ybl',2498.00,'pending'),(98,'1742309056','vidyeshym@ybl',2498.00,'pending'),(99,'1742309111','vidyeshym@ybl',2498.00,'pending'),(100,'1742309199','vidyeshym@ybl',999.00,'pending'),(101,'1742382909','vidyeshym@ybl',999.00,'pending'),(102,'1742383019','vidyeshym@ybl',999.00,'pending'),(103,'1742385568','vidyeshym@ybl',172179.00,'pending'),(104,'1742393841','vidyeshym@ybl',2299.00,'pending'),(105,'1742393847','vidyeshym@ybl',2299.00,'pending'),(106,'1742393983','vidyeshym@ybl',2299.00,'pending'),(107,'1742394712','vidyeshym@ybl',999.00,'pending'),(108,'1742394766','vidyeshym@ybl',3298.00,'pending'),(109,'1742395275','vidyeshym@ybl',2299.00,'pending'),(110,'1742395405','vidyeshym@ybl',3298.00,'pending'),(111,'1742395612','vidyeshym@ybl',2299.00,'pending'),(112,'1742402382','vidyeshym@ybl',4598.00,'pending'),(113,'1742402492','vidyeshym@ybl',6797.00,'pending'),(114,'1742402865','vidyeshym@ybl',2299.00,'pending'),(115,'1742403371','vidyeshym@ybl',3298.00,'pending'),(116,'1742468625','vidyeshym@ybl',7297.00,'pending'),(117,'1742659779','vidyeshym@ybl',5998.00,'pending'),(118,'1742659815','vidyeshym@ybl',6997.00,'pending'),(119,'1742659893','vidyeshym@ybl',5998.00,'pending'),(120,'1742659972','vidyeshym@ybl',5998.00,'pending'),(121,'1742700406','vidyeshym@ybl',2999.00,'pending'),(122,'1742732301','vidyeshym@ybl',2699.00,'pending'),(123,'1742813293','vidyeshym@ybl',2999.00,'pending'),(124,'1743843272','vidyeshym@ybl',1999.00,'pending'),(125,'1743843341','vidyeshym@ybl',2999.00,'pending'),(126,'1744429118','vidyeshym@ybl',2999.00,'pending');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-13 13:50:04
