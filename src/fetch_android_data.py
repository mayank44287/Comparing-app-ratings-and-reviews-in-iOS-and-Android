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

#df.to_csv('./data/android_data.csv', index = False)
social = ["1065781769","1096918571","454638411","284882215","985746746","985746746","1462082664","643496868","304878510","686449807"]
games = ["1344700142","1490384223","1094591345","1499812410","664575829","1498817833","1494449873","623592465","1500564080","406889139"]
health_and_fitness = ["571800810","301521403","387771637","1099771240","634598719","1168348542","462638897","1241229134","300235330","487847188", "1361619409"]
travel = ["293622097","368677368","529379082","401626263","1245772818","904418768","989307692","288113403","336381998","1438670520","474259675","533365777"]
utility = ["868077558","1178765645","416023011","309172177","491126018","926252661","942608209","621574163","1200318119","561625752","917932200"]
education = ["924620788","570060128","756972930","919087726","522826277","552602056","467329677","469863705","875063456","453142230","950424861","546473125","977976646"]
lifestyle = ["429047995","1490078757","680819774","944011620","930441707","1161035371","1222822904","463630399","1462195529","464988855","1288415553","1459289784"]

category_dict = {0: "social", 1: "games", 2:"health_and_fitness", 3:"travel", 4:"utility", 5:"education", 6:"lifestyle"}


