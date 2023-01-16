# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 08:59:03 2020

@author: vishnu
"""

import numpy as np
import pandas as pd


dt = pd.date_range('20190101',periods = 6,freq = 'D')

df = pd.DataFrame(np.random.randn(6,4),index = dt,columns = list('ABCD'))

df2 = pd.DataFrame({'A':2,
                    'B':pd.Series(1,index = list(range(4))),
                    'D':np.array([3]*4)
                    },index = range(4))

df2.plot()