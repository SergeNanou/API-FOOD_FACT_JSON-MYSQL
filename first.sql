

CREATE DATABASE Pure_beure;
USE Pure_beure;

CREATE TABLE Category (
    id SMALLINT   PRIMARY KEY,
    nom_category VARCHAR(1000) NOT NULL

)
ENGINE=InnoDB;



CREATE TABLE Produit (
    code_bar BIGINT  PRIMARY KEY,
    nom_produit VARCHAR(100) NOT NULL,
    
    description VARCHAR(1000),
    
    url VARCHAR(1000)
     
)
ENGINE=InnoDB;

CREATE TABLE Categorie_Produit (
    categorie_id SMALLINT   REFERENCES Category(id),
    produit_code_bar BIGINT  REFERENCES Produit(code_bar),
    PRIMARY KEY (categorie_id, produit_code_bar)
)
ENGINE=InnoDB;

CREATE TABLE Substitut (
    id SMALLINT  UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nom_produit VARCHAR(100) NOT NULL,
    produit_substitut VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Magasin (
    id SMALLINT   PRIMARY KEY,
    nom_magasin VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Produit_Magasin(
    magasin_id SMALLINT   REFERENCES Magasin(id),
    produit_code_bar BIGINT REFERENCES Produit(code_bar),
     PRIMARY KEY (magasin_id, produit_code_bar)
    
)
ENGINE=InnoDB;