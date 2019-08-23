#! /usr/bin/python3
# -*- coding: Utf-8 -*-

import unittest

import requests
import regex as re


def search(search_term,pge_size):

	
    payload = {"search_terms": search_term,"search_tag": 
               "categories","page_size": pge_size, "json": 1}
    res = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", 
                            params=payload)
	# result of json request 
    results = res.json()
    products = results["products"][0]['product_name_fr']
    return(products)


m_success = search("Biscuits",1)

def test_with_request_get_mock_success(monkeypatch):
    product = 'PRINCE Gout CHOCOLAT au Ble Complet'
    class MockResponse:
        def json(self):
            return({"products":[{"product_name_fr":'PRINCE Gout CHOCOLAT au Ble Complet'}]})

    def mock_requests_get_sucess_1(url,  params):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_requests_get_sucess_1)
    assert search("Biscuits",1) == product
