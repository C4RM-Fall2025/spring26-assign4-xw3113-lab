
def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    cf = couponRate * face
    for timesZ, ycZ in zip(times,yc):
        pv = (1+ ycZ) **-timesZ
        pvcf= pv*cf
        #pvcfsum = pvcfsum + pvcf
        pvcfsum += pvcf
    bondprice = pvcfsum + pv*face
    return(bondprice)
