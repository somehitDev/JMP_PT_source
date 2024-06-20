import os, jmp, pandas as pd

def to_dt(df:pd.DataFrame, dt_name:str = "DataTable") -> jmp.DataTable:
    csv_file = os.path.join(os.path.join(jmp.TEMP, dt_name + ".csv"))
    df.to_csv(csv_file, index = False, encoding = "utf-8")

    jmp.run_jsl(f'''
dt = Open("{csv_file}"); Wait(0);
dt << SetWindowTitle("{dt_name}");
DeleteFile("{csv_file}");
''')

    return jmp.table(dt_name)
