```python
!pip install tweepy
```

    Collecting tweepy
      Downloading tweepy-3.9.0-py2.py3-none-any.whl (30 kB)
    Requirement already satisfied: six>=1.10.0 in c:\users\vallabhan\anaconda3\lib\site-packages (from tweepy) (1.15.0)
    Collecting requests-oauthlib>=0.7.0
      Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
    Requirement already satisfied: requests[socks]>=2.11.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from tweepy) (2.24.0)
    Collecting oauthlib>=3.0.0
      Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests[socks]>=2.11.1->tweepy) (2020.6.20)
    Requirement already satisfied: idna<3,>=2.5 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests[socks]>=2.11.1->tweepy) (2.10)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests[socks]>=2.11.1->tweepy) (1.25.9)
    Requirement already satisfied: chardet<4,>=3.0.2 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests[socks]>=2.11.1->tweepy) (3.0.4)
    Requirement already satisfied: PySocks!=1.5.7,>=1.5.6; extra == "socks" in c:\users\vallabhan\anaconda3\lib\site-packages (from requests[socks]>=2.11.1->tweepy) (1.7.1)
    Installing collected packages: oauthlib, requests-oauthlib, tweepy
    Successfully installed oauthlib-3.1.0 requests-oauthlib-1.3.0 tweepy-3.9.0
    


```python
!pip install wordcloud
```

    Collecting wordcloud
      Downloading wordcloud-1.8.0-cp38-cp38-win_amd64.whl (159 kB)
    Requirement already satisfied: pillow in c:\users\vallabhan\anaconda3\lib\site-packages (from wordcloud) (7.2.0)
    Requirement already satisfied: numpy>=1.6.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from wordcloud) (1.18.5)
    Requirement already satisfied: matplotlib in c:\users\vallabhan\anaconda3\lib\site-packages (from wordcloud) (3.2.2)
    Requirement already satisfied: python-dateutil>=2.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from matplotlib->wordcloud) (2.8.1)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from matplotlib->wordcloud) (1.2.0)
    Requirement already satisfied: cycler>=0.10 in c:\users\vallabhan\anaconda3\lib\site-packages (from matplotlib->wordcloud) (0.10.0)
    Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from matplotlib->wordcloud) (2.4.7)
    Requirement already satisfied: six>=1.5 in c:\users\vallabhan\anaconda3\lib\site-packages (from python-dateutil>=2.1->matplotlib->wordcloud) (1.15.0)
    Installing collected packages: wordcloud
    Successfully installed wordcloud-1.8.0
    


```python
import tweepy
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 
```


```python
consumer_key = 'SYrSUUtSMj9axUDGeaa15v9lb'
consumer_secret = 'wFx1VF4DZ24F1aE4Ll915n3kndh30dApTKC5K4LQ9sFXeoF0Iq'
access_token = '1286681690019110914-KU9w8PLUGR5SLfUHjm5qk5tFvo6o5y'
access_token_secret = 'iiS4DUZ0g0hvB0b4fm8LaK42ocwfzie9YeRHk4h7V2jxc'
```


```python
!pip install vaderSentiment
```

    Collecting vaderSentiment
      Downloading vaderSentiment-3.3.2-py2.py3-none-any.whl (125 kB)
    Requirement already satisfied: requests in c:\users\vallabhan\anaconda3\lib\site-packages (from vaderSentiment) (2.24.0)
    Requirement already satisfied: idna<3,>=2.5 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests->vaderSentiment) (2.10)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests->vaderSentiment) (2020.6.20)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests->vaderSentiment) (1.25.9)
    Requirement already satisfied: chardet<4,>=3.0.2 in c:\users\vallabhan\anaconda3\lib\site-packages (from requests->vaderSentiment) (3.0.4)
    Installing collected packages: vaderSentiment
    Successfully installed vaderSentiment-3.3.2
    


```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
```


```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```


```python
def list_tweets(user_id, count, prt=False):
    tweets = api.user_timeline(
        "@" + user_id, count=count, tweet_mode='extended')
    tw = []
    for t in tweets:
        tw.append(t.full_text)
        if prt:
            print(t.full_text)
            print()
    return tw
```


```python
user_id = 'inc_atcs' 
count=10000
tw_atcs = list_tweets(user_id, count)
```


