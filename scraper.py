from pyquery import PyQuery as pq
import pandas as pd
import time

base_url = "https://osu.ppy.sh/rankings/osu/performance?page={page_number}#scores"
start = 1
end = 200
columns = ["rank", "name", "accuracy", "playcount", "pp", "lenSS", "lenS", "lenA"]


def r(page_number: id):
    return base_url.replace("{page_number}", str(page_number))


if __name__ == "__main__":
    a = start
    data = {
        "rank": [],
        "name": [],
        "accuracy": [],
        "playcount": [],
        "pp": [],
        "lenSS": [],
        "lenS": [],
        "lenA": []
    }
    while a <= end:
        d = pq(url=r(a))
        sample = d("table.ranking-page-table tbody tr.ranking-page-table__row")
        for i in sample.items():
            rank_unclean = i.find("td").eq(0).text()
            rank = int(rank_unclean.replace("#", ""))
            name = i.find("td").eq(1).text()
            accuracy_unclean = i.find("td").eq(2).text()
            accuracy = float(accuracy_unclean.replace("%", ""))
            playcount_unclean = i.find("td").eq(3).text()
            playcount = int(playcount_unclean.replace(",", ""))
            performance_unclean = i.find("td").eq(4).text()
            performance = int(performance_unclean.replace(",", ""))
            lenSS_unclean = i.find("td").eq(5).text()
            lenSS = int(lenSS_unclean.replace(",", ""))
            lenS_unclean = i.find("td").eq(6).text()
            lenS = int(lenS_unclean.replace(",", ""))
            lenS_unclean = i.find("td").eq(6).text()
            lenS = int(lenS_unclean.replace(",", ""))
            lenA_unclean = i.find("td").eq(7).text()
            lenA = int(lenA_unclean.replace(",", ""))
            print(a)
            print(rank, name, accuracy, playcount, performance, lenSS, lenS, lenA)
            data["rank"].append(rank)
            data["name"].append(name)
            data["accuracy"].append(accuracy)
            data["playcount"].append(playcount)
            data["pp"].append(performance)
            data["lenSS"].append(lenSS)
            data["lenS"].append(lenS)
            data["lenA"].append(lenA)
        time.sleep(1)
        a = a + 1
    dataframe = pd.DataFrame(data, columns=columns)
    export_csv = dataframe.to_csv(r'user_data.csv', index=None, header=True)
