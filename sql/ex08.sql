-- added in ex2
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

-- added in ex3
-- SQL: TRUE == 1, FALSE == 0
INSERT INTO person (id, first_name, last_name, age) VALUES (0, 'Zed', 'Shaw', 37);
INSERT INTO pet (id, name, breed, age, dead) VALUES (0, 'Fluffy', 'Unicorn', 1000, 0);
INSERT INTO pet VALUES (1, 'Gigantor', 'Great Big Robot', 1, 1);


-- added in ex4
INSERT INTO person_pet (person_id, pet_id) VALUES (0,0);
INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'Mr.', 'Wizard', 40);
INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Fang', 'Chihuahua', 4, 0);
INSERT INTO person_pet VALUES (0,1);
INSERT INTO person_pet (person_id, pet_id) VALUES (1,2);


-- added in ex5
-- SELECT * FROM person;
-- SELECT name, age FROM pet;
-- SELECT name, age FROM pet WHERE dead = 0;
-- SELECT * FROM person WHERE first_name != 'Zed';

-- ex8 main section
-- DELETE FROM pet WHERE id IN (
--    SELECT pet.id
--    FROM pet, person_pet, person
--    WHERE
--    person.id = person_pet.person_id AND
--    pet.id = person_pet.pet_id AND
--    person.first_name = 'Zed'
-- );

-- SELECT * FROM pet;
-- SELECT * FROM person_pet;

-- DELETE FROM person_pet
--    WHERE pet_id NOT IN (
--        SELECT id FROM pet
--    );

-- SELECT * FROM person_pet;


-- ### EXTRA CREDIT QUESTIONS ###
--Delete dead pets owned by me
INSERT INTO person (id, first_name, last_name, age) VALUES (2, 'Me', 'Myself', 25);
INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Tres', 'Shepard', 4, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Quatro', 'Wolf', 7, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (5, 'Cinco', 'Shih-Tzu', 2, 0);
INSERT INTO pet (id, name, breed, age, dead) VALUES (6, 'Seis', 'Shih-Tzu', 4, 0);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,3);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,4);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,5);
INSERT INTO person_pet (person_id, pet_id) VALUES (2,6);


-- SQLITE3 printer directive
.print ''
.print 'Validate EX Credit 1'
SELECT pet.id, pet.name, pet.dead FROM pet, person_pet 
      WHERE person_pet.person_id = 2 
        AND pet.id = person_pet.pet_id;
    
DELETE FROM pet WHERE pet.id IN (
    SELECT person_pet.pet_id FROM person_pet
        WHERE person_pet.person_id = 2
    )
    AND pet.dead = 1;

.print ''

SELECT pet.id, pet.name, pet.dead FROM pet, person_pet 
      WHERE person_pet.person_id = 2 
        AND pet.id = person_pet.pet_id;



--Delete people instead of pets
--  NB: This is really a bad idea because a person could have two pets
--  one dead and one alive but the person would still be deleted
INSERT INTO person (id, first_name, last_name, age) VALUES (3, 'Him', 'Them', 33);
INSERT INTO person (id, first_name, last_name, age) VALUES (4, 'Her', 'Them', 33);
INSERT INTO pet (id, name, breed, age, dead) VALUES (7, 'Siete', 'Mutt', 2, 1);
INSERT INTO pet (id, name, breed, age, dead) VALUES (8, 'Ocho', 'Mutt', 4, 0);
INSERT INTO person_pet (person_id, pet_id) VALUES (3,7);
INSERT INTO person_pet (person_id, pet_id) VALUES (4,8);

.print '' 
.print ''
.print 'Validate EX Credit 2'
SELECT person.id, person.first_name, pet.name, pet.dead FROM person, pet, person_pet
    WHERE pet.id = person_pet.pet_id
      AND person.id = person_pet.person_id;

.print ''
.print 'Owners who will be deleted'
SELECT person_pet.person_id, pet.name FROM person_pet, pet
    WHERE pet.dead = 1
      AND person_pet.pet_id = pet.id;

DELETE FROM person WHERE person.id IN (
    SELECT person_pet.person_id FROM person_pet, pet
        WHERE pet.dead = 1
          AND person_pet.pet_id = pet.id
    );

.print ''
.print 'After Delete'
SELECT person.id, person.first_name, pet.name, pet.dead FROM person, pet, person_pet
    WHERE pet.id = person_pet.pet_id
      AND person.id = person_pet.person_id;

--EOF
