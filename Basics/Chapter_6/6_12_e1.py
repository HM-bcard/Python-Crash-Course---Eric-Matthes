cities = {'New York':{'country':'United states','population':20_000_000,
                      'fun_fact':'sometimes is called "The Big Apple'}, 
          'San Fransico':{'country':'United states','population':10_000_000,
                      'fun_fact':'sometimes is called "The Hippie capital"'},
            'Honolulu':{'country':'United states','population':2_000_000,
                      'fun_fact':'Is situated in Hawaii'},
              'Prague':{'country':'Czech republic','population':2_000_000,
                      'fun_fact':'has good food'},
              'Vienna':{'country':'Austria','population':3_000_000,
                      'fun_fact':'One of the cultural capitals of Europe'}
}

for city,info in cities.items():
    #for info_item,value in info.items():
        print(f"The city is {city} and it's located in {info['country']} "
              f"it's population is {info['population']} "  
              f"and a fun fact about it is that {info['fun_fact']}"
              )
