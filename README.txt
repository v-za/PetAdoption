----------- HOW TO START VIRTUALENV on WINDOWS ------------------------------------

1) First, Make sure you have python installed to your PC:
	
	a) First, download the zip folder in "tahirtall-patch-1" branch to your PC and unzip it to Desktop
	b) Launch your command prompt.
	c) type: 	"cd Desktop"
	 		"python get-pip.py"
			"pip install virtualenv"
			"mkdir test"
			"cd test"
			"virtualenv api"
			"cd api"
	d) Now go to: Desktop -> PetAdoption -> tahirtall-patch-1 -> api
	e) Copy all the files inside the api folder.
	f) Paste it into Desktop -> test -> api
	g) type:	".\Scripts\activate"
			"pip install Flask"
			"pip install connexion"
			"pip install flask_sqlalchemy"
			"pip install flask_marshmallow"
			"pip install -U marshmallow-sqlalchemy"
			"pip install connexion[swagger-ui]"

	h) if you want to run:
			products database:	"python products_server.py"
			userAccount database:	"python userAccount_server.py"
			adoptPets database:	"python adoptPets_server.py"
	
	i) Launch your internet browser.
	j) on the navigation box, type(for):
			products database:	"localhost:5000/api/products"
			userAccount database:	"localhost:5000/api/users"
			adoptPets database:	"localhost:5000/api/adopt"
			
			*******************************************************************************
			** Note: for some reason, on windows PCs, instead of showing the list        **
			** of all items on a new tab for each database, the browser downloads        **
			** the list as a file, and if you open up that file with a text              ** 
			** editor, you will be able to display the list. This does not occur on Mac. **
			*******************************************************************************
	k) IMPORTANT: You can skip below step if you are not getting the indicated error.
		
			if you are coming across an error that is similar to this: "sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) unable to open database file"
			Do:
				1) "Open the appropriate "thedatabase"_models.py file with a text editor
				2) Locate "sqlite_url" variable.
				3) Delete everything after the "=" sign and copy/paste this 'sqlite:///Desktop/test/api/adopt.db' (with the quotations)
				4) Save the file and step j.
			

------------------------------------------ HOW TO START VIRTUALENV on MacOS ---------------------------------------

1) First, Make sure you have python installed to your macbook:
	
	a) First, download the zip folder in "tahirtall-patch-1" branch to your PC and unzip it to Desktop
	b) Launch your terminal.
	c) type:	"sudo easy_install pip"
			"sudo pip install virtualenv"
			"cd ~/Desktop"
			"mkdir test"
			"cd test"
			"virtualenv api"
			"cd api"
			"source bin/activate"
			"pip install Flask"
			"pip install connexion"
			"pip install flask_sqlalchemy"
			"pip install flask_marshmallow"
			"pip install -U marshmallow-sqlalchemy"
			"pip install connexion[swagger-ui]"
	d) if you want to run:
			products database:	"python products_server.py"
			userAccount database:	"python userAccount_server.py"
			adoptPets database:	"python adoptPets_server.py"

	e) Launch your internet browser.
	f) on the navigation box, type(for):
			products database:	"localhost:5000/api/products"
			userAccount database:	"localhost:5000/api/users"
			adoptPets database:	"localhost:5000/api/adopt"