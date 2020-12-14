#import to get the Object from implementation, this should be changed for the real Class if implemented the WebScraper
from src.json_formatter.dataset import *

# This function is responsible for instantiating the EndOfSaleProduct Object so we can use it as needed
def mock_generate_dataset(vendor,url,series,category,model,path,release,endofsale,endofsupport):
    cisco_valid_dataset = EndOfSaleProductDataset(vendor,url,series,category,model,path,release,endofsale,endofsupport)    
    return cisco_valid_dataset