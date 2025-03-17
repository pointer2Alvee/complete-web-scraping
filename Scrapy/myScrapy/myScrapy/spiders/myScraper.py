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
    ]
    
    def parse(self, response):
        """
        Say we want to extract the title of the page and store it in variable "title"
        title = response.css('title').extract() # extracts the <title> tag + text-in-a-list
        title = response.css('title::text').extract() # extracts the text only in a list
        title = response.css('title::text')[0].extract() # extracts the first item from list, return error if no element at [0]
        title = response.css('title::text').extract_first() # extracts the first item from list, if if no item a [0] then error handled, returns none
        quotes = response.css("span.text::text")[1].extract() # extracts the second item from list, return error if no element at [1]
        """
        ########### (1) SCRAPING USING CSS SELECTORS ###########
        """
        .css('title::text') --> is more like an if condition like if css tag title exists then grab the text class 
        """
        
        # 1. Scraps The title - using CSS selector
        title = response.css("title::text").extract_first() 
        yield {'title_text' : title} # showed as a dictionary , yield used instead of return as inside scrapy used generator
        

        # 2. Scraps The Quotes - using CSS selector
        quotes = response.css("span.text::text")[1].extract()
        yield {'quote_text' : quotes} # yield can be used once or multiple times

        # 3. Scraps The Quotes - using CSS selector
        author = response.css("small.author::text").extract()
        yield {'author_text' : author} # yield can be used once or multiple times
    
    
        ########################################################
        """
        Say we want to extract the title of the page and store it in variable "title"
        title = response.css('//title').extract() # extracts the <title> tag + text-in-a-list
        title = response.css('//title//text()').extract() # extracts the text only in a list
        title = response.css('//title//text()')[0].extract() # extracts the first item from list, return error if no element at [0]
        title = response.css('//title//text()').extract_first() # extracts the first item from list, if if no item a [0] then error handled, returns none
        quotes = response.css("//span[@class='text']/text()")[1].extract() # extracts the second item from list, return error if no element at [1]

        In order to select ID instead of a class:-
        quotes = response.css("//span[@id='text']/text()")[1].extract()
        """
        ########### (2) SCRAPING USING XPATH ###################  
        # 1. Scraps The title - using XPATH selector
        #title = response.xpath("//title").extract_first() 
        xp_title = response.xpath("//title/text()").extract_first() 
        yield {'xp_title_text' : xp_title} # showed as a dictionary , yield used instead of return as inside scrapy used generator
        

        # 2. Scraps The Quotes - using XPATH selector
        xp_quotes = response.xpath("//span[@class='text']/text()").extract()
        yield {'xp_quote_text' : xp_quotes} # yield can be used once or multiple times

        # 3. Scraps The Quotes - using XPATH selector
        
        xp_author = response.xpath("//small[@class='author']/text()").extract()
        yield {'xp_author_text' : xp_author} # yield can be used once or multiple times
    
        
        
        ########################################################
        """
        Say we want to extract the next of the page and store it in variable "next"
        next_text = response.css('li.next a').xpath("@href").extract()      
            --> selects the li class next and its a tag then from a tag we extract value of href
        
        next_text = response.css('a').xpath("@href").extract()
            --> ectracts all a tags
        """
        ########### (3) SCRAPING USING CSS + XPATH #############
        next_text = response.css('li.next a').xpath("@href").extract()
        yield {'next_text' : next_text}
        
        all_a_tags = response.css('a').xpath("@href").extract()
        yield {'all_a_tags' : all_a_tags}
        
        
        
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
