import nltk
from fetch import getScore

##pos_reviews=[('This is my favorite app n i can nver get sick of it...helps me stay connected in the most affordable way..n keeps getting better n better', 'positive'), 
##			('Its a great app I love and enjoy using this application, should be able to send  apk files, excel documents and those other attachments files, would be cool', 'positive'),
##			('Good app', 'positive'), ('Amazing app, love the way it is coded, the user interface is amazing and mind blowing', 'positive'), ('This is such an awesome app, its great', 'positive')]

##neg_reviews=[(' It would be nice if you can make an option that enables easy browsing of images that have been received. As of now its a little difficult to find pic sent a while back...so something that way will really be useful', 'negative'), ('Hey what\'s app, please add a option that only favorite contacts and can check out my status and profile pic because in my contacts I have many people like watchman, office staff person, office boy, customers  etc etc who are on whats app...  So why this unwanted people keep checking my personal status and profile pic.  So please do needful and add this feature', 'negative'),
##			('As the app is really gud at transfering messages...which ofcourse is the work of it and it does it great...but as you want to share anything u cant just mark evryperson nd send it in one go....but you have to send each person independently which is a lot time consuming....as for all a good aap....go for it', 'negative'),
##			('Cant send to multiple contacts unless they r in a group. Need to send msg to each contact one contact after another. Groups-not like in contacts. Should have a group for sending same message to all members of the group. Members limited to just 50 in a grup. Why the limit?? U wanna send to all u gotta send.. right??', 'negative'),
##			('whatsapp was known for its immediate transfer of messages. But now server is pathetic. In spite of good internet bandwidth messages take times to get delivered.  ', 'negative'),
##			('I suggest you add option for ringtones for contacts ,  I might need some contacts to be silent and others to know they sent me something', 'negative'), ('60 mb video is not going from one mobile to another. If you fix this I will give you 5 stars, please reply', 'negative'),
##			(' I would suggest adding the option to choose auto backup time. As, at 04 00, my phone is switched off when I sleep. So, it is not backuped', 'negative'), ('This app is not good, it sucks, cannot be used. It is useless', 'negative')]
			
pos_reviews = [('awesome' , 'positive') , (' Its very nice app' , 'positive') , ('I like it' , 'positive') , ('This app the is the best of my apps.' , 'positve') , ('faster than all other apps' , 'positive') , ('Love this game' , 'positive') , ('Very well made nice animations and very addiciting','positive') , ('Gud one' , 'positive') , ('Fun game' , 'positve') , ('Very easy to handle' , 'positve') , ('thanks' , 'positve') , ('i love it' , 'positve') , ('super fast' , 'positve') , ('wondeful graphics' , 'positve') , ('wonderful speed' , 'positve') , ('beautiful' , 'positve') , ('thumbs up' , 'positve') , ('amazing app' , 'positve') , ('best app' , 'positve') , ('Evrytone should download' , 'positve') , ('Superb' , 'positve') , ('its just awesome ' , 'positve') , ('cool' , 'positve') , ('Love it. Spot on' , 'positve') , ('Simple and nice app ' , 'positve') , ('Awesome application' , 'positve') , ('Really good' , 'positve') , ('Marvelous app' , 'positve') , ('Highly recommend' , 'positve') , ('Outstanding App' , 'positve') , ('Totally worth' , 'positve') , ('Sweet' , 'positve') , ('A must have for everyone' , 'positve') , ('Good god it Rocks' , 'positve') , ('Sweet, small and simple' , 'positve') , ('Superb' , 'positve') , ('Very clean' , 'positve') , ('efficient' , 'positve') , ('Easy to use ' , 'positve') , ('Easy and fast' , 'positve') , ('Not bad ' , 'positve') , ('Better' , 'positve') , ('Unbelievable' , 'positve') , ('Runs smooth ' , 'positve') , ('Looks great' , 'positve') , ('Best game I ever played' , 'positve') , ('Better than' , 'positve') , ('working fine' , 'positve') , ('fantastic graphics' , 'positve') , ('fantastic app' , 'positve') , ('Cool' , 'positve') , ('This is cool app to chat' , 'positve') , ('Best mobile' , 'positve') , ('nice idea' , 'positve') , ('Simply beautiful' , 'positve') , ('Addictive' , 'positve') , ('challenging' , 'positve') , ('keep up the good work' , 'positve') , ('mind blowing' , 'positve') , ('Great graphics ' , 'positve') , ('funny' , 'positve') , ('Really well done.' , 'positve') , ('I cant stop ' , 'positve') , ('very helpful' , 'positve') , ('Very entertaining' , 'positve') , ('interseting' , 'positve') , ('five stars' , 'positve') , ('positive' , 'positve') , ('Works perfect ' , 'positve') , ('stunning' , 'positve') , ('No problem' , 'positve') , ('Sexy' , 'positve') , ('perfect' , 'positve') , ('excellent' , 'positve') , ('Good stuff' , 'positve') , ('Satisfactory' , 'positve') , ('top app' , 'positve') , ('So far so good!' , 'positve') , ('Saving battery life' , 'positve') , ('epic' , 'positve') , ('good features' , 'positve') , ('useful' , 'positve') , ('This is my favorite app n i can nver get sick of it...helps me stay connected in the most affordable way..n keeps getting better n better', 'positive') , ('Its a great app I love and enjoy using this application, should be able to send  apk files, excel documents and those other attachments files, would be cool', 'positive') ,('Good app', 'positive'), ('Amazing app, love the way it is coded, the user interface is amazing and mind blowing', 'positive'), ('This is such an awesome app, its great', 'positive')]


