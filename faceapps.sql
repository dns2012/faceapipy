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
(5,	'USER 1',	'user1@faceapps.com',	'user1',	'24c9e15e52afc47c225b757e7bee1f9d',	6281001110001,	'USER 1 ADDRESS',	'default-user.png',	'user1_sample.jpg',	'0',	'2019-05-21 02:48:48',	'2019-05-21 18:02:20'),
(7,	'USER 2',	'user2@faceapps.com',	'user2',	'7e58d63b60197ceb55a1c487989a3720',	6281001110001,	'USER 2 ADDRESS',	'default-user.png',	'user2_sample.jpg',	'0',	'2019-05-21 02:48:48',	'2019-05-21 18:02:20'),
(8,	'USER 3',	'user3@faceapps.com',	'user3',	'92877af70a45fd6a2ed7fe81e1236b78',	6281001110001,	'USER 3 ADDRESS',	'default-user.png',	'user3_sample.jpg',	'0',	'2019-05-21 02:48:48',	'2019-05-21 18:02:20');

-- 2019-05-21 01:35:03
