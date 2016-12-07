-- MySQL dump 10.16  Distrib 10.1.10-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: hilmi
-- ------------------------------------------------------
-- Server version	10.1.10-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `main_data`
--

DROP TABLE IF EXISTS `main_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tanggal` date NOT NULL,
  `transaksi` varchar(32) NOT NULL,
  `harga` varchar(32) NOT NULL,
  `jenis` int(11) NOT NULL,
  `debet` int(11) NOT NULL,
  `kredit` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_data`
--

LOCK TABLES `main_data` WRITE;
/*!40000 ALTER TABLE `main_data` DISABLE KEYS */;
INSERT INTO `main_data` VALUES (1,'2011-12-01','Material Kayu Lambung','7800000',0,0,0),(2,'2011-12-01','Material Kayu Deck','7000000',1,0,1),(3,'2011-12-02','Material Kayu Gading','1000000',2,1,2),(4,'2011-12-03','Lem','200000',3,2,2),(5,'2011-12-04','Sekrup','1500000',4,1,3),(6,'2011-12-05','Paku Stenlis','350000',5,3,3),(7,'2011-12-06','Cat','300000',6,4,0),(8,'2011-12-07','pakal','284373',7,4,4),(9,'2011-12-08','Tangki Bahan Bakar','2112500',8,5,0),(10,'2011-12-09','Mesin Utama','5335175',9,6,0),(11,'2011-12-10','alat tangkap','5335175',10,2,0),(12,'2011-12-11','perlengkapan navigasi','4975175',11,7,0),(13,'2011-12-12','perlengkapan keselamatan','7800000',12,1,5),(14,'2011-12-13','perlengkapan pemadam kebakaran','7000000',13,8,0),(15,'2011-12-14','peralatan tambahan ','1000000',14,1,1),(16,'2011-12-15','gaji kepala tukang','200000',15,2,6),(17,'2011-12-16','gaji pekerja','1500000',16,1,4),(18,'2011-12-17','biaya listrik','350000',17,9,0),(19,'2011-12-18','biaya air','300000',18,10,7),(20,'2011-12-19','biaya telpon','284373',19,11,0),(21,'2011-12-20','paku kayu','2112500',20,12,8),(22,'2011-12-21','alat alat pemotong kayu','5335175',21,13,9),(23,'2011-12-22','biaya sewa kendaraan ','5335175',22,14,0),(24,'2011-12-23','dana tak terduga ','4975175',23,14,3);
/*!40000 ALTER TABLE `main_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-07 16:35:48
