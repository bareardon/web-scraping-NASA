# Import dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Set up app
app = Flask(__name__)

# Set up PyMongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Set up routes
@app.route("/")
def index():
    # Write a statement that finds all the items in the db and returns them
    mars_data = mongo.db.mars_data.find_one()
    print("MARS DATA", mars_data)
    # Render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars_data = mars_data)

@app.route("/scrape")
def scrape():
    # Write a statement that finds all the items in the db and returns them
    mars_data = mongo.db.mars_data

    # Run the scrape function
    mars = scrape_mars.scrape()
    print("MARS DATA", mars)

    # Update the Mongo database using update and upsert=True
    mars_data.update(
        {}, 
        mars, 
        upsert=True
    )

    # Redirect back to index page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
