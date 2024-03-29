import pandas as pd
import sqlite3


df = pd.read_csv("GlobalYouTubeStatistics.csv", low_memory=False)


conn = sqlite3.connect("youtube.db")


df.to_sql('youtube', conn, if_exists='append', index=False)


conn.commit()
conn.close()
