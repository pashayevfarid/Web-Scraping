def extract(prod_soup):
    phones = []
    seller_name = ""
    res = dict()
    try:
        contacts = prod_soup.find_all("a", class_="phone")

        for contact in contacts:
            phones.append(contact.text)
        seller_name = prod_soup.find("div", class_="name").text

        res["Seller name"] = seller_name
        res["Phones"] = phones
        return res

    except:
        try:
            contacts = prod_soup.find_all('a', class_="shop-phones--number")

            for contact in contacts:
                phones.append(contact.text)
            seller_name = prod_soup.find("a", class_="shop-contact--shop-name").text

            res["Seller name"] = seller_name
            res["Phones"] = phones
            return res
        except:
            return res

