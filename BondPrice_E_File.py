
def getBondPrice_E(face, couponRate, m, yc):
    pvcfsum = 0
    cf = couponRate * face
    for t, ycE in enumerate(yc[:m], start=1):
        pv = (1 + ycE) ** (-t)
        pvcf = pv * cf
        pvcfsum += pvcf
    bondPrice = pvcfsum + pv * face
    return bondPrice
