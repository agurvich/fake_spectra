#!/usr/bin env python
# -*- coding: utf-8 -*-
"""Make some plots of 2d histograms, velocity widths vs some other things"""

import matplotlib
matplotlib.use('PDF')

import matplotlib.pyplot as plt

import plot_spectra as ps
import os.path as path
import numpy as np
from save_figure import save_figure

base="/home/spb/scratch/Cosmo/"
outdir = base + "plots/2d_hist/"
print "Plots at: ",outdir

def plot_max_col_den(sim, snap, ff=False):
    """Load a simulation and plot the metal column density vs the HI column density"""
    halo = "Cosmo"+str(sim)+"_V6"
    if ff:
        halo+="_512"
    #Load from a save file only
    hspec = ps.PlottingSpectra(snap, base+halo, None, None)
    metal_col_den = np.max(hspec.get_col_density("Si", 2),axis=1)
    HI_col_den = np.max(hspec.get_col_density("H", 1),axis=1)
    ind = np.where(metal_col_den > 1e12)
    (H, xedges, yedges) = np.histogram2d(np.log10(metal_col_den[ind]), np.log10(HI_col_den[ind]), bins=30,normed=True)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    plt.imshow(H, extent=extent, aspect="auto", vmax = 0.15)
    plt.colorbar()

def plot_vel_col_den(sim, snap, ff=False):
    """Load a simulation and plot the metal column density vs the HI column density"""
    halo = "Cosmo"+str(sim)+"_V6"
    if ff:
        halo+="_512"
    #Load from a save file only
    hspec = ps.PlottingSpectra(snap, base+halo, None, None)
    metal_col_den = np.max(hspec.get_col_density("Si", 2),axis=1)
    vel= hspec.vel_width(hspec.get_tau("Si",2))
    ind = np.where(metal_col_den > 1e12)
    (H, xedges, yedges) = np.histogram2d(np.log10(metal_col_den[ind]), np.log10(vel[ind]), bins=30,normed=True)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    plt.imshow(H, extent=extent, aspect="auto")
    plt.colorbar()

def plot_vel_den(sim, snap, ff=False):
    """Load a simulation and plot the metal column density vs the HI column density"""
    halo = "Cosmo"+str(sim)+"_V6"
    if ff:
        halo+="_512"
    #Load from a save file only
    hspec = ps.PlottingSpectra(snap, base+halo, None, None)
    vel = hspec.vel_width(hspec.get_tau("Si",2))
    den = hspec.vel_width(hspec.get_col_density("Si", 2))
    ind = hspec.get_filt("Si",2)
    (H, xedges, yedges) = np.histogram2d(np.log10(den[ind]), np.log10(vel[ind]), bins=30,normed=True)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    plt.imshow(H, extent=extent, aspect="auto")
    plt.colorbar()

def plot_vel_HI_col_den(sim, snap, ff=False):
    """Load a simulation and plot the metal column density vs the HI column density"""
    halo = "Cosmo"+str(sim)+"_V6"
    if ff:
        halo+="_512"
    #Load from a save file only
    hspec = ps.PlottingSpectra(snap, base+halo, None, None)
    metal_col_den = np.max(hspec.get_col_density("Si", 2),axis=1)
    HI_col_den = np.max(hspec.get_col_density("H", 1),axis=1)
    vel= hspec.vel_width(hspec.get_tau("Si",2))
    ind = np.where(metal_col_den > 1e12)
    (H, xedges, yedges) = np.histogram2d(np.log10(HI_col_den[ind]), np.log10(vel[ind]), bins=30,normed=True)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    plt.imshow(H, extent=extent, aspect="auto")
    plt.colorbar()


colors=["blue", "purple", "orange", "red"]
reds = {54:4, 60:3, 68:2}

for ii in (0,1,2,3):
    #Plot col_density of metals vs HI
    plot_max_col_den(ii, 60)
    save_figure(path.join(outdir,"cosmo"+str(ii)+"z3_coldens"))
    plt.clf()

for ii in (0,1,2,3):
    #Plot metal col. den vs vel width
    plot_vel_den(ii, 60)
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_vel_den_z3"))
    plt.clf()


for ii in (0,1,2,3):
    #Plot metal col. den vs vel width
    plot_vel_col_den(ii, 60)
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_vel_col_z3"))
    plt.clf()

for ii in (0,1,2,3):
    #Plot metal col. den vs vel width
    plot_vel_HI_col_den(ii, 60)
    save_figure(path.join(outdir,"cosmo"+str(ii)+"_vel_HI_col_z3"))
    plt.clf()