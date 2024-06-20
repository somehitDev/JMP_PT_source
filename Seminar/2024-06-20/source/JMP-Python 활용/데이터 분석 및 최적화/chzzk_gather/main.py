# -*- coding: utf-8 -*-
"""
JMP Seminar자료용 Chzzk Stream Data
"""
import sqlite3, requests, json, pandas as pd, traceback
from datetime import datetime, timedelta

conn = sqlite3.connect("streams.db", check_same_thread = False)


def get_lives(keyword:str, search_time:datetime = None) -> list[dict[str, str]]:
    print(f"`{keyword}` started")

    if search_time is None:
        search_time = datetime.now()

    lives, offset = [], None
    while True:
        try:
            if offset is None:
                resp:dict = requests.get("https://api.chzzk.naver.com/service/v1/search/lives", params = { "keyword": keyword }, headers = { "user-agent": "Chrome/123.0.0.0" }).json()["content"]
            else:
                resp:dict = requests.get("https://api.chzzk.naver.com/service/v1/search/lives", params = { "keyword": keyword, "offset": offset }, headers = { "user-agent": "Chrome/123.0.0.0" }).json()["content"]

            if resp["size"] == 0:
                break

            lives.extend([
                {
                    "SearchTime": search_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "StreamTime": int((search_time - datetime.strptime(live["live"]["openDate"], "%Y-%m-%d %H:%M:%S")).total_seconds()),
                    "LiveID": live["live"]["liveId"],
                    "LiveTitle": live["live"]["liveTitle"],
                    "LiveCategory": live["live"]["liveCategoryValue"],
                    "ChannelID": live["channel"]["channelId"],
                    "Viewers": live["live"]["concurrentUserCount"]
                }
                for live in resp["data"]
                if json.loads(live["live"]["livePlaybackJson"])["live"]["status"] == "STARTED"
            ])

            offset = resp["page"]["next"]["offset"]
            print(f"searched: {offset}")
        except:
            print(traceback.format_exc())
            break

    print(f"`{keyword}` finished")

    return sorted(lives, key = lambda live: live["Viewers"])

def get_lives_all(keywords:list[str]):
    search_time = datetime.now()

    all_lives = []
    for keyword in keywords:
        all_lives.extend(get_lives(keyword, search_time))

    return sorted(all_lives, key = lambda live: live["Viewers"])


def update(conn:sqlite3.Connection):
    lives = get_lives_all([ "버튜버", "버츄얼" ])
    df_lives = pd.DataFrame.from_dict(lives).drop_duplicates()
    df_lives.to_sql("streams", conn, index = False, if_exists = "append")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action = "store_true")
    args = parser.parse_args()

    if args.test:
        lives = get_lives_all([ "버튜버", "버츄얼" ])
        print(lives[0])
    else:
        import schedule

        schedule.every().minute.do(update, conn)
        while True:
            try:
                cur_time = datetime.now()
                if cur_time >= datetime(2024, 6, 1, 0, 0, 0):
                    break
                
                if cur_time >= datetime(2024, 5, 18, 0, 0, 0):
                    schedule.run_pending()
            except KeyboardInterrupt:
                break

    conn.close()
