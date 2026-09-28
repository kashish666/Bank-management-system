
CREATE DATABASE bank_management_system;
USE  bank_management_system;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: myproject
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `account_type_id` int DEFAULT NULL,
  `opening_date` date DEFAULT NULL,
  `balance` decimal(15,5) DEFAULT NULL,
  `status` enum('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',
  `account_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `account_number` (`account_number`),
  KEY `customer_id` (`customer_id`),
  KEY `account_type_id` (`account_type_id`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `account_ibfk_2` FOREIGN KEY (`account_type_id`) REFERENCES `account_types` (`account_type_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (101,101,1,'2026-09-17',198800.00000,'ACTIVE','ACC101'),(102,102,2,'2026-09-21',2000.00000,'ACTIVE','ACC102'),(103,107,1,'2026-09-26',4000.00000,'ACTIVE','ACC103');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_types`
--

DROP TABLE IF EXISTS `account_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account_types` (
  `account_type_id` int NOT NULL,
  `account_type_name` varchar(50) DEFAULT NULL,
  `minimum_balance` decimal(12,2) DEFAULT NULL,
  `interest_rate` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`account_type_id`),
  UNIQUE KEY `account_type_name` (`account_type_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_types`
--

LOCK TABLES `account_types` WRITE;
/*!40000 ALTER TABLE `account_types` DISABLE KEYS */;
INSERT INTO `account_types` VALUES (1,'saving',1000.00,3.50),(2,'current',2000.00,0.00);
/*!40000 ALTER TABLE `account_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank_statement`
--

DROP TABLE IF EXISTS `bank_statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_statement` (
  `statement_id` int NOT NULL AUTO_INCREMENT,
  `account_number` varchar(20) DEFAULT NULL,
  `transaction_type` enum('DEBIT','CREDIT') DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `balance_after` decimal(10,2) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `transaction_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `reference_id` int DEFAULT NULL,
  `account_number_to` varchar(20) DEFAULT NULL,
  `cust_id` int DEFAULT NULL,
  PRIMARY KEY (`statement_id`),
  KEY `account_number` (`account_number`),
  KEY `reference_id` (`reference_id`),
  KEY `fk_bank_to_ben` (`account_number_to`),
  KEY `cust_id` (`cust_id`),
  CONSTRAINT `bank_statement_ibfk_1` FOREIGN KEY (`account_number`) REFERENCES `account` (`account_number`),
  CONSTRAINT `bank_statement_ibfk_2` FOREIGN KEY (`reference_id`) REFERENCES `transfer_money` (`transfer_id`),
  CONSTRAINT `cust_id` FOREIGN KEY (`cust_id`) REFERENCES `customers` (`customer_id`),
  CONSTRAINT `fk_bank_to_ben` FOREIGN KEY (`account_number_to`) REFERENCES `beneficiaries` (`account_number`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_statement`
--

LOCK TABLES `bank_statement` WRITE;
/*!40000 ALTER TABLE `bank_statement` DISABLE KEYS */;
INSERT INTO `bank_statement` VALUES (1,'ACC101','CREDIT',1000.00,199400.00,NULL,'2026-09-19 16:45:28',NULL,NULL,NULL),(2,'ACC101','DEBIT',500.00,198900.00,NULL,'2026-09-19 16:45:41',NULL,NULL,NULL),(3,'ACC101','CREDIT',2000.00,200900.00,NULL,'2026-09-20 14:02:11',NULL,NULL,NULL),(4,'ACC102','CREDIT',2000.00,7000.00,NULL,'2026-09-21 14:43:48',NULL,NULL,NULL),(5,'ACC102','DEBIT',1000.00,6000.00,NULL,'2026-09-21 14:44:05',NULL,NULL,NULL),(6,'ACC102','CREDIT',5000.00,8000.00,NULL,'2026-09-21 16:08:11',NULL,NULL,NULL),(7,'ACC101','CREDIT',1000.00,200800.00,NULL,'2026-09-23 15:40:46',NULL,NULL,NULL),(8,'ACC101','DEBIT',1000.00,199800.00,NULL,'2026-09-23 15:40:56',NULL,NULL,NULL),(9,'ACC102','CREDIT',1000.00,3000.00,NULL,'2026-09-24 13:22:53',NULL,NULL,NULL),(10,'ACC102','DEBIT',1000.00,2000.00,NULL,'2026-09-24 13:23:04',NULL,NULL,NULL),(11,'ACC103','CREDIT',3000.00,5000.00,NULL,'2026-09-26 06:04:41',NULL,NULL,NULL),(12,'ACC103','DEBIT',1000.00,4000.00,NULL,'2026-09-26 06:04:52',NULL,NULL,NULL);
/*!40000 ALTER TABLE `bank_statement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `beneficiaries`
--

DROP TABLE IF EXISTS `beneficiaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `beneficiaries` (
  `beneficiary_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `beneficiary_name` varchar(100) DEFAULT NULL,
  `account_number` varchar(20) NOT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `ifsc_code` varchar(20) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  PRIMARY KEY (`beneficiary_id`),
  UNIQUE KEY `account_number` (`account_number`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `beneficiaries_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `beneficiaries`
--

LOCK TABLES `beneficiaries` WRITE;
/*!40000 ALTER TABLE `beneficiaries` DISABLE KEYS */;
INSERT INTO `beneficiaries` VALUES (1,101,'Nikita','ACCHDFC101','HDFC','123456','2026-09-18 00:00:00'),(4,102,'Shweta','ACCSBI102','SBI','345654','2026-09-21 00:00:00'),(6,101,'Aryan','ACCBOB101','BOB','456766','2026-09-23 00:00:00'),(7,102,'nidhi','ACCBOB102','BOB','454657','2026-09-24 00:00:00'),(8,107,'KASHISH','ACCBOB107','BOB','344566','2026-09-26 00:00:00');
/*!40000 ALTER TABLE `beneficiaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `phone_num` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `role` enum('customer','admin') DEFAULT 'customer',
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `phone_num` (`phone_num`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (101,'kashish','wasnik','2000-10-01','female','5555555555','kash@gmail.com','gorewada','nagpur','maharastra','440065','abc123','2026-09-16 15:40:47','customer'),(102,'saloni','wasnik','1990-05-12','female','56565656566','saloni@gmail.com','dabha','nagpur','maharastra','440045','kash','2026-09-16 15:43:32','customer'),(103,'nandini','wasnik','1997-08-12','female','8765438764','nandu@gmail.com','dabha','nagpur','maharastra','440023','nandini','2026-09-20 13:53:47','customer'),(104,'abuzar','ahmad','2000-09-12','male','33333333333','abuzar@gmail.com','kamthi','nagpur','maharastra','441313','abuzar@123','2026-09-21 06:36:57','customer'),(105,'ragini','wasnik','2000-07-12','female','222222222222','ragini@gmail.com','prakash nagar','nagpur','maharastra','440067','ragini','2026-09-21 14:29:06','customer'),(106,'sahil','wasnik','1990-02-12','male','333345754776','Sahil@gmail.com','dabha','nagpur','maharastra','440023','sahil123','2026-09-23 05:39:34','customer'),(107,'sachin','diyewar','2000-04-23','male','4567655456','sachin@gmail.com','dfghj','dfghj','dfgvhbjn','345667','sachin321','2026-09-26 06:02:19','customer');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_payments`
--

DROP TABLE IF EXISTS `loan_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `loan_id` int DEFAULT NULL,
  `payment_amount` decimal(15,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `remaining_amount` decimal(15,2) DEFAULT NULL,
  `payment_status` enum('PENDING','PAID') DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `loan_id` (`loan_id`),
  CONSTRAINT `loan_payments_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `loans` (`loan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_payments`
--

LOCK TABLES `loan_payments` WRITE;
/*!40000 ALTER TABLE `loan_payments` DISABLE KEYS */;
INSERT INTO `loan_payments` VALUES (1,1,43609.89,'2026-09-20',456390.11,'PAID'),(2,1,43609.89,'2026-09-20',412780.22,'PAID'),(3,4,55097.39,'2026-09-21',1144902.61,'PAID'),(4,2,47073.47,'2026-09-23',952926.53,'PAID');
/*!40000 ALTER TABLE `loan_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loans` (
  `loan_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int DEFAULT NULL,
  `loan_type` varchar(50) DEFAULT NULL,
  `loan_amount` decimal(15,2) DEFAULT NULL,
  `loan_duration` int DEFAULT NULL,
  `interest_rate` decimal(5,2) DEFAULT NULL,
  `application_date` date DEFAULT NULL,
  `loan_status` enum('PENDING','APPROVED','REJECTED') DEFAULT 'PENDING',
  PRIMARY KEY (`loan_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `loans_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
INSERT INTO `loans` VALUES (1,101,'HOME',500000.00,12,8.50,'2026-09-20','APPROVED'),(2,101,'PERSONAL',1000000.00,24,12.00,'2026-09-20','APPROVED'),(3,101,'HOME',1000000.00,12,8.50,'2026-09-21','REJECTED'),(4,102,'CAR',1200000.00,24,9.50,'2026-09-21','PENDING'),(5,103,'EDUCTAION',1500000.00,24,12.00,'2026-09-21','PENDING'),(6,102,'EDUCATION',600000.00,36,7.00,'2026-09-21','PENDING'),(7,101,'CAR',1500000.00,36,9.50,'2026-09-23','APPROVED'),(8,102,'EDUCATION',400000.00,12,7.00,'2026-09-24','PENDING'),(9,107,'HOM',1200000.00,12,12.00,'2026-09-26','PENDING');
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transfer_money`
--

DROP TABLE IF EXISTS `transfer_money`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transfer_money` (
  `transfer_id` int NOT NULL AUTO_INCREMENT,
  `account_number_from` varchar(20) DEFAULT NULL,
  `beneficiary_id` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `status` enum('SUCCESS','FAILED','PENDING') DEFAULT 'PENDING',
  `transfer_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `account_table_to` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`transfer_id`),
  KEY `account_number_from` (`account_number_from`),
  KEY `beneficiary_id` (`beneficiary_id`),
  CONSTRAINT `transfer_money_ibfk_1` FOREIGN KEY (`account_number_from`) REFERENCES `account` (`account_number`),
  CONSTRAINT `transfer_money_ibfk_2` FOREIGN KEY (`beneficiary_id`) REFERENCES `beneficiaries` (`beneficiary_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transfer_money`
--

LOCK TABLES `transfer_money` WRITE;
/*!40000 ALTER TABLE `transfer_money` DISABLE KEYS */;
INSERT INTO `transfer_money` VALUES (1,'ACC101',1,1000.00,'SUCCESS','2026-09-18 20:04:15','ACCHDFC101'),(2,'ACC101',1,100100.00,'SUCCESS','2026-09-18 20:07:20','ACCHDFC101'),(3,'ACC101',1,21000.00,'SUCCESS','2026-09-18 20:24:28','ACCHDFC101'),(4,'ACC101',1,19000.00,'SUCCESS','2026-09-19 14:10:37','ACCHDFC101'),(5,'ACC101',1,21000.00,'SUCCESS','2026-09-19 14:18:16','ACCHDFC101'),(6,'ACC101',1,200.00,'SUCCESS','2026-09-19 14:18:49','ACCHDFC101'),(7,'ACC101',1,100000.00,'SUCCESS','2026-09-19 14:22:02','ACCHDFC101'),(8,'ACC101',1,500.00,'SUCCESS','2026-09-19 14:23:39','ACCHDFC101'),(9,'ACC101',1,400.00,'SUCCESS','2026-09-19 14:24:06','ACCHDFC101'),(10,'ACC101',1,500.00,'SUCCESS','2026-09-19 14:24:33','ACCHDFC101'),(11,'ACC101',1,500.00,'SUCCESS','2026-09-19 14:24:55','ACCHDFC101'),(16,'ACC101',1,100.00,'SUCCESS','2026-09-22 13:51:07','ACCHDFC101'),(20,'ACC101',1,1000.00,'SUCCESS','2026-09-23 15:39:21','ACCHDFC101'),(21,'ACC101',1,1000.00,'SUCCESS','2026-09-23 15:41:34','ACCHDFC101');
/*!40000 ALTER TABLE `transfer_money` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-28 19:58:07
