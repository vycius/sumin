#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gtfs_functions as gtfs

routes, stops, stop_times, trips, shapes = gtfs.import_gtfs("data/gtfs/gtfs-lt-all.zip", busiest_date = True)

cutoffs = [0,6,9,15,19,22,24]
line_freq = gtfs.lines_freq(stop_times, trips, shapes, routes, cutoffs = cutoffs)

gtfs.map_gdf(line_freq, )


# In[ ]:





# In[ ]:




