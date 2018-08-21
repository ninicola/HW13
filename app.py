# import necessary libraries
from flask import Flask, render_template, redirect
import scrape_mars
import pymongo

# create instance of Flask app
app = Flask(__name__)

client=pymongo.MongoClient()
db=client.mars_db1
collection=db.mars_entry




# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
   
   mars_info=list(db.collection.find())[0]

    # return template and data
   return render_template("index.html", mars=mars_info)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():
    db.collection.remove({})
    # Run scraped functions
    mars_info = scrape_mars.scrape()
    db.collection.insert_one(mars_info)
    # surf = scrape_info.scrape_surf()

    


    # Redirect back to home page so i create a html file in template once complted call scrape and insert data into mongodb
    return render_template("scrp.html")


if __name__ == "__main__":
    app.run(debug=True)
