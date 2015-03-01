# -*- coding: UTF-8 -*-
import os, urllib2, urllib

#设置下载后存放的本地路径"D:\xampp\htdocs\html5"
dirPath = r'D:\xampp\htdocs\html5'
gameName = r'TapTheMouse'
gamePath = os.path.join(dirPath, gameName)
#设置链接的路径
#http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/game.htm
#http://sda.4399.com/4399swf/upload_swf/ftp14/wangc/20141024/4/index.htm
# delete from [finger].[dbo].[Table_1]
# select DISTINCT id FROM [finger].[dbo].[Table_1]
# INSERT INTO [finger].[dbo].[Table_1] ([id]) VALUES ('/4399swf/upload_swf/ftp14/wangc/20140811/01/assets/sound/color_crash.mp3') 
baseUrl = "http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/"
allUrl = [
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/game.htm',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/4399.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/api/voyager.js',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/api/voyager_base-83d560e0d0350eb5ccd49f0320347575.js',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/bootstrap/progress/loader_back.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/bootstrap/progress/loader_progress.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/bootstrap/progress/logo.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/locale/messages.ini',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/bg0.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/bg1.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/bg2.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/bglevelselect.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/CatFinalMc.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/DarkMc.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/LevelCompleteMenu.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/main.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/page1.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/page2.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/page3.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/bg/shelf.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/Arial.fnt',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/Arial_0.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/cartoonist.fnt',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/cartoonist_0.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/sports.fnt',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/sports.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/sports_big.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/fonts/sportsbig.fnt',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game2.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game2.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game3.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/game3.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/ball_lost.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/bounce_platform.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/click.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/clock.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/drop_box.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/find.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/glass.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/lampscrew.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/level_win.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/loop.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/mouse.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/popup.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/shake_box.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/slide2.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/star1.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/star2.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/star3.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/switch.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/tnt.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/sounds/wood.mp3',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/stars.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/stars.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/ui.json',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/main/ui.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/sg.hooks.js',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/sg-loader.gif',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/softgames-1.1.js',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/assets/voyager-71c9db55a2771fa00f1072bf4f5ea985.css',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/rotate-phone.png',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/softgames_game.js',
'http://sda.4399.com/4399swf/upload_swf/ftp14/ck/20141107/6/targets/main-html.js']

#拼接文件路径
def joinGameDir(mBaseUrl, mUrl):
	mUrl = mUrl.replace(mBaseUrl, "")
	filePath = os.path.join(gamePath, mUrl)
	filePath = filePath.replace("/", "\\")
	filePath = filePath.replace("%20", " ")
	return filePath

#获取文件路径所在文件夹路径
def pathDirName(mFilePath):
	dirPath = os.path.dirname(mFilePath)
	return dirPath

#获取文件路径的文件名
def pathFileName(mFilePath):
	fileName = os.path.basename(mFilePath)
	return fileName

#创建文件夹
def makeGameDirs(mPath):
	try:
		if os.path.exists(mPath) == False:
			os.makedirs(mPath)
	except:
		print '\tmakeGameDirs :', mPath

#定义下载函数downLoadPicFromURL(网页URL, 本地文件夹)
def downLoadFromURL(url, destDir):
	try:
		urllib.urlretrieve(url, destDir)
	except:
		print '\tError retrieving the URL:', destDir

#主函数
def main():
	listLen = len(allUrl)
	for i in range(listLen):
		print  str(i) + r' / ' + str(listLen)
		filePath = joinGameDir(baseUrl, allUrl[i])
		dirPath = pathDirName(filePath)
		makeGameDirs(dirPath)
		downLoadFromURL(allUrl[i], filePath)
	print r'success'

#运行
if __name__ == "__main__":
    main()
