import pandas as pd
import requests
jsondata=requests.get("https://jsonplaceholder.typicode.com/posts")
data=jsondata.json()
df=pd.DataFrame(data)
filter_userid3=df[df["userId"] == 3]
filter_userid3.to_csv("modul_06_json-apis/user_3_posts.csv", index=False)
