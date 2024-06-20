# -*- coding: utf-8 -*-
import jmp

jmp.run_jsl(f'''
DataTable("{title}") << {formulaString};
DataTable("{title}"):Viewers Predictor << IgnoreErrors(2);
DataTable("{title}"):Viewers Predictor << SetName("ViewersPredictFormula");
''')
