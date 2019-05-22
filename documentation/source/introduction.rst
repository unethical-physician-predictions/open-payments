Predicting Unethical Physician Behavior At Scale: A Distributed Computing Framework
===================================================================================
As the amount of publicly shared data increases,
developing a robust pipeline to stream, store and process data is critical, as the casual user often lacks the technology, hardware 
and/or skills needed to work with such voluminous data. Inthis research, the authors employ Amazon EC2 and EMR, MongoDB, 
and Spark MLlib to explore 28.5 gigabytes of CMS Open Payments data in an attempt to identify physicians who may have a high propensity 
to act unethically, owing to significanttransfers of wealth from medical companies. 
A Random ForestClassifier is employed to predict the top decile of physicians whohave the highest risk 
of unethical behavior in the following year,resulting in an F-Score of 91%. 
The data is also analyzed byan anomaly detection algorithm that correctly identified a high-profile case 
of a physician leaving his prestigious position, ashe failed to disclose anomalously-large transfers of wealth from medical companies.
