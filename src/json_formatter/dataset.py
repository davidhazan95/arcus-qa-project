# This module is responsible for describing the Class of the Product since we don't have a real implementation of it. This module is merely for instantiating mocks
class EndOfSaleProductDataset:
    def __init__(this,vendor,url,series,category,model,path,release,endofsale,endofsupport):
        this.vendor = vendor
        this.url = url
        this.series = series
        this.category = category
        this.model = model
        this.path = path
        this.release = release
        this.endofsale = endofsale
        this.endofsupport = endofsupport
# It was decided to not add Downloads as part of the parametrization, instead, just force it on implementation, since it can have more than one download, 
# it would be better to do a separate class for it and bond it in there
        this.downloads = [
                            {
                                "latest": "1.2.1RB4",
                                "filename": "firmware_P2MB_1.2.1rb4.zip",
                                "size": 32406078,
                                "md5": "a81300ffccbceff4f714c99c3ca3a12b"
                            },
                            {
                                "all": "https://software.cisco.com/download/home/286277668/type/286277896/release/1.2.1RB4?i=!pp"
                            }
                        ]