# -*- coding: utf-8 -*-
import os, sys, jmp
from sqlalchemy import create_engine

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

engine = create_engine(f"sqlite:///{os.path.join(gdd, 'data.db')}")

to_pandas(dt).to_sql("big_class", engine, index = False, if_exists = "replace")
