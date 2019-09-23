CREATE TABLE IF NOT EXISTS CHILD(
    ID TEXT,
    Aadhar_Number INT UNIQUE, 
    Name TEXT NOT NULL,
    Date_of_Birth Date,
    Mother_Name TEXT NOT NULL, 
    Mother_ID TEXT NOT NULL UNIQUE, 
    Father_Name TEXT, 
    Father_ID TEXT NOT NULL UNIQUE, 
    Address TEXT, 
    PRIMARY KEY(ID) 
);


CREATE TABLE IF NOT EXISTS VACCINATION(
    Child_Name TEXT,
    Gender TEXT,
    DOB DATE,
    Registration_Date DATE,
    Polio DATE,
    hepatitis_0 DATE,
    BCG DATE,
    DPT_1 DATE,
    Hepatitis_1 DATE,
    OPV DATE,
    DPT_2 DATE,
    Hepatitis_2 DATE,
    OPV_2 DATE,
    DPT_3 DATE,
    Hepatitis_3 DATE,
    OPV_3 DATE,
    MMR_1 DATE,
    life_dose_1 DATE,
    DPT_Booster DATE,
    MMR_2 DATE,
    Survived_first_Birth DATE
    );


CREATE TABLE IF NOT EXISTS CHILD_HEALTH(
    No INTEGER,
    Child_Name TEXT,
    Father_Name TEXT,
    Mother_Name TEXT,
    DOB DATE,
    Weight TEXT
    );

CREATE TABLE IF NOT EXISTS PREGNANT_LADIES(
    Sl_No INT,
    Survey_No INT,
    Name TEXT,
    Pregnancy_status TEXT,
    Date_ DATE,
    Signature TEXT
    );



