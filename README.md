

## A static site using pelican

<a href="https://scientist-tortoise-12030.netlify.com/" target="_blank">Live site</a>

[Live site](https://scientist-tortoise-12030.netlify.com/)

### instructions: 


Create virtualenv using the requirements.txt

Put contents in content/ folder. 

To build site. 

	$pelican content


Run server:

	$cd output/
	$ python -m pelican.server


If use fab:

	pip install Fabric

	fab build

	fab regenerate  # watch for changes

	fab serve

The site will be running at http://localhost:8000/

