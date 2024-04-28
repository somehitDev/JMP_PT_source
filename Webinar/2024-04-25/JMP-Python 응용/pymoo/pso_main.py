# -*- coding: utf-8 -*-
import numpy as np, jmp
from datetime import datetime
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.soo.nonconvex.pso import PSO
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.termination import get_termination
from pymoo.optimize import minimize



# setup problem
class JMP_Problem(ElementwiseProblem):
    def __init__(self):
        bounds = [
            np.array([ -2.05, -2.05 ]),
            np.array([ 2.05, 2.05 ])
        ]

        super().__init__(
            n_var = 2, n_obj = 1, n_constr = 0,
            xl = bounds[0], xu = bounds[1]
        )

    def _evaluate(self, x:np.ndarray, out:dict, *args, **kwargs):
        dtModel["X1"][0] = x[0]
        dtModel["X2"][0] = x[1]

        jmp.run_jsl("dtModel << RerunFormulas;")
         
        out["F"] = [
            dtModel["Y"][0]
        ]
        
        jmp.run_jsl("dtResult << Add Rows(1);")
        
        dtResult["Iter"][dtResult.nrows - 1] = dtResult.nrows
        dtResult["X1"][dtResult.nrows - 1] = x[0]
        dtResult["X2"][dtResult.nrows - 1] = x[1]
        dtResult["Y"][dtResult.nrows - 1] = dtModel["Y"][0]

if __name__ == "__main__":
    # get start time
    start_time = datetime.now()

    # pymoo
    algorithm = PSO(
        pop_size = 40,
        n_offsprings = 10,
        sampling = FloatRandomSampling(),
        crossover = SBX(prob_var = 0.9, eta = 15),
        mutation = PM(eta = 20),
        eliminate_duplicates = True
    )
    problem = JMP_Problem()
    termination = get_termination("n_gen", 100)

    # clear output file
    jmp.run_jsl("""
dtOut << Select All Rows << Delete Rows;
dtModel << BringWindowToFront;
dtOut << BringWindowToFront;
""")

    # run pymoo
    result = minimize(
        problem, algorithm, termination,
        seed = 1, save_history = False, verbose = True
    )

    print(f"""Best solution found: 
X = {result.X}
F = {result.F}

elapsed: {datetime.now() - start_time}
""")
