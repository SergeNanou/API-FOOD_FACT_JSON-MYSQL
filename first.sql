

CREATE DATABASE Pure_beure;
USE Pure_beure;

CREATE TABLE Category (
    id SMALLINT   PRIMARY KEY,
    name_category VARCHAR(1000) NOT NULL

)
ENGINE=InnoDB;



CREATE TABLE Product (
    code_bar BIGINT  PRIMARY KEY,
    name_product VARCHAR(100) NOT NULL,
    
    description VARCHAR(1000),
    
    url VARCHAR(1000),
    nutrition_score VARCHAR(1)
     
)
ENGINE=InnoDB;

CREATE TABLE Categorie_Product (
    categorie_id SMALLINT   REFERENCES Category(id),
    product_code_bar BIGINT  REFERENCES Product(code_bar),
    PRIMARY KEY (categorie_id, product_code_bar)
)
ENGINE=InnoDB;

CREATE TABLE Substitut (
    id SMALLINT  UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name_produit VARCHAR(100) NOT NULL,
    product_substitut VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Shop (
    id SMALLINT   PRIMARY KEY,
    name_shop VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Product_shop(
    shop_id SMALLINT   REFERENCES Shop(id),
    product_code_bar BIGINT REFERENCES Product(code_bar),
     PRIMARY KEY (shop_id, product_code_bar)
    
)
ENGINE=InnoDB;