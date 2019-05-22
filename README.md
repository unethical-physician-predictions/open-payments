# Open payments

This is the code for the paper [**Predicting Unethical Physician Behavior At Scale: A Distributed Computing Framework** (link to be updated)](https://www.google.com).

For information regarding how to run the code on an EC2 instance check the [documentation (link to be updated)](https://www.google.com).

# Abstract

As the amount of publicly shared data increases, developing a robust pipeline to stream, store and process data is critical, as the casual user often lacks the technology, hardware and/or skills needed to work such voluminous data. In this research, the authors employ Amazon EC2 and EMR, MongoDB, and Spark MLlib to explore 28.5 gigabytes of CMS Open Payments data in an attempt to identify physicians who may have a high propensity to act unethically, owing to significant transfers of wealth from medical companies. A Random Forest Classifier is employed to predict the top decile of physicians who have the highest risk of unethical behavior in the following year, resulting in an F-Score of 91\%. The authors also employ an anomaly detection algorithm that correctly identified a high-profile case of a physician leaving his prestigious position, failing to disclose anomalously-large transfers of wealth from medical companies.

# Introduction

Sectors that deal with vast amounts of public data, such as healthcare, have long held the potential to unlock untold mysteries about the populations they serve. Until recently, the amount of data available for analysis far outstripped the abilities of both the technology and machine learning algorithms necessary to extract actionable information. Very recent advances in data and computational science have allowed researchers to tap into and identify patterns and relationships hidden in this sea of data. In healthcare, this leap has facilitated the identification of issues, both clinical and administrative, throughout the healthcare continuum.

Often times, medical research is focused on the clinical, owing to the high salaries of physicians, significant costs of procedures for patients, the costly operation of medical facilities, and the relatively limited amount of data required for well-scoped medical studies, e.g., a study on hypertension. However, recent advances have enabled researchers to comb through the  vast amounts of data associated with medical administration.

A salient facet of healthcare administration is the interconnected nature of the companies who provide medical supplies, devices and drugs to the physicians who use and/or prescribe the aforementioned products. There are several examples supporting the hypothesis that a physician receiving disproportionately large transfers of wealth or value from an organization, may be more inclined, persuaded, or outright fraudulent in concluding that certain medication, procedures, or medical devices are more effective than they truly are. Such payments or transfers of value have been formally linked to unethical physician and/or institutional behavior. However, the ability to apply machine learning algorithms at scale to analyze all physicians receiving transfers of wealth has been elusive. The casual user often lacks the technology, hardware and/or skills needed to work with such voluminous data. The authors have therefore established a robust pipeline to stream, store and process  Open Payments data from the Center for Medicare \& Medicaid Services (CMS), analyzing all payments or other transfers of value from group purchasing organizations (GPOs) and device and drug manufacturers to physicians or research institutions.

# Methodology

Cloud computing, MapReduce and Apache Spark, and Amazon Web Services were employed to create models for physicians earnings classification and detect annomalies in specific payments.

The data was stored in S3 and processed using MapReduce and Apache Spark on EMR clusters with different technical specifications. Timings and evaluation metrics (if applicable) were reported.

# Results

On Audit List:

| Master/Slave Config | \# Slaves | Memory | Cores | Run Time | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
|c3.8xlarge | 4 | 60GB | 32 | 22m23s |
|c3.8xlarge | 2 | 60GB | 32 | 37m12s |
|m4.xlarge | 8 | 16GB  | 4  | 37m43s |
|m4.xlarge | 4 | 16GB  | 4  | 64m13s |
|m4.xlarge | 2 | 16GB  | 4  | n/a |

On Anomaly Detection:

| Master/Slave Config | \# Slaves | Memory | Cores | Run Time | Data | 
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| c3.8xlarge | 10 | 60GB | 32 | 81m | Research |
| c3.8xlarge | 6 | 60GB | 32 | 118m | Research |
| c3.8xlarge | 2 | 60GB | 32 | 165m | Research |
| c3.8xlarge | 10 | 60GB | 32 | 1201m | Physician |
