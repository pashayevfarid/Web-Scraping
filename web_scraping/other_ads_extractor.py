def extract(prod_soup):
    other_ads = []
    ads = prod_soup.find("div", class_="shop-contact-i shop-contact--all-ads")
    if ads != None:
        link = ads.find("a")
        if link != None:
            other_ads.append(link["href"])
    else:
        other_ads.append("Null")

    return other_ads
