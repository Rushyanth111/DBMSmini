PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS person(
    person_id Integer,
    name Text,
    dob Date,
    caste Text,
    Primary Key(person_id)
);

CREATE TABLE IF NOT EXISTS family(
    family_id Integer,
    father_id Integer,
    mother_id Integer,
    Primary Key(family_id),
    Foreign key(father_id) references person(person_id),
    Foreign key(mother_id) references person(person_id)
);

CREATE TABLE IF NOT EXISTS survey(
    family_id Integer,
    survey_id Integer,
    address Text,
    Foreign Key(family_id) references family(family_id)
);

CREATE TABLE IF NOT EXISTS student(
    person_id Integer,
    RegDate Date,
    Foreign key(person_id) references person(person_id)
);

CREATE TABLE IF NOT EXISTS hospital(
    hospital_id integer,
    name text, 
    address text,
    Primary key(hospital_id)
);

CREATE TABLE IF NOT EXISTS doctor(
    doctor_id Integer,
    name text,
    hospital_id Integer,
    primary key(doctor_id),
    foreign key(hospital_id) references hospital(hospital_id)
);

CREATE TABLE IF NOT EXISTS person_birth(
    person_id Integer,
    doctor_id Integer,
    family_id Integer,
    place text,
    method text,
    weight text,
    primary key(person_id,doctor_id,family_id),
    foreign key(person_id) references person(person_id),
    foreign key(doctor_id) references doctor(doctor_id),
    foreign key(family_id) references family(family_id)
);

CREATE TABLE IF NOT EXISTS vaccination(
    person_id Integer,
    Date date,
    Vaccno varchar(12),
    doctor_id Integer,
    foreign key(person_id) references person(person_id),
    foreign key(doctor_id) references doctor(doctor_id)
);


CREATE TRIGGER validate_vaccno
    BEFORE INSERT ON vaccination
BEGIN
    SELECT
        CASE WHEN NEW.vaccno not like '__/__/______' THEN
            RAISE(ABORT, 'INVALID VACC ID')
        END;
END;

CREATE VIEW IF NOT EXISTS view_person_full_details
AS 
    select p.*, pb.* 
    from person p, person_birth pb
    where p.person_id = pb.person_id;

