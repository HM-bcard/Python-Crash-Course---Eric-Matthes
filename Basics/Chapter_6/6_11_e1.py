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

for city in cities:
    print(f"Th city is {city} and teh information are : {cities[city]}.")
