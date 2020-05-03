#import statements
import re
from google_play_scraper import Sort, reviews
import pandas as pd
from itertools import chain


#opening the appsid file
#extract appids from urls
def get_review(url_string):
    p = re.compile(".+\\bdetails\\?id=([^&]+)")
    result = p.search(url_string)
    appid = result.group(1)
    
    result, continuation_token = reviews(
    appid,
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=100, # defaults to 100
    filter_score_with=None # defaults to None(means all score)
    )
    
    #dataframe for app reviews
    '''
    df_app = pd.DataFrame(result)
    
    #drop stuff you don't need
    del df_app['userImage']
    del df_app['reviewCreatedVersion']
    del df_app['repliedAt']
    del df_app['replyContent']
    del df_app['userName']
    df_app.columns = ['at', 'content', 'score', 'thumbsUpCount']
    
    print(df_app)
    return df_app
    '''
    
    for element in result:
        element['appId'] = appid
        
    return result




try:
    with open('./resources/appsid', 'r') as aid:
        urls = aid.readline().split(',')

except IOError:
    print('Error while opening App\'s ID file. make sure that\
    you have a file named "appsid" in the irectory of this\
    scrip and you have right permissions to access file. \nExiting...')
    
length = len(urls)
#master dataframe
columns = ['at', 'content', 'score', 'thumbsUpCount']

app_data_list = []


while length:
    try:
        for url in urls:
            app_data = get_review(url.strip('\"'))
            app_data_list.append(app_data)
            print(str(length) + ' apps left')
            length -= 1
    except IOError as e:
        print('Operation Failed Error...')
        pass

df = pd.DataFrame(list(chain.from_iterable(app_data_list)))
#drop stuff you don't need 

del df['userImage']
del df['reviewCreatedVersion']
del df['repliedAt']
del df['replyContent']
del df['userName']
del df['at']

df.to_csv('./data/android_data.csv', index = False)

