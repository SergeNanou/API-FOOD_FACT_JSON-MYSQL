

CREATE DATABASE Pure_beure;
USE Pure_beure;

CREATE TABLE Category (
    id id SMALLINT  UNSIGNED NOT NULL AUTO_INCREMENT  PRIMARY KEY,
    name_category VARCHAR(255) NOT NULL

)
ENGINE=InnoDB;



CREATE TABLE Product (
    code_bar BIGINT  PRIMARY KEY,
    name_product VARCHAR(100) NOT NULL,
    
    description TEXT,
    
    url TEXT,
    nutrition_score CHAR(10)
     
)
ENGINE=InnoDB;

CREATE TABLE Category_Product (
    categorie_id SMALLINT   REFERENCES Category(id),
    product_code_bar BIGINT  REFERENCES Product(code_bar),
    PRIMARY KEY (categorie_id, product_code_bar)
)
ENGINE=InnoDB;

CREATE TABLE Substitut (
    id SMALLINT  UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name_produit VARCHAR(100) NOT NULL,
    composition TEXT NOT NULL, 
    url TEXT NOT NULL, 
    name_shop VARCHAR(100) NOT NUL
    product_substitut VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Shop (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_shop VARCHAR(100) NOT NULL
    
)
ENGINE=InnoDB;

CREATE TABLE Product_shop(
    shop_id SMALLINT   REFERENCES Shop(id),
    product_code_bar BIGINT REFERENCES Product(code_bar),
     PRIMARY KEY (shop_id, product_code_bar)
    
)
ENGINE=InnoDB;