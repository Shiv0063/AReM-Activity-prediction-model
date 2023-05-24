"# AReM-Activity-prediction-model"

- Input data:
Input RSS streams are provided in files named datasetID.csv, where ID is the progressive numeric sequence ID for each repetition of the activity performed.
In each file, each row corresponds to a time step measurement (in temporal order) and contains the following information:
avg_rss12, var_rss12, avg_rss13, var_rss13, avg_rss23, var_rss23
where avg and var are the mean and variance values over 250 ms of data, respectively.

- Target data:
Target data is provided as the containing folder name.

For each activity, we have the following parameters:
# Frequency (Hz): 20
# Clock (millisecond): 250
# Total duration (seconds): 12
