--
-- File generated with SQLiteStudio v3.4.17 on Ср мая 21 22:24:14 2025
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Ware
CREATE TABLE IF NOT EXISTS [Ware] (
	[ID]	smallint NOT NULL,
	[Produce]	nvarchar(50) COLLATE NOCASE,
	[Material]	nvarchar(50) COLLATE NOCASE,
	[Color]	nvarchar(15) COLLATE NOCASE,
	[Size]	nvarchar(15) COLLATE NOCASE,
	[Country]	nvarchar(50) COLLATE NOCASE,
	[ID_salespeople]	smallint,
	[Price]	real,
	[Count]	smallint,
	[REM]	nvarchar(50) COLLATE NOCASE,
    PRIMARY KEY ([ID])

);
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1001, 'CKN-002', 'кожзам', 'ч', '39x30x6,4', 'Германия', 2001, 143.0, 2, 'Notebrief (13,2")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1002, 'CKN-004', 'кожзам', 'ч', '42,5x28,50x6,4', 'Беларусь', NULL, 227.0, 10, 'Primocom (15,2")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1003, 'NKN-017', 'кожзам', 'ч', '34,3x27,9x6,4', 'Польша', 2011, 356.0, 3, 'Voyager II (14,1")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1004, 'NKN-818', 'кожзам', 'ч', '35,6x28,6x5,7', 'Россия', 2016, 324.0, 22, 'Mobile Office (14,1")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1006, 'NTN-712BK', 'нейлон', 'ч', '43,2х31,8х5,1', 'Россия', 2065, 350.0, 226, 'mt Brief Plus (17,0")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1009, 'NTN-714BK', 'нейлон', 'ч', '31,8х34,9х5,1', 'Китай', 2004, 350.0, 11, 'mt Urban Pac (15,4")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1010, 'NTN-891BK', 'нейлон', 'ч', '38,1x27,9x6,4', 'Корея', 2065, 246.0, 14, 'Twill Notebrief (14,1")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1011, 'NON-913RD', 'нейлон', 'красный', '30,5x33,5x5,1', 'Россия', 2065, 324.0, 1, 'Twill Digipack (15,2")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1012, 'NON-915BK', 'нейлон', 'ч', '36,8х26,7х6,4', 'Китай', 2015, 304.0, 0, 'Meg Cosmo Brief(15,2") + косметичка');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1013, 'NON-915GY', 'нейлон', 'серый', '36,8х26,7х6,4', 'Корея', 2016, 304.0, 21, 'Meg Cosmo Brief(15,2") + косметичка');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1014, 'SLN-062BK', 'кожа', 'ч', '36,8х26,7х6,4', 'Китай', 2048, 304.0, 10, 'She Rules TM Exclusive Leather (15,4") женская');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1015, 'PON-100', 'полиэстер', 'ч', '40,6x30,5x5,7', 'Китай', 2065, 391.0, 14, 'Bantam Brief (15,2")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1016, 'PON-302BK', 'полиэстер', 'ч', '30,5x25,4x5,1', 'Польша', 2015, 117.0, 17, 'Double Compartment Computer Brief (15,2")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1017, 'PON-303BK', 'полиэстер', 'ч', '44,5х33,7х5,1', 'Германия', 2015, 110.0, 29, 'Large Expandable computer brief (17")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1018, 'PON-304BK', 'полиэстер', 'ч', '29,2х31,1х5,1', 'Беларусь', 2048, 168.0, 8, 'Computer Backpack (15,2)');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1020, 'PON-855BK', 'полиэстер', 'ч', '34,9х28,6х5,1', 'Корея', 2004, 123.0, 3, 'ImpactGuardTM Insert Sleeve (15,4")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1021, 'GLN-001', 'кожа', 'ч', '33,7x26,7x5,7', 'Корея', 2015, 123.0, 4, 'Compact Leather (13,3")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1023, 'NDN-012BK', 'нейлон', 'ч', '41,3х28,6х14', 'Корея', 2001, 298.0, 15, 'Convertible Digipack');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1024, 'NE-SC  (F8N006ea)', 'нейлон', 'ч-серый', '35,6x29,2x5,1', 'Китай', 2004, 363.0, 16, 'Notebook Slip Case');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1025, '(F8E353eaLRG)', 'полиэстер/нейлон', 'ч', '40x30x70', 'Польша', 2015, 109.0, 13, 'Providence Street Case (15)');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1026, '(F8E157eaLRG)', 'полиэстер/нейлон', 'ч', '38,1x28x70', 'Германия', 2014, 126.0, 0, 'Stone Street Case (15)');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1028, 'NE-07 (F8N004ea)', 'нейлон', 'ч', '36,8x29,2x5,1', 'Россия', 2014, 168.0, 14, 'Notebook Bag');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1030, 'NE-01 (F8N001ea)', 'нейлон', 'ч', '36,8x30,5x5,1', 'Польша', 2001, 176.0, 24, 'Notebook Case');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1031, 'NE-L01 (F8L001ea)', 'кожа', 'ч-серый', '36,8x30,5x5,1', 'Корея', 2004, 225.0, 2, 'Leather Case');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1032, '(F8E157eaXXL)', 'кожзам.', 'ч', '42x33x6,6', 'Польша', 2001, 246.0, 14, 'Stone Street Case (17)');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1036, 'CN01', 'полиэстер', 'ч', '39x30x5', 'Германия', 2011, 435.0, 32, 'Computer Case (15/15,4")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1038, 'TAR300', 'полиэстер', 'ч', '38,5x30x4,5', 'Корея', 2065, 260.0, 24, 'Computer Case (15/15,4")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1041, 'TAR400', 'полиэстер', 'ч', '38,5x30x4,5', 'Китай', 2016, 145.0, 144, 'Computer Case (15/15,4")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1043, 'KCB-01', 'нейлон', 'ч', '40x30x7', 'Польша', 2065, 133.0, 12, 'Notepack Deluxe (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1045, 'KCB-02', 'нейлон', 'ч', '40x30x7', 'Китай', 2001, 154.0, 22, 'Notepack Deluxe (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1047, 'KCB-02L', 'кожа', 'ч', '40x30x7', 'Китай', 2048, 112.0, 1, 'Notepack Deluxe (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1048, 'KCB-03', 'нейлон', 'ч', '40x30x8,5', 'Беларусь', 2001, 197.0, 35, 'System Case (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1049, 'KCB-03BKP', 'кожзам.', 'ч', '40x30x8,5', 'Германия', 2001, 325.0, 14, 'System Case (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1052, 'KCB-03L', 'кожа', 'ч', '40x30x8,5', 'Польша', NULL, 204.0, 21, 'System Case (15")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1055, 'KCB-05BKP', 'кожзам.', 'ч', '35,5x28x6', 'Польша', 2016, 189.0, 4, 'Traditional Case (16")');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1064, 'HB-1110', 'кожа', 'ч', '41x30x6', 'Россия', 2015, 401.0, 2, 'Briefcase deluxe large/17''''');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1078, 'AU1', 'нейлон', 'ч', '41x29x6', 'Китай', 2016, 310.0, 1, 'Nylon Computer Case (15'''')');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1105, 'AU2', 'нейлон', 'ч', '40x28x5,5', 'Россия', 2011, 1050.0, 14, 'Nylon Computer Case (15'''')');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1205, 'AU4', 'нейлон', 'ч', '37x27x4', 'Беларусь', 2065, 110.0, 2, 'Nylon Computer Case (15'''')');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1235, 'AH02', 'нейлон', 'ч', '39x29x5', 'Польша', 2014, 136.0, 5, 'Nylon Computer Case (15'''')');
INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM) VALUES (1254, 'CC06', 'нейлон', 'ч', '38x29x7', 'Германия', 2011, 110.0, 6, 'Nylon Computer Case (15'''')');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
