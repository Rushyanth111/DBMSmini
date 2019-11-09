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
                Weight Float,
                DateOfArrival Text,
                DoctorName Text,
                OfficerSignature Text,
                Signature Text,
                Address Text);

CREATE TABLE IF NOT EXISTS PTM(
                SNo Integer PRIMARY KEY,
                Name RangedValue,
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
                Weight Float);

CREATE TABLE IF NOT EXISTS DailyFood(
                SNo Integer PRIMARY KEY,
                Name Text,
                Wheat Float,
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
                DOB Date,
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
    ID Text,
    Aadhar_Number Integer UNIQUE,
    Name Text NOT NULL,
    Date_of_Birth Date,
    Mother_Name Text NOT NULL,
    Mother_ID Text NOT NULL UNIQUE,
    Father_Name Text,
    Father_ID Text NOT NULL UNIQUE,
    Address Text,
    PRIMARY KEY(ID)
);


CREATE TABLE IF NOT EXISTS VACCINATION(
    Child_Name Text,
    Gender Text,
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
    Child_Name Text,
    Father_Name Text,
    Mother_Name Text,
    DOB DATE,
    Weight Text
    );

CREATE TABLE IF NOT EXISTS PREGNANT_LADIES(
    Sl_No Integer,
    Survey_No Integer,
    Name Text,
    Pregnancy_status Text,
    Date_ DATE,
    Signature Text
    );
"""


def SQLinit(db: QSqlDatabase):
    for x in Query.split(";"):
        db.exec_(x)
