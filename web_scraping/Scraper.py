import json
import datetime

import requests
from bs4 import BeautifulSoup

import additional_info_extractor
import price_info_extractor
import contact_info_extractor
import property_extractor
import statistics_extractor
import passiv_product
import photos_extractor
import other_ads_extractor
import question_extractor
import change_time_format
import os

main_url = "https://tap.az/"
main_response = requests.get(main_url)

print(f"Main response: {main_response.status_code}")

ID = 27443149

file = open("./Data/test.jsonl", "w", encoding="utf-8")
file.write("[\n")

prod_res_status = None
property_dict = dict()


# while prod_res_status != 404:
for i in range(30):
    try:

        prod_res = requests.get(main_url + "elanlar/" + str(ID), headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"})

        prod_res_status = prod_res.status_code
        scr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current ID: {ID}")
        if prod_res_status >= 300:
            ID += 1
            continue
        prod_html = prod_res.content
        prod_soup = BeautifulSoup(prod_html, "html.parser")
        redirected_to_home = prod_soup.find("body", class_="products")
        if redirected_to_home !=None:
            ID += 1
            continue



        property_dict = property_extractor.extract(prod_soup)
        property_dict["ID"] = ID
        property_dict["scr_time"] = scr_time
        property_dict["an_time"] = change_time_format.extract(prod_soup)
        property_dict["Price"] = price_info_extractor.extract(prod_soup)

        contact_info = contact_info_extractor.extract(prod_soup)
        property_dict["Seller"] = contact_info

        additional_info = additional_info_extractor.extract(prod_soup)
        property_dict["Additional info"] = additional_info

        property_dict["Other ads of store"] = other_ads_extractor.extract(prod_soup)

        property_dict["Photos"] = photos_extractor.extract(prod_soup)

        property_dict["Baxışların sayı"] = statistics_extractor.extract(prod_soup)

        property_dict["Question"] = question_extractor.extract(prod_soup)

        property_dict["Advertisement"] = passiv_product.extract(prod_soup)


        json.dump(property_dict, file, ensure_ascii=False)
        file.write(",\n")
        ID += 1

    except:
        ID += 1

file.close()
with open('./Data/test.jsonl', 'a', encoding="utf-8") as file:
    file.write("\n]")
