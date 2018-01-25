def get_s2_subregion(sentinelTwoGranule,sliceVals):
    """takes a sentineltwoGranule object and sliceVals
    which is a 4 value list [minY,maxY,minX,maxX]
    """
    v = sliceVals
    # make an empty array of correct size (mxnx4)
    arr = np.empty(shape=(v[1]-v[0],v[3]-v[2],4))
    # do the file open ops
    for i,key in enumerate(['B02','B03','B04','B08']):
        arr[:,:,i] = sentinelTwoGranule.msiBands[key].data[v[0]:v[1],v[2]:v[3]]
    return arr