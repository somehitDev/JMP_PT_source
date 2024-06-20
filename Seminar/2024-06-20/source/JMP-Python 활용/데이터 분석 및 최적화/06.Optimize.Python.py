# -*- coding: utf-8 -*-
import os, sys, jmp, joblib, numpy as np, pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.termination import get_termination
from pymoo.optimize import minimize

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

category_codes = to_pandas(dtCategoryMatch).sort_values(by = [ "CategoryCode" ])["CategoryCode"].unique()
model:GradientBoostingRegressor = joblib.load(os.path.join(gdd, "models", f"{channelId}.model"))
# history_datas = []

# setup problem
class OptProblem(ElementwiseProblem):
    def __init__(self):
        super().__init__(
            n_var = 2, n_obj = 1, n_constr = 0,
            xl = np.array([ 0, category_codes[0] ]),
            xu = np.array([ 6 * 60 * 60, category_codes[-1] ])
        )

    def _evaluate(self, x:np.ndarray, out:dict, *args, **kwargs):
        stream_time = round(x[0])
        category_code = round(x[1])

        if category_code > category_codes[-1]:
            category_code = category_codes[-1]

        out["F"] = [
            model.predict([[ stream_time, category_code ]])[0] * -1
        ]

        # history_datas.append({
        #     "Step": len(history_datas) + 1,
        #     "StreamTime": stream_time,
        #     "CategoryCode": category_code,
        #     "Viewers": out["F"][0] * -1
        # })


# pymoo
algorithm = PSO(
    pop_size = 10,
    n_offsprings = 10,
    sampling = FloatRandomSampling(),
    crossover = SBX(prob_var = 0.9, eta = 15),
    mutation = PM(eta = 20),
    eliminate_duplicates = True
)
problem = OptProblem()
termination = get_termination("n_gen", 100)

# run pymoo
result = minimize(
    problem, algorithm, termination,
    seed = 1, save_history = False, verbose = False
)

dtOptimize["StreamTime"][-1] = round(result.X[0])
dtOptimize["CategoryCode"][-1] = round(result.X[1])
dtOptimize["Viewers"][-1] = round(result.F[0] * -1)

# df_history = pd.DataFrame.from_dict(history_datas)
