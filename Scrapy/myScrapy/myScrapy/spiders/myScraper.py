import scrapy

#################### (1) Scraping Basics ######################
###############################################################

class NetSpiderOne(scrapy.Spider):
    """
    "name" & "start_urls" variable names must not be changed 
    """
    name = "netOne" # name of the spider
    start_urls = [ # list of sites to be scrapped
        'https://quotes.toscrape.com/',
        'https://alvee.vercel.app/'
    ]
    
    def parse(self, response):
        """
        Say we want to extract the title of the page and store it in variable "title"
        """
        title = response.css('title').extract()
        yield {'title_text' : title} # showed as a dictionary , yield used instead of return as inside scrapy used generator
    
    

############# (1.1) #############

############# (1.1) #############









#################### (2) Scraping Advanced ####################
###############################################################

############# (1.1) #############

############# (1.1) #############





#################### (3) Storing Scrapped Data ################
###############################################################



#################### (1) Scraping Basics ######################
###############################################################
