def extract(prod_soup):
        qiymet = ""
        valyuta = ""
        result = dict()
        prices = prod_soup.find_all("div", class_="middle")
        for price in prices:
                qiymet = price.find("span", class_="price-val").text
                valyuta = price.find("span", class_="price-cur").text
        result["Valyuta"] = valyuta
        result["Qiymet"] = qiymet
        return result


