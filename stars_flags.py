# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:38:12 2022

@author: Anderson Almeida
"""
import numpy as np
############################################################################### 

def stars_flags(members_ship, gaia_dr3): 
    
    # buscando do query as estrelas em comum com o catalogo
    ind_ind = members_ship['comp_mass'] == 0 #indicando individuais
    ab, a_ind, b_ind = np.intersect1d(gaia_dr3['source_id'], members_ship['Source'][ind_ind], 
                                      return_indices=True)
    
    # Massas indivuais
    ind_catalog = members_ship['mass'][ind_ind][b_ind] #indivuals stars catalog
    gaia_dr3_mass_ind = gaia_dr3['mass_flame'][a_ind]
    
    
    ###############################################################################  
    # # indicando as binarias
    ind_b = members_ship['comp_mass'] > 0.
    cd, c_ind, d_ind = np.intersect1d(gaia_dr3['source_id'],members_ship['Source'][ind_b], 
                                      return_indices=True)
    
    # Massas binarias
    bin_system_catalog = (members_ship['mass']+ members_ship['comp_mass'])[ind_b][d_ind]
    gaia_dr3_mass_bin = gaia_dr3['mass_flame'][c_ind]
    
    return ind_catalog, bin_system_catalog, gaia_dr3_mass_ind, gaia_dr3_mass_bin