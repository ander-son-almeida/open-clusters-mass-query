# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:02:53 2022

@author: Anderson Almeida
"""

'''
Gaia dr3 documentation about mass estimator: 
https://gea.esac.esa.int/archive/documentation/GDR3/Data_analysis/chap_cu8par/sec_cu8par_apsis/ssec_cu8par_apsis_flame.html

'''

from query_gaia import *
from graphics import *
from stars_flags import *
from load_members_ship import *

diretorio = r'S:\Área de Trabalho\open-clusters-mass-query'  

all_cluster = False
cluster_target = True

cluster_name = 'Melotte_22'

# load members_ship
members_ship = load_members_ship(diretorio, cluster_target, cluster_name, all_cluster)

# query gaia ADQL
gaia_dr3 = query_gaia(members_ship)

# stars flags
(ind_catalog, bin_system_catalog,
 gaia_dr3_mass_ind, gaia_dr3_mass_bin) = stars_flags(members_ship, gaia_dr3)

# plot graphics
graphics(gaia_dr3_mass_ind, ind_catalog, gaia_dr3_mass_bin, bin_system_catalog, 
         cluster_name, all_cluster, cluster_target)
    