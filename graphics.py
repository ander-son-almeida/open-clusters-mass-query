# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:26:02 2022

@author: Anderson Almeida
"""
import matplotlib.pyplot as plt


def graphics(gaia_dr3_mass_ind, ind_catalog, gaia_dr3_mass_bin, bin_system_catalog, 
         cluster_name, all_cluster, cluster_target):
    
    if (cluster_target):
    
        fig, ax = plt.subplots(1,2,figsize=(10,5))
        
        fig.suptitle('{}'.format(cluster_name))
        
        ax[0].plot([0,gaia_dr3_mass_ind.max()],[0,gaia_dr3_mass_ind.max()],'r')
        
        ax[0].scatter(gaia_dr3_mass_ind,ind_catalog, 
                    alpha=0.5, label='Individual')
        ax[0].scatter(gaia_dr3_mass_bin,bin_system_catalog,
                    alpha=0.5, label='Binary')
            
        ax[0].set_aspect('equal')
        ax[0].set_xlim(gaia_dr3_mass_ind.min()-0.1,gaia_dr3_mass_ind.max())
        ax[0].set_ylim(gaia_dr3_mass_ind.min()-0.1,gaia_dr3_mass_ind.max())
        ax[0].set_xlabel(r'DR3 (2022) ($M_{\odot}$)')
        ax[0].set_ylabel(r'This work ($M_{\odot}$)')
        ax[0].legend()
        
        
        
        ax[1].hist((gaia_dr3_mass_ind-ind_catalog)/ind_catalog,
                 bins='auto',label='Individual',alpha=0.5)
        ax[1].hist((gaia_dr3_mass_bin-bin_system_catalog)/bin_system_catalog,
                 bins='auto',label='Binary',alpha=0.5)
        
        ax[1].set_xlabel(r'DR3 (2022) ($M_{\odot}$)')
        ax[1].set_ylabel(r'This work ($M_{\odot}$)')
        ax[1].legend()
        
    if (all_cluster):
        
        fig, ax = plt.subplots(1,2,figsize=(10,5))
        
        fig.suptitle('All sample completeness')
        
        ax[0].plot([0,gaia_dr3_mass_ind.max()],[0,gaia_dr3_mass_ind.max()],'r')
        
        ax[0].scatter(gaia_dr3_mass_ind,ind_catalog, 
                    alpha=0.5, label='Individual')
        ax[0].scatter(gaia_dr3_mass_bin,bin_system_catalog,
                    alpha=0.5, label='Binary')
            
        ax[0].set_aspect('equal')
        ax[0].set_xlim(gaia_dr3_mass_ind.min()-0.1,gaia_dr3_mass_ind.max())
        ax[0].set_ylim(gaia_dr3_mass_ind.min()-0.1,gaia_dr3_mass_ind.max())
        ax[0].set_xlabel(r'DR3 (2022) ($M_{\odot}$)')
        ax[0].set_ylabel(r'This work ($M_{\odot}$)')
        ax[0].legend()
        
        
        
        ax[1].hist((gaia_dr3_mass_ind-ind_catalog)/ind_catalog,
                 bins='auto',label='Individual',alpha=0.5)
        ax[1].hist((gaia_dr3_mass_bin-bin_system_catalog)/bin_system_catalog,
                 bins='auto',label='Binary',alpha=0.5)
        
        ax[1].set_xlabel(r'DR3 (2022) ($M_{\odot}$)')
        ax[1].set_ylabel(r'This work ($M_{\odot}$)')
        ax[1].legend()
        
    