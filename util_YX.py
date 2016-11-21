# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:41:00 2016

@author: xiaoerhei
"""


def is_outlier(points, thresh=3.5):
    """
    Returns a boolean array with True if points are outliers and False 
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor. 
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh
def percentile_based_outlier(data, threshold=95):
    diff = (100 - threshold) / 2.0
    minval, maxval = np.percentile(data, [diff, 100 - diff])
    return (data < minval) | (data > maxval)



def percentile_outlier_treat(data,varList, threshold=90):
    output={}
    bd={}
    diff = (100 - threshold) / 2.0
    for i in (varList):
       temp = data[i]
       bd[i]={}
       minval, maxval = np.nanpercentile(temp, [diff, 100 - diff])
       H = 0.15 * max((np.nanpercentile(temp, 0.75)-np.nanpercentile(temp, 0.25)),4)
       data[i] = np.where(data[i]>maxval,maxval,data[i])
       data[i] = np.where(data[i]<minval,minval,data[i])
       bd[i]["lowBound"]=minval
       bd[i]["upBound"]=maxval
    output['dataSet']=data
    output['bd']=bd
    
    return (output)









l










































