<div align="center" markdown>
<img src="https://imgur.com/7cEkX6w.jpg"/>


# CSV Products Catalog to Images Project

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#Demo-Video">Demo Video</a> •
    <a href="#Demo-Data">Demo Data</a> •
  <a href="#Results">Results</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/supervisely-ecosystem/import-csv-catalog)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-csv-catalog)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/import-csv-catalog.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/import-csv-catalog.png)](https://supervisely.com)

</div>

# Overview

Application converts **.CSV catalog** [**(example)**](https://github.com/supervisely-ecosystem/import-csv-catalog/releases/download/v0.0.1/test_snacks_catalog.csv) to Supervisely Images Project

Application key points:  
- `.CSV` required fields: **image_url**, **product_id**
- `.CSV` delimeter is **comma**
- Сan contain several rows for same **product_id**
- Each images from the catalog will be labeled by class `product` with appropriate **product_id** tag
- Additional fields will be stored in `object properties` -> `Data`
- Can upload products without URL ([example](https://github.com/supervisely-ecosystem/import-csv-catalog/releases/download/v1.0.7/without_URL_example.csv)) 


# How to Run
1. Add [CSV Products Catalog to Images Project](https://ecosystem.supervisely.com/apps/import-csv-catalog) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/import-csv-catalog" src="https://imgur.com/NxeAATL.png" width="350px" style='padding-bottom: 20px'/>  

2. Run app from the context menu of the `.CSV` file:

<img src="https://i.imgur.com/8s9IREE.png" width="100%"/>


# Demo Data

- [.CSV table to import example](https://github.com/supervisely-ecosystem/import-csv-catalog/releases/download/v0.0.1/test_snacks_catalog.csv) — table example

# Demo Video
<a data-key="sly-embeded-video-link" href="https://www.youtube.com/watch?v=CbE5l_ObuhQ" data-video-code="CbE5l_ObuhQ">
    <img src="https://i.imgur.com/0fhnAB7.png" alt="SLY_EMBEDED_VIDEO_LINK"  width="70%">
</a>

# Results

After running the application, you will be redirected to the `Tasks` page.  
Once application processing has finished, your project will be available.  
Click on the project name to proceed to it.

<img src="https://i.imgur.com/G4BOKH4.png"/>


