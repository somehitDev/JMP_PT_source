# -*- coding: utf-8 -*-
import pathlib, sqlite3, pandas as pd

root_dir = pathlib.Path(gdd).resolve()
conn = sqlite3.connect(str(root_dir.joinpath("test.db")))

df_join = pd.read_sql(queryString, conn)

conn.close()
