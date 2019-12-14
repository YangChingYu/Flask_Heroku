from flask import Flask

app=Flask(__name__)
#現在要執行的模組

@app.route("/")
def home():
	return "Hello Flask"

@app.route("/test")#我們要處理的網站路徑
def test():
	return "This is test2"


if __name__ =="__main__":
	app.run()
#在這邊起動伺服器
