from alive_progress import alive_bar
import time

items = range(1000)                  # retrieve your set of items
with alive_bar(len(items)) as bar:   # declare your expected total
    for item in items:               # iterate as usual
        # process each item
        time.sleep(0.01)
        bar(1)                        # call after consuming one item