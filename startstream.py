from pywinauto.application import Application
from pywinauto.controls import win32_controls
import xml.etree.ElementTree as ET
from TwitterAPI import TwitterAPI


# a class to store xml data for app usage.
class appSetting:

    def __init__(self, name=None,path=None, posX=None, posY=None, height=None, width=None):
        self.name = name
        self.path = path
        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width


# a class to store xml data for social media usage.
class socialClass:

    def __init__(self, twitch=None,tweet=None, facebook=None):
        self.twitch = twitch
        self.tweet = tweet
        self.facebook = facebook

appList = []

socialSetting = socialClass

# a class to store twitter xml data for send tweets.
class twitterAuthClass:

    def __init__(self, consumer_key=None,consumer_secret=None, access_token_key=None, access_token_secret=None,test=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.test = test



appList = []

def twitterXML():
    #load the config.xml data file
    tree = ET.parse('D:/twitter/twitter.xml')
    #set the root
    root = tree.getroot()

    twitterAuth.consumer_key = root.find('consumer_key').text
    twitterAuth.consumer_secret = root.find('consumer_secret').text
    twitterAuth.access_token_key = root.find('access_token_key').text
    twitterAuth.access_token_secret = root.find('access_token_secret').text
    twitterAuth.test = root.find('test').text

    print(twitterAuth.test)



twitterAuth = twitterAuthClass()
twitterXML()

api = TwitterAPI(twitterAuth.consumer_key, twitterAuth.consumer_secret, twitterAuth.access_token_key, twitterAuth.access_token_secret)





def openApp(name=None,path=None, posX=None, posY=None, height=None, width=None):
    app = Application().start(path)
    print (app)
    dlg = app['Notepad++']
    dlg = app.window(best_match=' - Notepad++')
    dlg.move_window(posX,posY)


def testNotePad():
    # Run a target application
    app = Application().start("notepad.exe")
   # dlg = app['Notepad']
   # dlg.move_window(10,10,100,100)


    # Select a menu item
    #app.UntitledNotepad.menu_select("Help->About Notepad")
    # Click on a button
    #app.AboutNotepad.OK.click()
    # Type a text string
    #app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

def readXMLFile():
    #load the config.xml data file
    tree = ET.parse('SSconfig.xml')
    #set the root
    root = tree.getroot()
    apps = root.find('apps')

    # parse the xml file and load the app data information for positions
    for app in apps.findall('app'):
        name = app.get('name')
        path = app.find('path').text
        posX = app.find('posX').text
        posY = app.find('posY').text
        height = app.find('height').text
        width = app.find('width').text
        appList.append(appSetting(name,path,posX,posY,height,width))

    social = root.find('social')
    socialSetting.twitch = social.find('twitch').text
    twitterEL = social.find('twitter')
    socialSetting.tweet = twitterEL.find('tweet').text
    socialSetting.facebook = social.find('facebook').text
    # test that the class has stored the correct data.
    for appData in appList:
        pass

def writeXMLFile():
    # create the file structure
    data = ET.Element('data')
    items = ET.SubElement(data, 'items')
    item1 = ET.SubElement(items, 'item')
    item2 = ET.SubElement(items, 'item')
    item1.set('name', 'item1')
    item2.set('name', 'item2')
    item1.text = 'item1abc'
    item2.text = 'item2abc'

    # create a new XML file with the results
    mydata = ET.tostring(data)
    myfile = open("items2.xml", "w")
    myfile.write(str(mydata))




def sendTweet(tweet):
    r = api.request('statuses/update', {'status': tweet})
    if r.status_code == 200:
        print('SUCCESS')
    else:
        print("Twitter Error: " + str(r.status_code))


def main():
    readXMLFile()
    #print (socialSetting.tweet)
    #sendTweet(socialSetting.tweet)
    for appData in appList:
        openApp(appData.name,appData.path,appData.posX,appData.posY)


main()


