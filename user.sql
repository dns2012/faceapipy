-- Adminer 4.7.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `address` text NOT NULL,
  `image` varchar(255) NOT NULL,
  `sample_image` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `user` (`id`, `name`, `username`, `password`, `phone`, `address`, `image`, `sample_image`, `created_at`, `updated_at`) VALUES
(1,	'Aji',	'aji',	'acception',	89643385968,	'Aji Address',	'aji_sample.jpg',	'aji_sample.jpg',	'2019-05-14 02:48:48',	'2019-05-14 02:48:48'),
(2,	'Fadil',	'fadil',	'acception',	89643385968,	'Fadil Address',	'fadil_sample.jpg',	'fadil_sample.jpg',	'2019-05-14 02:48:48',	'2019-05-14 02:48:48'),
(3,	'Viko',	'viko',	'acception',	89643385968,	'Viko Address',	'viko_sample.jpg',	'viko_sample.jpg',	'2019-05-14 02:48:48',	'2019-05-14 02:48:48'),
(4,	'Yosa',	'yosa',	'acception',	89643385968,	'Yosa Address',	'yosa_sample.jpg',	'yosa_sample.jpg',	'2019-05-14 02:48:48',	'2019-05-14 02:48:48'),
(5,	'Dani',	'dani',	'acception',	89643385968,	'Dani Address',	'dani_sample.jpg',	'dani_sample_dark.jpg',	'2019-05-14 02:48:48',	'2019-05-14 02:48:48');

-- 2019-05-15 23:54:12
