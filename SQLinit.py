from PyQt5.QtSql import QSqlDatabase

Query = """CREATE TABLE IF NOT EXISTS Admission(
                No  Integer PRIMARY KEY,
                SurveyNo Integer,
                Name Text,
                FatherName Text,
                MotherName Text,
                DOB Text,
                Caste Text,
                RegisterDate Text,
                Weight float,
                DateOfArrival Text,
                DoctorName Text,
                OfficerSignature Text,
                Signature Text,
                Address Text);

CREATE TABLE IF NOT EXISTS PTM(
                SNo Integer PRIMARY KEY,
                Name Text,
                GuardianName Text,
                Discussion Text);

CREATE TABLE IF NOT EXISTS BirthRegister(
                SNo Integer,
                Name Text,
                FatherName Text,
                NoOfSiblings Integer,
                DeliveryDate Text,
                PlaceOfBirth Text,
                MethodOfBirth Text,
                Weight float);

CREATE TABLE IF NOT EXISTS DailyFood(
                SNo Integer PRIMARY KEY,
                Name Text,
                Wheat FLOAT,
                Sugar Integer,
                Jaggery Integer,
                Milk Integer,
                Nutrient_Mix Integer,
                Pulses Integer,
                Height Integer,
                Weight Integer,
                Signature Text);

CREATE TABLE IF NOT EXISTS Family(
                SNo Integer PRIMARY KEY,
                Survey_ID Integer,
                Name Text,
                Relation Text,
                Gender Text,
                Marriage Text,
                DOB DATE,
                Age Integer,
                Mothers_name Text,
                PhysicalDisabilities Text,
                ResidenceOfAnganwadi Text,

                NativeOfMarsandra Text,
                DateOfArrival Date,
                DateOfDeath Date,
                Lunch Text,
                Signature Text);

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
CREATE TABLE IF NOT EXISTS FA1(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);


CREATE TABLE IF NOT EXISTS FA2(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);

CREATE TABLE IF NOT EXISTS SA1(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);

CREATE TABLE IF NOT EXISTS FA3(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);

CREATE TABLE IF NOT EXISTS FA4(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);



CREATE TABLE IF NOT EXISTS SA2(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Integer,
                Kannada Integer,
                Mathematics Integer,
                Science Integer,
                Social_Science Integer
                EVS Text);

CREATE TABLE IF NOT EXISTS Attendance(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Class Integer,
                English Text,
                Kannada Text,
                Mathematics Text,
                Science Text,
                Social_Science Text
                EVS Text);

CREATE TABLE IF NOT EXISTS MidDay(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Quantity Integer);

CREATE TABLE IF NOT EXISTS Stationary(
                Adm_No  Integer PRIMARY KEY,
                Name Text,
                Books Text
                Uniform Text
                Stationary Text
                Remarks Text);
"""


def SQLinit(db: QSqlDatabase):
    for x in Query.split(";"):
        db.exec_(x)
