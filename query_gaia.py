# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:13:57 2022

@author: Anderson Almeida
"""

from astroquery.gaia import Gaia
import numpy as np

# query gaia ADQL
def query_gaia(members_ship):
    print('\n Query loading...')
    query = """SELECT 
    source_id, mass_flame
    FROM gaiadr3.astrophysical_parameters
    WHERE source_id IN {}
    """.format(tuple(members_ship['Source'].tolist()))
    
    job = Gaia.launch_job_async(query)
    gaia_dr3 = np.array(job.get_results())
    
    # remove NaNs
    ind = np.where(gaia_dr3['mass_flame'] > 0)
    gaia_dr3 = gaia_dr3[ind]
    
    return gaia_dr3