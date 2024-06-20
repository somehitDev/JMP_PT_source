# File: dt2pandas.py
# Author: Paul Nelson
#
# Description:  Script to mimic JMP 17 behavior in JMP 18 with regard to use of pandas.
#
# Usage: Script below shows usage of taking a data table as dt, and making it a
#        pandas dataframe using JMP 14-17's behavior of writing to a CSV file in the
#        filesystem, and the using pandas to read the csv file. Since dt2pandas does
#        an import jmp, it's not needed by the calling scripts, but it does no harm
#        to import it from the calling script as well.
#
#  import pandas as pd
#  import dt2pandas as j2pd
#
#  dt = jmp.open(jmp.SAMPLE_DATA +'Big Class.jmp')
#  df = j2pd.to_pandas(dt)
#  print(df.head)
#
#  Or equivalently from JSL
# 
#  Names Default to Here(1);
#  dt = open("$SAMPLE_DATA/Big Class.jmp");
#  Python Send(dt);
#  Python Submit("\[ 
#  import dt2pandas as j2pd
#
#  df = j2pd.to_pandas(dt);
#  print(df.head)
#  ]\");
#
# See -    'JSL for exporting/saving JMP Data Table as CSV'
# https://community.jmp.com/t5/Discussions/JSL-for-exporting-saving-JMP-Data-Table-as-a-CSV-file-without/td-p/4620
#
# JMP 14-17 made a COPY of the data table and created a pandas.DataFrame using CSV files
#    as the transfer mechanism.
#
# JMP 18's Python Send(dt) creates a jmp.DataTable object that is a live reference 
#    to the actual data table allowing readinga and direct manipulation of the data  
#    table from Python.
#
# The to_pandas() function below replicates the previous behavior copying a
# JMP data table to pandas using CSV files.
import os
import jmp
import pandas as pd

def to_pandas(dt):

    jmp.run_jsl('''
    Names Default To Here(1);
    // save current prefs
    current_pref = Char( Arg( Parse( (Char( Get Preferences( Export settings ) )) ), 1 ) );
    
    // set up prefs for CSV export
    Pref( Export Settings( End Of Field( Comma ), Export Table Headers( 1 ) ) );
    ''')
    # Get the table by name
    s = '_dt_ = Data Table("' + dt.name + '");'
    print(s)
    jmp.run_jsl( s );
    jmp.run_jsl(''' _dt_ << save("$TEMP/dt_2_pd.csv", text);

    //Restore original prefs
    Eval( Parse( "pref(" || current_pref || ")" ) );
    ''')

    # create the data frame
    df = pd.read_csv(jmp.TEMP +'dt_2_pd.csv', skip_blank_lines=False)

    # remove the temporary CSV file
    os.unlink( jmp.TEMP + 'dt_2_pd.csv' )
    
    return df

#
# Disclaimer by 
# SAS Institute Inc. 
# 
# License Agreement for Corrective Code or 
# Additional Functionality 
#
# SAS INSTITUTE INC. IS PROVIDING YOU WITH THE COMPUTER SOFTWARE CODE INCLUDED WITH THIS AGREEMENT ("CODE") ON AN "AS IS" BASIS, AND AUTHORIZES YOU TO USE THE CODE SUBJECT TO THE TERMS HEREOF.  BY USING THE CODE, YOU AGREE TO THESE TERMS.  YOUR USE OF THE CODE IS AT YOUR OWN RISK.  SAS INSTITUTE INC. MAKES NO REPRESENTATION OR WARRANTY, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT AND TITLE, WITH RESPECT TO THE CODE. 
#
# The Code is intended to be used solely as part of a product ("Software") you currently have licensed from SAS or one of its subsidiaries or authorized agents ("SAS"). The Code is designed to either correct an error in the Software or to add functionality to the Software, but has not necessarily been tested.  Accordingly, SAS makes no representation or warranty that the Code will operate error-free.  SAS is under no obligation to maintain or support the Code.
#
# Neither SAS nor its licensors shall be liable to you or any third party for any general, special, direct, indirect, consequential, incidental or other damages whatsoever arising out of or related to your use or inability to use the Code, even if SAS has been advised of the possibility of such damages.
#
# Except as otherwise provided above, the Code is governed by the same agreement that governs the Software.  If you do not have an existing agreement with SAS governing the Software, you may not use the Code. 
#
#(SAS and all other SAS Institute Inc. product or service names are registered trademarks or trademarks of SAS Institute Inc. in the USA and other countries. ® indicates USA registration. Other brand and product names are registered trademarks or trademarks of their respective companies.)
#
