from isatools.model import *
from isatools import isatab
'''
Created on 31 Oct 2018

@author: ostlerr
'''

def create_descriptor():
    investigation = Investigation()
    investigation.identifier = "bbkworms2014"
    investigation.title = "Broadbalk Earthworm Survey 2014, selected plots"
    investigation.description = "Earthworm survey data collected from selected Broadbalk plots during spring 2014"
    investigation.submission_date = "2016-09-29"
    investigation.public_release_date = "2017-02-24"
    
    study = Study(filename = "bbk_worm_data.csv")
    study.identifier = "sbbkworms2014"
    study.title = "Broadbalk Earthworm Survey 2014, selected plots"
    study.description = "Earthworm survey data collected from selected Broadbalk plots during spring 2014"
    study.submission_date = "2016-09-29"
    study.public_release_date = "2017-02-24"
    