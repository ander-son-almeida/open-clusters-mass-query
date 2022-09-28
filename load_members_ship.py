# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:05:23 2022

@author: Anderson Almeida
"""

import numpy as np
import numpy.lib.recfunctions as rfn

import pandas as pd


def load_members_ship(diretorio, cluster_target, cluster_name, all_cluster):

    if all_cluster == cluster_target:
        raise ValueError('Specify a cluster or select all!')
        
    else:

        if (cluster_target):
            
            members_ship = np.load(diretorio + r'\results_eDR3_likelihood_2022'
                                       '\membership_data_edr3\{}_data_stars.npy'.
                                       format(cluster_name))
            return members_ship
        
        if (all_cluster):
    
            list1 = []
            list2 = []
            list3 = []
            
            print('\n Wait a few minutes')
            
            cluster = pd.read_csv(diretorio + r'\results_eDR3_likelihood_2022\results'
                                  '\log-results-eDR3-MF_detalhada.csv', sep=';')
            cluster = cluster.to_records()
            
            filtro = np.genfromtxt(diretorio + r'\filters\amostra_dissertacao.csv',
                                   dtype=None, names=True, encoding=None, delimiter=';')

            ab, a_ind, b_ind = np.intersect1d(cluster['name'],filtro['clusters_bons'], 
                                              return_indices=True)
            cluster = cluster[a_ind]
            cluster = cluster[cluster['dist'] < 1000] #aplicando o filtro parar ter completeza
            cluster = cluster[cluster['mass_total'] > 0] #tirando o valor Nan
                        
            for i in range(0, cluster.shape[0]): 
                
                try:
                    cluster_name = (cluster['name'][i])
                    
                    members_ship = np.load(diretorio + r'\results_eDR3_likelihood_2022'
                                               '\membership_data_edr3\{}_data_stars.npy'.
                                               format(cluster_name))
                    
                    list1.append(members_ship['Source'])
                    list2.append(members_ship['mass'])
                    list3.append(members_ship['comp_mass'])
                    
                except:
                    pass
             
            # id and masses       
            source_catalog_ = np.concatenate(list1)
            catalog_mass_ind_ = np.concatenate(list2)
            catalog_mass_bin_ = np.concatenate(list3)
            
            source_catalog = np.full(source_catalog_.shape[0],source_catalog_, 
                                     dtype=[('Source', np.int64)])

            catalog_mass_ind = np.full(catalog_mass_ind_.shape[0], catalog_mass_ind_,
                                       dtype=[('mass', float)])
            catalog_mass_bin = np.full(catalog_mass_bin_.shape[0], catalog_mass_bin_, 
                                       dtype=[('comp_mass', float)])
    
            members_ship = rfn.merge_arrays((source_catalog, catalog_mass_ind, 
                                             catalog_mass_bin), flatten=True)
            
            return members_ship
