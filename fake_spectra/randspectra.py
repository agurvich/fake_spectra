# -*- coding: utf-8 -*-
"""Class to gather and analyse various metal line statistics"""

from __future__ import print_function
import numpy as np
import hdfsim
import spectra

class RandSpectra(spectra.Spectra):
    """Generate metal line spectra from simulation snapshot"""
    def __init__(
        self,num, base, ndla = 1000, numlos=5000, res = 1., cdir = None,
        thresh=10**20.3, savefile="rand_spectra_DLA.hdf5",
        savedir=None, elem="H", ion=1,units=None,ext_fname=None,
        use_corr_UInt = False):
        #Load halos to push lines through them
        f = hdfsim.get_file(num, base, 0,ext_fname=ext_fname)
        self.box = f["Header"].attrs["BoxSize"]
        f.close()
        self.NumLos = numlos
        #All through y axis
        axis = np.ones(self.NumLos)
        #Sightlines at random positions
        #Re-seed for repeatability
        np.random.seed(23)
        cofm = self.get_cofm()
        #np.save('/n/home04/agurvich/lymanalpha/src/cofm',cofm)
        spectra.Spectra.__init__(self,num, base, cofm, axis, res=res, cdir=cdir, savefile=savefile,savedir=savedir,reload_file=True, units=units, load_halo=False,ext_fname=ext_fname)

        self.use_corr_UInt = use_corr_UInt

        if np.size(thresh) > 1 or thresh > 0:
            self.replace_not_DLA(ndla, thresh, elem=elem, ion=ion)
            print("Found objects over threshold")


    def get_cofm(self, num = None):
        """Find a bunch more sightlines: should be overriden by child classes"""
        if num == None:
            num = self.NumLos
        cofm = self.box*np.random.random_sample((num,3))
        return cofm

