#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask, render_template


# In[ ]:


from flask_pymongo import PyMongo
import requests
from splinter import Browser


# In[ ]:


app = Flask(__name__)


# In[ ]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[ ]:


@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[ ]:


@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run()


# In[ ]:





# In[ ]:




