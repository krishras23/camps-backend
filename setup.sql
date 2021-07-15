CREATE TABLE child_information (
	student_id int,
	name VARCHAR(220),
	allergies VARCHAR(220),
	DOB DATE
);



CREATE TABLE types_of_camps (
	camp_id int,
	name VARCHAR(10),
	description VARCHAR(220),
	price double,
	age_range VARCHAR(15)
);


INSERT INTO SummerCamps.types_of_camps (camp_id, name, description, price, age_range) values (1, "Explorers", "Explore every destination we have to offer", 90.44, "hi");
INSERT INTO SummerCamps.types_of_camps (camp_id, name, description, price, age_range) values (2, "Mini Camp", "Have fun with friends and play games", 130.44, "8-12");

INSERT INTO SummerCamps.types_of_camps (camp_id, name, description, price, age_range)
		values(3, "Adventure", "Adventure into the world around you", 200, "5-8");



insert into SummerCamps.child_information (student_id, name, allergies, age) values (35, "Rastanvi", "Chinese Food", 10)


insert into child_information (student_id, name, allergies, age) values (35, "Anvi", "Medicine", 10)

delete from SummerCamps.child_information where name = "Rastanvi"