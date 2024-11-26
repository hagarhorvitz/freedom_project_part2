-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: freedom
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `country_name` varchar(100) NOT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Israel'),(2,'Spain'),(3,'Italy'),(4,'Thailand'),(5,'Mexico'),(6,'Japan'),(7,'Greece'),(8,'Germany'),(9,'France'),(10,'Panama'),(11,'New York'),(12,'United kingdom'),(13,'Cyprus'),(14,'Africa'),(15,'Egypt');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `user_id` int NOT NULL,
  `vacation_id` int NOT NULL,
  KEY `userId_idx` (`user_id`),
  KEY `vacationId_idx` (`vacation_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `vacation_id` FOREIGN KEY (`vacation_id`) REFERENCES `vacations` (`vacation_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (42,18),(2,7),(2,18),(44,19),(42,17),(44,8),(44,1),(42,1),(42,19),(45,5),(45,19),(45,18);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_title` varchar(45) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `roleId_idx` (`role_id`),
  CONSTRAINT `role_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Hagar','Horvitz','hagar@gmail.com','shraga12345',1),(2,'Gali','Ginsburg','gali@gmail.com','mona123',2),(42,'Mona','Shuli','ms@gmail.com','3d6c5cfb77a8aa46a013af69ce55e61070e21c3f1d84275cb902ebebf1676a73b7a128b2f89e6169a78186b4c58a8fc11eb047a38e841959e087e00e8975c2b2',2),(43,'Shraga','Black','shraga@gmail.com','c9f284be4c6df017db4dcc4c3362fb519261eac400114a2d3d6b906eab5683b893bcb45b201574c511ad3c4a8f325caf422325ca013612a7521133ef7237885a',1),(44,'Maya','Korman','maya@gmail.com','06665037e4743bda582b46fbe337405b82a27d6371b026222f6eb454f4fa52906ef0b510567d56a6cd163bd8696b67e2547d47729970a892ba1c9de187f8a3f0',2),(45,'Lena','Badash','lena@gmail.com','dc313faa5fd1dde57751bed91e9315ffa1dc980c27d272f82def6b6cee33a0729d83fa023ffa00905b506d3f647ea4607d3697f389eefe19d1b1c64d44adaf58',2),(46,'Ori','Bina','ori@gmail.com','05ecf0c8ebe53ef77269acbe28aef95143fce6032c636b3775be03add40643a213f86bbc2092318311fa9212a454ecd40ad09b0b8c7c22f72d7b677c984050f7',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacation_id` int NOT NULL AUTO_INCREMENT,
  `country_id` int NOT NULL,
  `description` varchar(250) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` int NOT NULL,
  `image_name` varchar(300) NOT NULL,
  PRIMARY KEY (`vacation_id`),
  KEY `countryId_idx` (`country_id`),
  CONSTRAINT `country_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (1,3,'Walk in the beautiful streets of Rome, Italy. Enjoy geart food and wine or cold Aperol all day','2024-05-22','2024-05-26',6000,'12338461-3188-4c27-8853-fcd0441b7731.jpg'),(5,5,'Want to run from the cold? Book your next vacation to the sunny Mexico. Beautiful white beaches, nonstop margaritas and tacos, and party all day and night!','2024-12-28','2025-01-18',10000,'da7ca0e7-2c5f-486c-9ad2-67f1cab4d3af.jpg'),(6,4,'Visit the gorgeous Thailand! Relax and have a massage everyday, drink unique cocktails and local cuisine. Do not forget to come to a fullmoon party!!','2025-03-23','2025-04-07',10000,'a7915b75-921d-4fc7-9184-11f2dfce3d84.jpg'),(7,8,'Check out unique and interesting Berlin. Visit all historical places and the best crazy parties at night! Do not forget to try all the beers of all over the world in th famous Oktoberfest','2024-10-01','2024-10-06',6700,'a82201b0-30d6-44fa-8959-82b60f991daa.jpg'),(8,2,'Visit gorgeous Madrid, Spain this coming summer! Beautiful wether, people and architecture. Try our local special restaurants and fun speakeasy bars.','2024-08-22','2024-08-27',7200,'9455f71e-4291-4506-9ea1-f34f5ff53f8d.jpg'),(9,10,'Perfect getaway to connect the nature! Visit the beautiful beaches of Bocas Del Toro, Panama. Check the wild sealife with some snorkeling and try our local special dishes.','2025-01-30','2025-02-20',10000,'60f53ed8-8f4c-4f40-98a1-0e53aaa8325c.jpg'),(12,7,'Enjoy this summer in our new exclusive resort, adults ONLY!!, in Paros. Authentic Greece just like you imagine! Check out town\'s beaches or take the boat to find secret beaches. Party day & night in the local taverns with great music, food and drinks','2024-08-03','2024-08-10',9500,'9b727807-cfe4-4c48-9171-65e454623a5e.jpg'),(17,11,'Embarking on a vacation to New York City is like stepping into a world where every corner holds a new adventure. From the moment you arrive, the city\'s iconic skyline greets you with the promise of endless possibilities.','2025-03-12','2025-03-25',10000,'2480ed2e-2898-4527-b07f-76c1ab7a9925.jpg'),(18,1,'Explore Israel\'s charm, where ancient history meets modern vibrancy! Wander through Jerusalem, relax in the Dead Sea, try Middle Eastern delights, and experience diverse landscapes from the Negev Desert to Tel Aviv\'s lively nightlife!','2025-02-11','2025-02-16',9900,'ad688720-e591-4ad5-bc7f-8a3776a16a09.jpg'),(19,7,'Relax in beautiful Athens,Greece. Try authentic mediterranean food and the local Ouzo in our Taverns','2024-08-29','2024-09-02',8600,'de587651-7e50-4899-9f16-9a04782c2cc4.jpg'),(20,9,'Have your romantic vacation in Paris, France. Visit the Eiffel tower, the Louvre and do not forget to save a full fun day in Disneyland!!\r\n','2025-03-05','2025-03-09',7700,'cdac6de8-f5d0-48d3-a58c-de3e5ea1ea1a.jpg'),(22,5,'Want to have a perfect getaway from school and have the time of your life? We have special deals for winter break in sunny, exotic Cancun, Mexico!! Sun, amazing beaches, alcohol, party day and night!','2024-12-19','2024-12-29',8850,'3a7fad19-c854-4eab-8a79-c1ed9ec43f2f.jpg');
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-02 23:07:57
