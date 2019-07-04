import dataset
from flask import Flask, render_template, request, redirect

app= Flask(__name__)
db = dataset.connect('sqlite:///database2.db')

bookstable= db["books"]

@app.route('/')
def loadPage():

	bookslist = list(bookstable.all())

	print bookslist ,"Here are all the books"
	return render_template(('home.html'), list = bookslist)


@app.route('/addbooks' , methods=['POST', "GET"])
def signup():
	if request.method== "POST":
		print "Books"

		bookname= request.form["bookname"]
		authorname= request.form["authorname"]
		bookscopies=request.form["bookscopies"]
		typeofbook=request.form["typeofbook"]
		print bookname, authorname, bookscopies, typeofbook

		bookstable.insert({"bookname":bookname , "authorname":authorname, "bookscopies":bookscopies, "typeofbook": typeofbook})
		# for i in bookstable:
			

		return redirect('/')

	if request.method == "GET":
		return render_template('books.html')
if __name__ == '__main__':

	app.run(port=8004 , debug= True)