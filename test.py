# url = "https://www.securitylab.ru/news/520908.php"
#
# article_id = url.split("/")[-1]
# article_id = article_id[:-4]
# print(article_id)
import json

with open("news_list.json") as file:
    news_dict = json.load(file)

search_id = "520908123"

if search_id in news_dict:
    print("article is already in the feed, repeat the iteration")
else:
    print("something new, adding to the list")