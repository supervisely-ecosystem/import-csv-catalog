<div align="center" markdown>
<img src="https://imgur.com/hJPOgeu.png"/>


# Import CSV catalog

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#How-To-Use">How To Use</a> •
  <a href="#Results">Results</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/import-csv-catalog)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-csv-catalog)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/import-csv-catalog&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/import-csv-catalog&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/import-csv-catalog&counter=runs&label=runs&123)](https://supervise.ly)

</div>

# Overview

Application creates Supervisely images project from csv catalog

Application key points:  
- Name of the `csv` file determines created project name
- Each product from the catalog will be assigned to class `product` with appropriate product id(number) tag
- Product info will be stored in `object properties` -> `Data`


# How to Use
1. Add [Import CSV catalog](https://ecosystem.supervise.ly/apps/import-csv-catalog) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/import-csv-catalog" src="" width="350px" style='padding-bottom: 20px'/>  

2. Run app from the context menu of the 'csv' file:

<img src="" width="100%"/>

# Results

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your project will be available. Click on the project name to proceed to it.

<img src=""/>