neg_reviews = [('The update crashes sometimes and is slower than the previous versions' , 'negative') , ('negative' , 'negative' ) , ('stopped' , 'negative') , ('freezes sometimes and lags' , 'negative') , ('have to pay' , 'negative') , ('Application stops responding in between' , 'negative') , ('Has not worked for months' , 'negative') , ('Not even a game! Just spam ' , 'negative') ,('It is boring' , 'negative') ,('This is a completely useless app. ' , 'negative') , ('this is very poor application I dont like' , 'negative') ,('Waste of Internet Pack' , 'negative') , ('Doesnt work' , 'negative') , ('Take very long time to install' , 'negative') ,('there are huge problems.' , 'negative') ,('Very disappointed' , 'negative') , ('worst game ever downloaded' , 'negative') , ('Not satisfying' , 'negative') , ('Not very useful' , 'negative') , ('Error' , 'negative') , ('Didnt work on' , 'negative') , ('The background wont work' , 'negative') , ('Horrible' , 'negative') , ('Too much size' , 'negative') , ('too much memory' , 'negative') , ('cant run on background' , 'negative') , ('bad battery' , 'negative') , ('Doesnt share' , 'negative') , ('horrible app' , 'negative') , ('too many ads' , 'negative') , ('bad graphics' , 'negative') , ('issues with sound' , 'negative') , ('Its getting blurred so its very hard to fix it.' , 'negative') , ('Pls fix this' , 'negative') , ('Cant open' , 'negative') , ('Keeps Crashing' , 'negative') , ('Drains battery' , 'negative') , ('Lots of bugs since the last update' , 'negative') , ('Not able to use at all' , 'negative') , ('Featured and nearby wont load' , 'negative') , ('many bugs' , 'negative') , ('waste of money' , 'negative') , ('waste of data' , 'negative') , ('Solve problems ' , 'negative') , ('Doesnt work well' , 'negative') , ('Does not work with email or facebook, had to delete to get notifications back' , 'negative') , ('Dissatisfied' , 'negative') , ('It looks to have been copied ' , 'negative') , ('awful controls' , 'negative') , ('Boring not enough to do' , 'negative') , ('very bad graphics' , 'negative') , ('waste of memory' , 'negative') , ('dont download this' , 'negative') , ('dont install this' , 'negative') , ('total mess' , 'negative') , ('Please fix problem' , 'negative') , ('Have to keep uninstalling ' , 'negative') , ('sucks' , 'negative') , ('not satisfied' , 'negative') , ('cant load ' , 'negative') , ('wont send' , 'negative') , ('dissapointed' , 'negative') , ('not interesting' , 'negative') , ('WTF' , 'negative') , ('lame game' , 'negative') , ('Cant do anythingn' , 'negative') , ('WORST GAME EVER' , 'negative') , ('Bullshit' , 'negative') , ('Nonesense' , 'negative') , ('useless app' , 'negative') , ('excessive data consumption' , 'negative') , ('rubbish' , 'negative') , ('Too slow' , 'negative') , ('I cant login ' , 'negative') , ('Real bad for me now to use ' , 'negative') , ('Doesnt work' , 'negative') , ('Not worth my time' , 'negative') , ('So lame ' , 'negative') , ('Terrible' , 'negative') , ('Spam' , 'negative') , ('Needs Improvement' , 'negative') , ('no support' , 'negative') , ('Just as bad ' , 'negative') , ('Not user friendly' , 'negative') , ('Very poor app' , 'negative') , ('stupid lame and boring' , 'negative') , (' It would be nice if you can make an option that enables easy browsing of images that have been received. As of now its a little difficult to find pic sent a while back...so something that way will really be useful', ''), ('Hey what\'s app, please add a option that only favorite contacts and can check out my status and profile pic because in my contacts I have many people like watchman, office staff person, office boy, customers  etc etc who are on whats app...  So why this unwanted people keep checking my personal status and profile pic.  So please do needful and add this feature', 'negative'),('As the app is really gud at transfering messages...which ofcourse is the work of it and it does it great...but as you want to share anything u cant just mark evryperson nd send it in one go....but you have to send each person independently which is a lot time consuming....as for all a good aap....go for it', 'negative') , ('Cant send to multiple contacts unless they r in a group. Need to send msg to each contact one contact after another. Groups-not like in contacts. Should have a group for sending same message to all members of the group. Members limited to just 50 in a grup. Why the limit?? U wanna send to all u gotta send.. right??', 'negative') , ('whatsapp was known for its immediate transfer of messages. But now server is pathetic. In spite of good internet bandwidth messages take times to get delivered.  ', 'negative') , ('I suggest you add option for ringtones for contacts ,  I might need some contacts to be silent and others to know they sent me something', 'negative'), ('60 mb video is not going from one mobile to another. If you fix this I will give you 5 stars, please reply', 'negative') , (' I would suggest adding the option to choose auto backup time. As, at 04 00, my phone is switched off when I sleep. So, it is not backuped', 'negative'), ('This app is not good, it sucks, cannot be used. It is useless', 'negative')]