android_url_list = ["https://play.google.com/store/apps/details?id=com.herzick.houseparty&hl=en_US&showAllReviews=true&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.android.apps.tachyon&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.facebook.katana&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.discord&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.whatsapp&hl=en_US","https://play.google.com/store/apps/details?id=com.popshow.yolo&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.android.talk&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.skype.raider&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=org.telegram.messenger&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.matteljv.uno&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.xmgame.savethegirl&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.freeplay.runandfight&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.playrix.fishdomdd.gplay&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.fivebits.borderpatrol&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.playgendary.creamaster&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.wb.headsup&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.panteon.homesweethome&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.moonactive.coinmaster&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.calm.android&hl=en_US&showAllReviews=true","https://play.google.com/store/apps/details?id=com.nike.ntc&showAllReviews=true","https://play.google.com/store/apps/details?id=com.nike.plusgps&showAllReviews=true","https://play.google.com/store/apps/details?id=com.bendingspoons.thirtydayfitness&showAllReviews=true","https://play.google.com/store/apps/details?id=com.wsl.noom&showAllReviews=true","https://play.google.com/store/apps/details?id=com.zerofasting.zero&showAllReviews=true","https://play.google.com/store/apps/details?id=com.fitbit.FitbitMobile&showAllReviews=true","https://play.google.com/store/apps/details?id=com.reflectlyApp&showAllReviews=true","https://play.google.com/store/apps/details?id=com.fitnesskeeper.runkeeper.pro&showAllReviews=true","https://play.google.com/store/apps/details?id=gov.cdc.general&showAllReviews=true","https://play.google.com/store/apps/details?id=net.beginners.weight.loss.workout.women.yoga.go&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.earth&showAllReviews=true","https://play.google.com/store/apps/details?id=com.ubercab&showAllReviews=true","https://play.google.com/store/apps/details?id=me.lyft.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.airbnb.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.vrbo.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.android.street&showAllReviews=true","https://play.google.com/store/apps/details?id=com.uhaul.android.myuhaul&showAllReviews=true","https://play.google.com/store/apps/details?id=at.nk.tools.iTranslate&showAllReviews=true","https://play.google.com/store/apps/details?id=com.priceline.android.negotiator&showAllReviews=true","https://play.google.com/store/apps/details?id=com.spirit.customerapp&showAllReviews=true","https://play.google.com/store/apps/details?id=com.pilottravelcenters.mypilot&showAllReviews=true","https://play.google.com/store/apps/details?id=com.flistholding.flightplus&showAllReviews=true","https://play.google.com/store/apps/details?id=com.bitstrips.imoji&showAllReviews=true","https://play.google.com/store/apps/details?id=com.xfinity.digitalhome&showAllReviews=true","https://play.google.com/store/apps/details?id=com.vzw.hss.myverizon&showAllReviews=true","https://play.google.com/store/apps/details?id=com.att.myWireless&showAllReviews=true","https://play.google.com/store/apps/details?id=com.sprint.care&showAllReviews=true","https://play.google.com/store/apps/details?id=com.ringapp&showAllReviews=true","https://play.google.com/store/apps/details?id=com.brighthouse.mybhn&showAllReviews=true","https://play.google.com/store/apps/details?id=com.amazon.clouddrive.photos&showAllReviews=true","https://play.google.com/store/apps/details?id=com.apple.qrcode.reader&showAllReviews=true","https://play.google.com/store/apps/details?id=com.tmobile.pr.mytmobile&showAllReviews=true","https://play.google.com/store/apps/details?id=com.riffsy.FBMGIFApp&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.android.apps.classroom&showAllReviews=true","https://play.google.com/store/apps/details?id=com.duolingo&showAllReviews=true","https://play.google.com/store/apps/details?id=com.vidku.app.flipgrid&showAllReviews=true","https://play.google.com/store/apps/details?id=com.microblink.photomath&showAllReviews=true","https://play.google.com/store/apps/details?id=com.remind101&showAllReviews=true","https://play.google.com/store/apps/details?id=com.classdojo.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.bagatrix.mathway.android&showAllReviews=true","https://play.google.com/store/apps/details?id=org.khanacademy.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.wonder&showAllReviews=true","https://play.google.com/store/apps/details?id=com.piazza.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.blackboard.android.bbstudent&showAllReviews=true","https://play.google.com/store/apps/details?id=com.quizlet.quizletandroid&showAllReviews=true","https://play.google.com/store/apps/details?id=co.brainly&showAllReviews=true","https://play.google.com/store/apps/details?id=com.pinterest&showAllReviews=true","https://play.google.com/store/apps/details?id=com.c2m.frankly&showAllReviews=true","https://play.google.com/store/apps/details?id=com.google.android.apps.chromecast.app&showAllReviews=true","https://play.google.com/store/apps/details?id=com.amazon.dee.app&showAllReviews=true","https://play.google.com/store/apps/details?id=com.bumble.app&showAllReviews=true","https://play.google.com/store/apps/details?id=com.prayapp.client&showAllReviews=true","https://play.google.com/store/apps/details?id=com.samsung.android.oneconnect&showAllReviews=true","https://play.google.com/store/apps/details?id=com.victoriassecret.pinknation&showAllReviews=true","https://play.google.com/store/apps/details?id=com.survjun&showAllReviews=true","https://play.google.com/store/apps/details?id=com.nest.android&showAllReviews=true","https://play.google.com/store/apps/details?id=com.hualai&showAllReviews=true","https://play.google.com/store/apps/details?id=com.arlo.app&showAllReviews=true"]
android_master_dict = {}

counter = 0
social_a = android_url_list[counter:counter + len(social)]
counter = counter + len(social)
games_a = android_url_list[counter:counter + len(games)]
counter = counter + len(games)
hf_a = android_url_list[counter: counter + len(health_and_fitness)]
counter = counter + len(health_and_fitness)
travel_a = android_url_list[counter:counter + len(travel)]
counter = counter + len(travel)
utility_a = android_url_list[counter: counter + len(utility)]
counter = counter + len(utility)
education_a = android_url_list[counter: counter + len(education)]
counter = counter + len(education)
lifestyle_a = android_url_list[counter: counter + len(lifestyle)]
counter = counter + len(lifestyle)

master_android_list = [social_a, games_a, hf_a, travel_a, utility_a, education_a, lifestyle_a]


def get_android_id(url_string):
    p = re.compile(".+\\bdetails\\?id=([^&]+)")
    result = p.search(url_string)
    appid = result.group(1)
    return appid

for index, i in enumerate(master_android_list):
    for j in i:
        android_master_dict[get_android_id(j)] = category_dict[index]



def apply_android_category(row):
    return android_master_dict[row['appId']]
df['category'] = df.apply (lambda row: apply_android_category(row), axis=1)
df.to_csv('./data/android_data.csv', index = False)
