drop table City cascade;
drop table Judge cascade;
drop table Team cascade;
drop table Game cascade;
drop table Users cascade;

CREATE TABLE IF NOT EXISTS City(
  id INT NOT NULL,
  name VARCHAR(45) NULL,
  population VARCHAR(45) NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Judge (
  id INT NOT NULL,
  city_id INT NULL,
  fio VARCHAR(45) NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_Judge_City
    FOREIGN KEY (city_id)
    REFERENCES City (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Team (
  id INT NOT NULL,
  city_id INT NULL,
  name VARCHAR(45) NULL,
  line_up VARCHAR(45) NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_Team_City1
    FOREIGN KEY (city_id)
    REFERENCES City (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Users (
    id int not null,
    login varchar(45) not null,
    password varchar(45) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Game (
  id INT NOT NULL,
  team_owner_id INT NULL,
  team_guest_id INT NULL,
  city_id INT NULL,
  judge_id INT NULL,
  time VARCHAR(45) NULL,
  date VARCHAR(45) NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_Game_Team1
    FOREIGN KEY (team_owner_id)
    REFERENCES Team (id),
  CONSTRAINT fk_Game_Team2
    FOREIGN KEY (team_guest_id)
    REFERENCES Team (id),
  CONSTRAINT fk_Game_City1
    FOREIGN KEY (city_id)
    REFERENCES City (id),
  CONSTRAINT fk_Game_Judge1
    FOREIGN KEY (judge_id)
    REFERENCES Judge (id)
);

