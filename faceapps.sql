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
(15,	16,	'2019-05-30T223421image-b3eb4f44-4da7-4342-b01f-09b613220886.jpg',	67,	'-7.78708449',	'113.18568524',	'2019-05-30 22:35:01',	'2019-05-30 22:35:01'),
(16,	17,	'2019-05-30T223628image-c41d8abe-e4e6-4530-8c8f-c5f3136aa5e6.jpg',	63,	'-7.74974184895481',	'113.215298477321',	'2019-05-30 22:36:57',	'2019-05-30 22:36:57'),
(17,	17,	'2019-05-30T224044image-2a8ff37c-65a9-4e1e-bea6-73f0869653cd.jpg',	74,	'-7.74998684561922',	'113.21517568594',	'2019-05-30 22:41:22',	'2019-05-31 07:39:16'),
(18,	16,	'2019-05-30T225142image-43634a2d-a73b-40db-972a-d498b795e5c6.jpg',	64,	'-7.78709026',	'113.18581462',	'2019-05-30 22:52:01',	'2019-05-30 22:52:01');

DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `level` int(5) NOT NULL COMMENT '1 = admin, 0 = user',
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `code` varchar(10) NOT NULL COMMENT 'code forget password',
  `email` varchar(255) NOT NULL,
  `photo` text NOT NULL,
  `telepon` text NOT NULL,
  `alamat` text NOT NULL,
  `status` int(5) NOT NULL COMMENT '1 = ONLINE, 0 = OFFLINE',
  `lat` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `lng` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `url` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `t_admin` (`id`, `level`, `name`, `password`, `code`, `email`, `photo`, `telepon`, `alamat`, `status`, `lat`, `lng`, `created_at`, `updated_at`, `url`) VALUES
(6,	0,	'Admin',	'c14bcebc5b4cd0c7fce90c3806188619',	'zbTJ',	'fadil@canisnfelis.com',	'20190531124447dani.jpg',	'123123123123',	'jl.kh.abdul hamid',	2,	'-7.7730737',	'113.173935',	'0000-00-00 00:00:00',	'0000-00-00 00:00:00',	''),
(7,	0,	'padilatur',	'c14bcebc5b4cd0c7fce90c3806188619',	'u5r7',	'fadil@gmail.com',	'20190531123902small.jpg',	'123123123',	'jasjdasd',	2,	NULL,	NULL,	'0000-00-00 00:00:00',	'0000-00-00 00:00:00',	'');

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
(16,	'DNS PROGRESS',	'dnsprogress@gmail.com',	'dnsprogress',	'c14bcebc5b4cd0c7fce90c3806188619',	89643385968,	'Jalan Nangka Probolinggo',	'2019-05-30T220529image-d64ef201-794e-4f58-86b7-2300603719ef.jpg',	'2019-05-30T220529image-d64ef201-794e-4f58-86b7-2300603719ef.jpg',	'1',	'2019-05-30 22:09:30',	'2019-05-30 23:20:46'),
(17,	'Fadil',	'fadhilatur7@gmail.com',	'fadil',	'c14bcebc5b4cd0c7fce90c3806188619',	123456,	'hjjj',	'2019-05-30T222121image-118f23df-8cbe-4793-be42-a9e702e4ac50.jpg',	'2019-05-30T222121image-118f23df-8cbe-4793-be42-a9e702e4ac50.jpg',	'1',	'2019-05-30 22:21:41',	'2019-05-31 07:40:03');

-- 2019-06-16 10:14:37