```python
tw_atcs
```




    ['Here’s Ajay Torgal, Managing Director, ATCS Bengaluru, talking about the rising importance of Robotic Process Automation in Healthcare industry pertaining to the impacts of pandemic. - https://t.co/NjmlKTRwOQ\n\n#ATCS #RoboticProcessAutomation #Healthcare #Technology #HBot https://t.co/CbrZd1ioAM',
     'Turning into ‘Describers’ and ‘Artists’, members at ATCS USA gathered virtually and played this fun game of ‘Can You Hear Me Now?’. Interesting descriptions, sketches, and guesses made it worth witnessing. \n\n#CanYouHearMeNow #ATCS #FunActivity #EmloyeeEngagement #GreatWorkPlace https://t.co/00ngfwBW8b',
     'Here’s Roop Singh, Executive Director – India, ATCS, sharing his opinion on how digitization of healthcare data can be leveraged to combat crisis, and identify challenges proactively through data analysis. - https://t.co/1oVzoHwXEH\n\n#ATCS #BigData #Analytics #DataAnalysis #COVID https://t.co/eRjuOvoeko',
     "@Salesforce Live: India virtual event was incredible! Packed with innovative ideas, expert sessions, inspiring customers stories, the event had something for everyone. Here’s a look at how ATCS' Team engaged in the virtual session\n#ATCS #Salesforce #SalesforceLiveEventIndia #LIVE https://t.co/fgChO86GVi",
     "@Salesforce Live: India virtual event was incredible! Packed with innovative ideas, expert sessions, inspiring customers stories, the event had something for everyone. Here’s a look at how ATCS' Team engaged in the virtual session\n#ATCS #Salesforce #SalesforceLiveEventIndia #LIVE https://t.co/rDZSojl0N5",
     'Here’s Sven Sommerfeld, Managing Director, ATCS GmbH, sharing his #LeadershipOutlook comprised of views on resource productivity, business and dealing with transformation during the pandemic.\n\n#Leadership #ATCS #BusinessGrowth #OrganizationValues #Pandemic https://t.co/PQy1zLuEDX',
     'The much-awaited result is here! We are pleased to announce the winners of The Great Frame Photography Contest – Hitesh Jain &amp; Vamsi Tripasuri. Have a look at their mesmerizing clicks. \n\n#ATCSGreatFrameChallenge #ATCS #Photography #Creativity https://t.co/n0HQWTirea',
     'ATCS conducted Virtual Scrum Training where a comprehensive session on the subject was delivered. Pandemic has surely not distanced our enthusiastic learners from acquainting ahead. \n\n#ATCS #ScrumTraining #Agile #Technology #ProjectManagement #Globalcollaboration https://t.co/gumul9GvG7',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at - https://t.co/TI9yZ70gAM\n\n#marketingstrategies #brandcommunication #brandcomm\n#consumerbehaviour #brandmarketing #covid #coronavirus #newnormal #advertising #ContentMarketing https://t.co/ErkhCEGa7Q',
     'Tushar Patil, Managing Director – ATCS North America, stating his #LeadershipOutlook towards the pandemic’s impacts, challenges, and effective approach.\n\n#Leadership #ATCS #BusinessGrowth #OrganizationValues https://t.co/U6G7T4z7Ip',
     'ATCS marks a spot in the Inc. 5000 list of the fastest-growing private companies in America! We’re extremely thankful to all our members, partners, and clients – who have contributed to our consistent growth.\n\n#INC5000 #ATCS #FastestGrowingCompany #ITConsulting https://t.co/NuJtBceKWq',
     'We are distant, still strongly connected! Recently, we organized ATCS Virtual Townhall – August 2020, an organizational meet where our Leadership Team along with members gathered virtually. \n\n#ATCS #ATCSVirtualTowhall #BusinessPlanning #Leadership #Communication #businessgrowth https://t.co/fkfmK8nSt8',
     'Pictionary being a game of quick sketches and great guesses, brought an unforgettable recreational experience to the teams of ATCS Jaipur. Have a look at the fun-filled glimpses!\n\n#Pictionary #ATCSWorkCulture #EmployeeEngagement #FunActivity8 https://t.co/JgTxbzBn6o',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at - https://t.co/TI9yZ7hRsk\n\n#covid #usa #pandemic #analytics #digitaltransformation #technology #digitalanalytics #digitalmarketingtrends #coronavirusoutbreak https://t.co/5TqXN4SB1V',
     'ATCS Germany team’s first post-quarantine get-together – here’s the glimpse! Their smiles express it all with an excitement for many more such moments.\n\n#ATCS #ATCSWorkCulture #TeamBond #WeAreBack #PostQuarantine https://t.co/4ZUkX60mng',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at - https://t.co/TI9yZ7hRsk\n\n#covid #usa #pandemic #analytics #digitaltransformation #technology #digitalanalytics #digitalmarketingtrends https://t.co/Wvmnz7cutl',
     'On this sacred day, may almighty caress our lives with His grace, love, and kindness. ATCS wishes everyone a very happy #Eid.\n\n#EidMubarak #Festivals #ATCS #GoodWishes #AuspiciousOccasion https://t.co/BuoE8rvQsC',
     'ATCS Family wishes everyone a very happy #InternationalFriendshipDay.\n\n#ATCS #Friendship #BestColleagues #StrongBond #StandingByEachOther https://t.co/TXsjLbXVqo',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/zwfajNBbeX\n#students #elearning #covid19 #teachers #parents #backtoschool #digitaltransformation #technology #socialanalytics #digitalanalytics https://t.co/SU6IraX7mp',
     'Our team at ATCS GmbH participated in the #SelfieChallenge with great enthusiasm. Though this activity emerged as sure-shot fun, it carried the ‘new normal’ message of wearing masks – wherever you are!\n\n#ATCS #WorkCulture #FunActivity #SelfieChallenge #NewNormal https://t.co/FvFR0vDUr3',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/xcavFjab1P\n\n#travel #travelindustry #traveltechnology #hospitality #hospitalityindustry #covid19 https://t.co/G6vKgKJH2J',
     'Sven Sommerfeld, Partner &amp; Managing Director, ATCS GmbH, talks about reliance on automobile aftersales segment on AI, IoT, &amp; ML to enhance customer satisfaction.  Have a good read: https://t.co/hC3UZiaguk\n\n#ArtificialIntelligence #MachineLearning #Telematics #ATCS https://t.co/eJYIolPmNe',
     'When work and fun co-exist, it makes way for a great work culture – ATCS USA members ensures this with virtual professional collaborations while having fun activities as well. Have a glance at how well they stay connected!\n\n#WorkFromHome #ATCSWorkCulture #VirtualMeetings https://t.co/dabvnoTnwR',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/xcavFiSAah\n\n#sociallistening #socialanalytics #insights #covid19 #coronavirus https://t.co/DxgneWZ8Ya',
     'Members of ATCS Jaipur returned to office and joyously uttered #WeAreBack. Have a look at what they have to say.\n\n#BackToOffice #WorkResumes #Excitement #GoodToBeBack https://t.co/9H0iSnFX2V',
     'Members of ATCS Jaipur returned to office and joyously uttered #WeAreBack. Have a look at what they have to say.\n\n#BackToOffice #WorkResumes #Excitement #GoodToBeBack https://t.co/eIwQhGVO0w',
     'Members of ATCS Germany returned to office and joyously uttered #WeAreBack. Have a look at what they have to say.\n\n#BackToOffice #WorkResumes #Excitement #GoodToBeBack https://t.co/aEBjHXSJqW',
     'Members of ATCS Germany returned to office and joyously uttered #WeAreBack. Have a look at what they have to say.\n\n#BackToOffice #WorkResumes #Excitement #GoodToBeBack https://t.co/lxvLfLp7Xf',
     'Members of ATCS China returned to office and joyously uttered #WeAreBack. Have a look at what they have to say.\n\n#BackToOffice #WorkResumes #Excitement #GoodToBeBack https://t.co/P0uVfvzwJ8',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/xcavFjab1P\n\n#sociallistening #socialanalytics #insights #covid19 #coronavirus https://t.co/amDjr2udyc',
     'Ensuring the safest workspace for our members, most of our ATCS offices have resumed. Have a look at how ATCS Jaipur is following all the necessary precautionary measures.\n\n#NewNormal #Safety #Hygiene #BackToWork https://t.co/rwXdgKvvd6',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/4PH4b7jlcD https://t.co/sglSY5cLvi',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/OycjgfWhH7\n\n#sociallistening #socialanalytics #insights #covid19 #coronavirus https://t.co/2L6hBNxK1Q',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/JcYfcynbFP\n\n #sociallistening #socialanalytics #insights #covid19 #coronavirus https://t.co/yygSwXNWm0',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/aDO1274o4N\n\n#sociallistening #insights #covid19 #coronavirus #socialanalytics https://t.co/Flor6Y6R0w',
     'Pets are a bliss! This lockdown may have its own disadvantages but has surely given us a quality time to relish with our pets. So, we went on to make the most of the moments and took great Petfies.\n\n#Petfie #PetLove #BondWithPets #ATCSFunActivity #WorkCulture #workispawsome https://t.co/CoF5st4u4E',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/6ylBhWFRuH\n\n#sociallistening #insights #covid19 #coronavirus #socialanalytics https://t.co/TwC9Ttqco7',
     'How Americans are reacting to the COVID-19 crisis. View our social listening studies on this topic at – https://t.co/eu4wwpvSL1\n\n#sociallistening #insights #covid19 #coronavirus #socialanalytics https://t.co/hTRzl71QGi',
     "ATCS celebrated Women's day with great zest and cheer. Here are the glimpses. https://t.co/EWrQnoVWk9",
     'Awareness is certainly the confronting answer to CANCER!\nBy basing stern and impactful cancer awareness, around 7 million lives could be saved in the next decade, globally! \n\n#WorldCancerDay #CancerAwareness #FightingCancer #ATCSCares #HealthyWorld #CancerFreeWorld #IAmAndIWill https://t.co/lq1E7dEAFB',
     'Asian Age features Mr. Roop Singh, Executive Director – ATCS India and his thoughts about "Impact of big data analytics on Indian economy." Link: https://t.co/k4JlSq0J34 https://t.co/fX4KTy6hRT',
     'Team ATCS at @IITBHU_Varanasi for campus placement.\n\n#iitbhu #campushiring #atcstalentsearch https://t.co/JXxJiGFplv',
     'Team ATCS at @iitroorkee for campus placement!!\n\nCongratulations to the selected aspirants and wishing them luck to be a part of our team!\n\n#iitroorkee #campushiring #atcstalentsearch https://t.co/XbmNIoxeER',
     'ATCS Germany had a great time baking cookies with children and painting a reading room. Here are the glimpses:\n\n#csractivities #atcsculture #happychildren https://t.co/QSCZ614PyE',
     'Concluded our annual #campushiring at @IITKanpur with an overwhelming response from brilliant minds and hiring some amazing talent!\nCongratulations to the selected folks and excited to have you On-board soon.\n\n#campusplacements #ATCStalentsearch #congratulations https://t.co/dEvvqytfy9',
     'Press Release Coverage in Yahoo India: https://t.co/CKgty2GafD\nATCS Pvt. Ltd. Gets CMMI Maturity Level 5 Recognition!!\n\n#CapabilityCounts #cmmimaturitylevel5 #cmmi #atcsgo #yahooIndia https://t.co/MpNSqxveVe',
     'RT @Poornima_Univ: We congratulate all the students who have been #placed at @ATCS_Group, a digital sol., product &amp; services company that h…',
     'ATCS represented at the Detroit Automotive Warranty Conference.\n\n#Detroitautomotiveconference #ATCS #automotiveindustry https://t.co/r6IrUlJ1HE',
     'ATCS participated in Job fair in Stuttgart, Germany.\n\n# #ATCS #JobsInGermany #Jobs #ITJobs #campusplacement #ATCStalentsearch #recruitmentdrive https://t.co/vMobkyQhEC',
     'Team ATCS at Poornima University, Rajasthan for Campus placement.\n\n#campusplacement #ATCStalentsearch #recruitmentdrive https://t.co/aXkIX2210L',
     'Team ATCS at JECRC University, Rajasthan for Campus placement.\n\n#campusplacement #ATCStalentsearch #recruitmentdrive https://t.co/XeZQrHSaB8',
     'ATCS participated in the Beijing Automotive Roundtable, where more than 50 automotive industry representatives discussed about the latest trends of “Connected Vehicles for Future Mobility”\n\n#connectedvehicles #futuremobility #datamonetization #atcsgo #beijingautomotiveroundtable https://t.co/G0zKPIs2Fa',
     'Team ATCS @SKIT College for Campus placement.\n\n#atcsgo #campusplacements #atcstalentsearch https://t.co/2jAeCM3wGQ',
     'ATCS has been appraised at level 5 of the @CMMI_Institute’s Capability Maturity Model Integration! #CapabilityCounts ##cmmimaturitylevel5 #cmmi #atcsgo https://t.co/cLmSpeR4hU',
     "Nikhil Singhal, Associate Data Scientist at ATCS has shared his view on how healthcare industries are using the latest technologies to connect and influence the patient's opinion.\n\nRead on to find more: https://t.co/mC4mucc2qT\n\n#coverage #healthcare #expresshealthcare #atcsgo https://t.co/4MRKod394O",
     'Ajay Torgal, Executive Director at ATCS has shared his thoughts on how H-bots is set to revolutionize the healthcare industry and can help minimize disruption even when the systems are under pressure. Read on to find more: https://t.co/NEDA1Y7x9x\n\n#coverage #healthcare #atcsGo https://t.co/uRYFIRbZa2',
     'Ajay Torgal, Executive Director at ATCS has shared his thoughts on how bots are helping the shipping industry to simplify their process.\n\nhttps://t.co/vluUypromM…/simplifying-shipment-tracking-proc…/\n\n#chatbots #shippingindustry #IT #ATCS #technology https://t.co/xAH4PUOfvM',
     'In this smart tech era, ATCS understands that Chatbots can be the possible solution to insurance agents problems that not only augments their efficiency but also help companies to generate more business. Read on to find more: https://t.co/4H4NJURiTi \n #chatbots #moneycontrol https://t.co/p52wE6zZ11',
     'Migration to Cloud is a process that almost every organization is now following owing to the various advantages that Cloud has to offer. Read here to  know more: https://t.co/2LGVjQhOXI \n #migrationtocloud #enterprizeapplications #cloudcomputing https://t.co/ZXU6CNfyau',
     "As a leading disruptor of our time, digital transformation is generating change throughout the automotive industry. Let's take a look at the major aspects here: https://t.co/lquTGNs0Hw\n #digitaltransformation #automotiveindustry #digitization #change #digitizationwave https://t.co/pRf4VEAdWm",
     "Do you know what kind of challenges are faced by the HR department to retain the workforce? Read this  blog to know the HR practices that help in retention and augment the  company's productivity: https://t.co/VSj8maAa56\n #employeeretention #HRpractices #Productivity #workbalance https://t.co/DtytSPHZFm",
     'ATCS at T5-Job fair in Stuttgart\n\n #T5JobFairStuttgart2019 #T5JobFairStuttgart #ATCS #JobsInGermany #Jobs #ITJobs #T5JobMesseStuttgart https://t.co/iTlwaLPdyJ',
     'To all the techies, analysts, and consultants out there in Germany, the wait will be over tomorrow.\n\nDrop by at the Stuttgart job fair from 10 am to 4 pm where you can meet our team and get all your career related queries answered.\n \n#T5JobFairStuttgart2019 #ATCS #ITJobsInGermany',
     'RT @5v3n50mm3rf3ld: Looking forward to representing @ATCS_Group at this years #engautowarranty conference in #Brussels.  https://t.co/UqyH6…',
     'Two Week to go!\nJoin us for a freewheeling chat at the Stuttgart job fair where you can meet our team and shoot all your career related queries. Sign up for free and meet us at "T5 Job Messe Stuttgart 2019" on 27th March from 10 am to 4 pm.\n\n#T5JobFairStuttgart2019#ATCS #ITJobs',
     'Team ATCS at SKIT College, Jaipur for a seminar on Big Data and Data Science.\n\n#DataScience #Bigdata #ATCS #SKIT #seminars https://t.co/McwpE53QSA',
     "To help you make an informed career choice, ATCS is taking part in one of Germany's biggest job fairs this month: T5 Job Messe Stuttgart 2019. See you on 27th of March. \n\n#T5JobFairStuttgart2019 #T5JobFairStuttgart #ATCS #JobsInGermany #Jobs #ITJobs #T5JobMesseStuttgart",
     'Team ATCS @JECRC Foundation for seminar on Big Data and Data Science https://t.co/47rJfnzHGP',
     'Team ATCS at BITS Pilani for campus placement.\n#ATCSTalentSearch #Campusplacement #BitsPilani #JobOpportunities https://t.co/pYeSEOxu9B',
     '#DataCenters #ATCStech, #LatestTechnology https://t.co/biqCESF5DN',
     'Data centers are vital for the smooth functioning of the digital economy and the connected world. How? Read on to know about the role played by data centers in the current scenario as well as in the future: https://t.co/3046pq3dVH \n\n#DataCenters #DigitalEconomy #smartcities https://t.co/xWt6XH9P55',
     'This #WorldCancerDay, ATCS visited Cancer hospital in Jaipur to visit children undergoing cancer treatment and shared some beautiful moments with them. \n\n#cancerawareness #cancerfree #CSR #atcsculture https://t.co/sXVjrCWwgz',
     'Happy Chinese New Year 2019 from ATCS China\n\n#chinesenewyear2019 #springfestival #atcs https://t.co/uSXYrJ1xLs',
     '#ATCS #certifications #achievements https://t.co/madzu7ONnO',
     '@ATCS_Group Townhall 2019 Clarion Bella Casa, Jaipur\n\n#Townhall2019 #ATCS #ShareYourThoughts https://t.co/vk4iy2vIZH',
     '#Townhall #TeamATCS #ShareYourThoughts https://t.co/biHj8X7Hla',
     '#Connectedcars #ATCStech #latestTechnology https://t.co/HzUnH8dJm1',
     'Digitization of Automobiles is the new normal !! Want to know how emerging technologies are paving way for connected cars, then read here: https://t.co/l3fDEWrXud\n\n#ConnectedCars #AutomobileIndustry #Digitisation https://t.co/BksNzS5uaj',
     '#ATCSIndia #BusinessStrategies #KeyTechnologies https://t.co/2HzHYLHEEZ',
     'Roop Singh, executive director, ATCS, talks to Paromik\nChakraborty of the EFY Group about the firm’s business\nstrategies for Indian industries. Read more at https://t.co/Ofs13HZrue \n#businessstrategies #ATCSIndia #EFYMagazine https://t.co/rn7kyLflrg',
     '#AtcsChina #IndiaChinaCorridor #DigitalSolutions https://t.co/1H54DlEfeX',
     'Christmas celebration across various locations of ATCS.\n#atcsjaipur #atcsmumbai #atcschina #atcsgermany #christmasCelebration https://t.co/5wlTEwwkub',
     'India-China IT corridor aims to offer greater market access for IT companies. Let’s understand how ATCS has aligned strategically to market trends and is leading the way. Read more at https://t.co/RZrSQqnLuV \n\n#ATCS #IndiaChinaCorridor #DigitalSolutions https://t.co/HhFiCEmPHo',
     'ATCS India HQ Moving to Mahindra SEZ. Read More @https://bit.ly/2R7ZDG5\n#MahindraSEZ #ATCS #Businessmadeeasy https://t.co/GrW6eNCv7R',
     'Team ATCS Jaipur @ SPL Corporate league Season- 5.\n#ATCSGlimpses #cricketleague #playtowin https://t.co/oZYyPyC7yb',
     'Team ATCS @IIT Roorkee for campus placement.\n#ATCSTalentSearch #Campusplacement #IITians #JobOpportunities https://t.co/kCNDasORyL',
     'ATCS Team @IIT-BHU and @IIT Kanpur with shortlisted candidates.\n#ATCSTalentSearch #Campusplacement #congratulations #IITians https://t.co/ifwVceX8yG',
     'Team ATCS @ IIT-BHU for Campus Placement.\n#ATCSTalentSearch #Campusplacement #IIT https://t.co/7HJOGZ457O',
     '#innovativemanagement #employeecentric #atcs https://t.co/GSa8Re4IlV',
     'ATCS @DataHack Summit 2018 at Bengaluru\n\n#datahacksummit #hacking #datasecurity https://t.co/4AMwJCaumN',
     'The utopian future of driverless car in India guarantees safer and spacious roads and reduces the risk of accidents. Read on to find more about the future of autonomous vehicles in India at https://t.co/Tu3DmoxPfR\n\n#AutonomousVehicles #connectedcars #ArtificialIntelligence https://t.co/31fsUzQOMB',
     'ATCS recognized as APAC CIO Outlook Top 10 Automotive Solution Provider - 2018 https://t.co/r57ab1ZzSC',
     'As “Make in India” completes its 4 glorious years, Manish Krishnan, CEO of ATCS Inc. shares his experience on how ATCS is contributing to India’s Domestic growth. Read more at https://t.co/7Dx7YySd15 https://t.co/q9oKs7lzVm',
     'Technologies like Big Data are set to revolutionize the future of automotive industry. Take a sneak peek at our informative article featured in Deccan Chronicle magazine.\n\n#bigdata #automation #connectedcars #autonomousvehicles #deccanchronicle\n\nhttps://t.co/3c3z3am8nY',
     'ATCS Completes 5 Years Association With Make-A-Wish https://t.co/ZWAfnJ8yUM',
     'Leading discussions around Automotive Warranty in Detroit at #enguswarranty https://t.co/J0WgcvPtcL',
     '#enguswarranty https://t.co/RVNjgEE5QD',
     '@JasonCastellani',
     'ATCS represented at the ENG Automotive Warranty Conference in Detroit. #enguswarranty https://t.co/oDdPeDoC15',
     'CEO Insight Magazine: Top Indian CEO from the US in 2018. Congratulations to our #ATCS #CEO Manish Krishnan!\nhttps://t.co/8Xj9sYuLvE',
     'Our head of Digital Services talking about if Artificial Intelligence is Overblown in Social Media Circles? Check it out: \nhttps://t.co/KYLrD77SUe\n#ArtificialIntelligence #socialmedia #digitalservices #atcs #idealyst',
     'Is this the next step to buy/rent a car? https://t.co/MvArHKGURq',
     'What is a connected car and its features. Read more here: https://t.co/OFQHOrCoKt\n#atcs #ConnectedCar #iot #telematics',
     "#atcs is presenting its #bigdata services today at the BigData #Expo in #Guizhou. Come by our booth and talk to our experts Vishwaraaj Shetty and Xueyan Lang. We're there from May 26 - May 28.\n#analytics #deeplearning #machinelearning #atcs https://t.co/tUlgj5k9es",
     'State of the art ist uns zu langweilig. Interesse an einem #Job in dem Du Deine Ideen verwirklichen kannst? =&gt; https://t.co/MU8dij2sUc \n#stellenanzeige #itconsultant #businessanalyst #atcs #jobsuche',
     '#WeChat is the fastest and easiest  way to attract new #customers to your brand in #china. #ATCS can help you to use the full potential of over 960 million daily user. Get your #free #whitepaper on how #WeChat can help your company here:\nhttps://t.co/YkPbLk81Gj\n#digitalmarketing',
     '#WeChat ist die schnellste und einfachste Form in #China neue Kunden zu gewinnen. #ATCS kann Ihnen helfen das volle Potential von über 960 Millionen täglichen Nutzern auszuschöpfen. Sichern Sie sich Ihr #kostenloses #whitepaper hier: https://t.co/QdbyLVHA1n\n#digitalmarketing',
     'Artificial intelligence can lip-read better than a trained professional - via @techreview https://t.co/S59LtZq76r',
     '#atcs ist heute auf der #engautowarranty in Berlin vertreten. Schauen Sie doch einfach mal bei unserem Stand vorbei. \n\n#atcs presents its services today at the #engautowarranty. Just stop by our booth to get more information. https://t.co/TscKjTFELZ',
     '#ATCS has been recognized as one of the 39 organizations which create exceptional workplaces by #Gallup: https://t.co/1ljt6bPSMC \nIf you want to find out how we do it, visit us in one of our offices around the wold. #awesomeworkplace #werehiring #softwaredevelopment',
     'ATCS eröffnet sein achtes Büro in #Atlanta. \nATCS opens its eight office in #Atlanta.\nCome and visit us!\nhttps://t.co/qslMnJIH3L\n#awesomeworkplace #atcs #globalfootprint #softwaredevelopment #itconsulting',
     'RT @Daimler: Mercedes-Benz is giving approximately 700,000 customers a digital Easter present that’s very special: what3words https://t.co/…',
     "RT @iotconsortium: Per @UMich's Transportation Research Institute, up to 8.1 million car crashes and 44,000 deaths could be prevented if th…",
     'RT @DeepLearn007: Types of machine learning algorithms\n#AI #MachineLearning #BigData #Fintech #Insurtech #Marketing #DataScience #ML #Robot…',
     'RT @iotconsortium: Top industries investing in #IoT today and in 3 years (via @PwC). #Auto leads the way today. https://t.co/M3WzpnEX3f',
     'RT @iotconsortium: #IoT: Evolution or Revolution? https://t.co/RbseDMgbaD',
     'Kennen Sie Ihre #Influencer? Kennen Sie die #PainPoints Ihrer Verbraucher? Finden Sie mit #SocialListening heraus, wie Sie im Vergleich zu Ihren Mitbewerbern wahrgenommen werden. Sichern Sie sich Ihren kostenlosen Report hier: https://t.co/ngaMZuNQxV \n#ATCSDigitalServices',
     'RT @DeepLearn007: McKinsey: What’s now and next in analytics &amp; AI\n#AI #MachineLearning #DeepLearning #BigData #Fintech #Insurtech #Marketin…',
     'Our managing director in China, Vish Shetty, talking about the expat community in China. https://t.co/0EhzDwsWGf\n#china #atcs #expat #beijing #werehiring',
     'Our employees Leonard Wianke, Tristan Vogt, David Horbank talking about why ATCS is the perfect company for them and their development. https://t.co/km3IzNlz4l\n#atcs #awesomeworkplace',
     'Congratulations @MBUSA https://t.co/MrRisr0Duq',
     'Beautfil example how data visualization can help understand data: https://t.co/WKUDnBUs6Q\n#data #visualization',
     'ATCS Germany is wishing a happy holi to all colleagues and partners of the ATCS family.\nMay this holi will bring color of happiness to you and your families. https://t.co/Gd12zBWzxj',
     'ATCS जर्मनी आपने ATCS परिवार के सभी सहकर्मचारियोंको होली त्यौहार की बहुत बहुत  शुभकामनाये देता है।.\nयह होली आपके  ओर  आपके  परिवार में खुशियोंका रंग भर दे।.',
     'RT @YarmolukDan: A computer was trained to play Qbert and immediately broke the game in a way no human ever has https://t.co/yqN5RJHR6J #ML…',
     'Interesse an einem Praktikum als Webentwickler in einem agilen und innovativem Unternehmen?\nBewirb Dich hier: https://t.co/uAyc856Fcn \n#praktikum #webentwickler #atcs #awesomeworkplace',
     'RT @DeepLearn007: MIT: Reshaping Business With Artificial Intelligence\n#AI #MachineLearning #DeepLearning #BigData #Fintech #Insurtech #Mar…',
     'RT @Daimler: Private car sharing and Digital Vehicle Key: The new A-Class: sharing with friends, contactless opening👉 https://t.co/lKFteCp0…',
     'RT @iotconsortium: Long-term timeline of emerging science and technology: a visual framework via @rossdawson =&gt; https://t.co/PyqX2JnGcv htt…',
     'State of the art ist uns zu langweilig. Interesse an einem Job in dem Du Deine Ideen verwirklichen kannst? =&gt; https://t.co/G7EsVOx8kx \n#stellenanzeige #itconsultant #businessanalyst #atcs',
     'WeChat ist die schnellste und einfachste Form in China neue Kunden zu gewinnen. ATCS kann Ihnen helfen das volle Potential von über 960 Millionen täglichen Nutzern auszuschöpfen.\nhttps://t.co/sWog5tFejX\n\n#WeChat #digitalmarketing #China #atcs',
     'It’s a candidate’s perspective that matters: https://t.co/LzCOdJVSoH\n\nUnser global HR Head Esha Chowdhary im Interview über Recruitment.\nOur global HR Head Esha Chowdhary  sharing her thoughts on recruitment.\n\n#atcs #hr #talentaquisition',
     'Hallo Welt! ATCS ist nun auch auf Twitter unterwegs!\nHello World! ATCS is now also active on Twitter!\n#meinErsterTweet #myFirstTweet #itservices #softwaredevelopment #analytics #digitalmarketing\n\nFollow us: https://t.co/RGCrXZsBae']




