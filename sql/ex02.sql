CREATE TABLE person(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);

CREATE TABLE pet(
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);

CREATE TABLE person_pet(
    person_id INTEGER,
    pet_id INTEGER
);


-- ### EXTRA CREDIT QUESTIONS ###
-- Create a table with pet id included
--    NB: sqlite3 has no boolean type, integer instead (0=FALSE, 1=TRUE)
CREATE TABLE person2(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    pet_id INTEGER
);

-- Populate tables
INSERT INTo person2 (id, first_name, last_name, age, pet_id) VALUES (6, 'Six', 'Dude6', 30, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Woof1', 'Cujo', 3, 0);
-- Retrieve data by selecting from both tables
SELECT pet.id, pet.name FROM pet, person2 WHERE pet.id == person2.pet_id;


-- populate pet table and create a cat lady
INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'One', 'CatLady', 20);
INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Meow2', 'Cheshire', 2, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Meow3', 'Cheshire', 4, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Meow4', 'Cheshire', 3, 1);
INSERT INTO person_pet (person_id, pet_id) VALUES (1, 2);
INSERT INTO person_pet (person_id, pet_id) VALUES (1, 3);
INSERT INTO person_pet (person_id, pet_id) VALUES (1, 4);
SELECT * FROM person_pet;


-- cars
CREATE TABLE cars(
    id INTEGER PRIMARY KEY,
    model TEXT,
    year INTGER,
    running INTEGER 
);

CREATE TABLE cars_people(
    person_id,
    car_id
);

INSERT INTO cars (id, model, year, running) VALUES (1, 'Chrysler', 1963, 1);
INSERT INTO cars_people (person_id, car_id) VALUES (1,1);
SELECT * FROM cars_people;
