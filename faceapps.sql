-- Adminer 4.7.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `present`;
CREATE TABLE `present` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `image` varchar(255) NOT NULL,
  `similiar` int(11) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `present` (`id`, `user_id`, `image`, `similiar`, `latitude`, `longitude`, `created_at`, `updated_at`) VALUES
(1,	5,	'test.jpg',	62,	'52352,523423',	'5235252423',	'2019-05-19 20:50:42',	'2019-05-19 20:50:42');

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `address` text NOT NULL,
  `image` varchar(255) NOT NULL,
  `sample_image` varchar(255) NOT NULL,
  `status` enum('0','1') NOT NULL DEFAULT '0' COMMENT '0=offline, 1=online',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `user` (`id`, `name`, `email`, `username`, `password`, `phone`, `address`, `image`, `sample_image`, `status`, `created_at`, `updated_at`) VALUES
(5,	'Dani S',	'dani@canisnfelis.com',	'dnsprogress',	'c14bcebc5b4cd0c7fce90c3806188619',	6289643385968,	'Jalan Nangka RT 2 RW 3 Pohsangit Kidul Kecamatan Kademangan Probolinggo',	'2019-05-19T102523user-default.png',	'dani_sample.jpg',	'0',	'2019-05-14 02:48:48',	'2019-05-19 18:02:20');

-- 2019-05-19 13:55:58