```python
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)        
    return input_txt
    
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def clean_tweets(lst):
    # remove twitter Return handles (RT @xxx:)
    lst = np.vectorize(remove_pattern)(lst, "RT @[\w]*:")
    # remove twitter handles (@xxx)
    lst = np.vectorize(remove_pattern)(lst, "@[\w]*")
    # remove URL links (httpxxx)
    lst = np.vectorize(remove_pattern)(lst, "https?://[A-Za-z0-9./]*")
    # remove special characters, numbers, punctuations (except for #)
    lst = np.core.defchararray.replace(lst, "[^a-zA-Z#]", " ")
    return lst
```


```python
tw_atcs[2]
```




    'Here’s Roop Singh, Executive Director – India, ATCS, sharing his opinion on how digitization of healthcare data can be leveraged to combat crisis, and identify challenges proactively through data analysis. - https://t.co/1oVzoHwXEH\n\n#ATCS #BigData #Analytics #DataAnalysis #COVID https://t.co/eRjuOvoeko'




```python
def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1
```


```python
def anl_tweets(lst, title='Tweets Sentiment', engl=True ):
    sents = []
    for tw in lst:
        try:
            st = sentiment_analyzer_scores(tw, engl)
            sents.append(st)
        except:
            sents.append(0)
    ax = sns.distplot(
        sents,
        kde=False,
        bins=3)
    ax.set(xlabel='Negative                Neutral                 Positive',
           ylabel='#Tweets',
          title="Tweets of @"+title)
    return sents
```


```python
import seaborn as sns
```


```python
tw_atcs_sent=anl_tweets(tw_atcs,user_id)
```


![png](output_15_0.png)



```python
def word_cloud(wd_list):
    stopwords = set(STOPWORDS)
    all_words = ' '.join([text for text in wd_list])
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        width=1600,
        height=800,
        random_state=21,
        colormap='jet',
        max_words=50,
        max_font_size=200).generate(all_words)
    plt.figure(figsize=(12, 10))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation="bilinear");
```


```python
word_cloud(tw_atcs)
```


![png](output_17_0.png)



```python

```