reviews=[]

for (words, sentiment) in pos_reviews + neg_reviews:		    #Cleans the manually classified data
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    reviews.append((words_filtered, sentiment))

def get_words_in_reviews(reviews):															
    all_words = []
    for (words, sentiment) in reviews:
      all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features
    
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

word_features = get_word_features(get_words_in_reviews(reviews))							

training_set = nltk.classify.apply_features(extract_features, reviews)
    
classifier = nltk.NaiveBayesClassifier.train(training_set)

readReview = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\preview.txt", "r")

storeReview = readReview.read()

readReview.close()

reviews_filtered = [e.lower() for e in storeReview.split() if len(e) >= 3]

##cleanedReviews=reviews_filtered
    
##print cleanedReviews

writeReview = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\cleanedReviews.txt", "w")

writeReview.truncate()

for i, j in enumerate(reviews_filtered):
	writeReview.write(str(j))
	writeReview.write("\n")

writeReview.close()

openReview = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\cleanedReviews.txt", "r")

finalReviews = openReview.read()

openReview.close()

##review='This app sucks. its bad dont use not'

result=classifier.classify(extract_features(finalReviews.split()))

writeResult = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\presult.txt", "w")

score = open("C:\Users\Aniket\Documents\Visual Studio 2010\WebSites\WebSite2\Python\score.txt", "r")

storeScore = score.read()

if(result=="positive" and storeScore <= '3.75'):
	result= "negative"

score.close()

writeResult.write(result)

writeResult.close()
