import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
def extract(prod_soup):
    time = []
    months = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
    container = prod_soup.find("div", class_="lot-info")

    if container != None:
        texts = container.find_all("p")
        st = texts[-1].text

        date_str_0 = st.split(": ")[-1]
        date_str = date_str_0.split(": ")[-1].split(", ")

        if date_str[0] == "Bugün":
            ad_date = datetime.today().strftime('%Y-%m-%d')
            ad_hour = date_str[-1]
            timeobj = ad_date + " " + ad_hour + ":00"
            time.append(timeobj)
        elif date_str[0] =="Dünən":
            ad_date = (datetime.date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
            ad_hour = date_str[-1]
            timeobj = ad_date + " " + ad_hour + ":00"
            time.append(timeobj)
        else:
            s = date_str_0.split(" ")
            Month = months.index(s[1]) + 1
            timeobj = str(s[-1]) + "-" + str(Month) + "-" + str(s[0] + " 11:00:00")
            time.append(timeobj)
        return time
