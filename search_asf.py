import sys
import asf_search as asf

def main(argv):

    opts = {
        'platform': asf.PLATFORM.SENTINEL1A,
        'start': '2016-08-01T00:00:00Z',
        'end': '2016-08-31T23:59:59Z'
    }
    aoi1 = 'POLYGON((-90.8881117 30.2836521,   -90.7989272  30.2836521, -90.7989272  30.2269194, -90.8881117  30.2269194, -90.8881117 30.2836521))'              

    results = asf.geo_search(intersectsWith=aoi1, **opts)
    #print(results)
    for r in results:
        url = r.properties['url']
        if "SLC" in url:
            print(url)
    return
if __name__ == "__main__":
    main(sys.argv[1:])
    