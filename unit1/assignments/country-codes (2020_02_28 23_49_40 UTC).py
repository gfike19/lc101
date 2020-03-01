def get_country_codes(prices):
    new_prices = prices.split()
    
    new_list = []
    for codes in new_prices:
        new_list.append(codes[0:2])
        
    return(', '.join(new_list))

# don't include these tests in Vocareum
from test import testEqual

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")