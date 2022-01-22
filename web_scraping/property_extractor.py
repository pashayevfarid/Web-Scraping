def extract(prod_soup):
    product_properties = prod_soup.find_all("tr", class_="property")
    property_dict = dict()
    property_dict["ID"] = None
    property_dict["scr_time"] = None
    property_dict["an_time"] = None


    for properties in product_properties:
        property_name = properties.find("td", class_="property-name")
        property_value = properties.find("td", class_="property-value")

        if property_name != None and property_value != None:

            property_dict[property_name.text] = property_value.text

    return property_dict