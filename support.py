import pandas as pd

def query_data(min_count, db):
    counts = pd.read_sql_query("select UserId, count(UserId) as Count \
                               from Reviews \
                               group by UserId \
                               having Count > " + str(min_count), db)

    text = pd.read_sql_query("select UserId, Text \
                               from Reviews", db)

    reviews = pd.merge(text, counts, on="UserId", how="inner")
    
    return reviews, len(reviews), len(counts)


def unique_values(reviews):
    """
    Assigns a value to each unique value passed in. The purpose
     of this is to allow for the colorization of the plot
    Returns a list the size of the number of users with a color
     value for each. 
    """
    uniqs = reviews["UserId"].unique()

    remap = {}
    for idx, uniq in enumerate(uniqs):
        remap[uniq] = idx
    return reviews["UserId"].replace(remap)