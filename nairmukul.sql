CREATE TABLE IF NOT EXISTS Admission(
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


