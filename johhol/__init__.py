import untangle
import requests

def fraction():
    r=requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
    data=untangle.parse(r.content)
    outages=data.NYCOutages.outage
    
    total=len(outages)
    repair=0
    
    for outage in outages:
        if outage.reason.cdata== 'REPAIR':
            repair+= 1
    fraction=float(repair)/float(total)
    print fraction
