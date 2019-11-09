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
