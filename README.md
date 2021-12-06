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
- Supports only **instances.json** from **COCO** format
- Polygons without holes are supported
- Backward compatible with [Import COCO](https://github.com/supervisely-ecosystem/import-coco)


# How to Use
1. Add [Import CSV catalog](https://ecosystem.supervise.ly/apps/import-csv-catalog) to your team from Ecosystem.

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/import-csv-catalog" src="https://imgur.com/OxqtYTS.png" width="350px" style='padding-bottom: 20px'/>  

2. Run app from the context menu of **Images Project**:

<img src="https://imgur.com/0JwLqYJ.png" width="100%"/>

# Results

After running the application, you will be redirected to the `Tasks` page. Once application processing has finished, your link for downloading will be available. Click on the `file name` to download it.

<img src="https://imgur.com/kK1wmN9.png"/>

You can also find your converted project in   
`Team Files` -> `Export to COCO` -> `<taskId>_<projectName>.tar`

<img src="https://imgur.com/CovU9Re.png"/>
