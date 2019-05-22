"""
Functions for PySpark Open Payments Data Processing
"""

def split_comma(x):
    return list(reader([x], delimiter=',', quotechar='"'))[0]

def is_na(x):
    """
    To be wrapped with udf.
    Returns 1 if the element in the column is null and 0 otherwise.
    """
    if x is not None:
        return 1
    else:
        return 0

isNa = F.udf(is_na)


def safe_double(x):
    try:
        return float(x)
    except:
        return x

safeDouble = F.udf(safe_double)

def safe_int(x):
    try:
        return int(x)
    except:
        return x

safeInt = F.udf(safe_int)

def str_to_bool(x):
    """
    To be wrapped with udf.
    Applied to a colum, maps yes/no and transform them to 1/0 respectively. Nones mapped to 0.
    """
    try:
        if x.lower()=='yes':
            return 1
        else:
            return 0
    except:
        return 0

strToBool = F.udf(str_to_bool)

def max_to_one(x):
    """
    To be wrapped with udf.
    Applied to a colum, maps yes/no and transform them to 1/0 respectively. Nones mapped to 0.
    """
    try:
        if x>1:
            return 1
        else:
            return x
    except:
        return x

maxToOne = F.udf(max_to_one)

def replace_na(x):
    """
    To be wrapped with udf.
    Applied to a colum, maps yes/no and transform them to 1/0 respectively. Nones mapped to 0.
    """
    if x is None:
        return 'blank'
    else:
        return x

replaceNA = F.udf(replace_na)

def check_blanks(x):
    try:
        if len(x)==0 or x is None:
            return 'blank'
        else: return x
    except:
        return x

checkBlankUdf = F.udf(check_blanks)

def date_to_day(x):
    """
    To be wrapped with udf.
    Extracts the day from a date in the format MM/DD/YYYY as an int.
    """
    try:
        v = x.split('/')
        return int(v[1])
    except:
        return x

dateToDay = F.udf(date_to_day)

def date_to_month(x):
    """
    To be wrapped with udf.
    Extracts the month from a date in the format MM/DD/YYYY as an int.
    """
    try:
        v = x.split('/')
        return int(v[0])
    except:
        return x

dateToMonth = F.udf(date_to_month)

def to_buckets_p(x, limits=[35.71, 112.22, 325.0]):
    """
    To be wrapped with udf.
    For Phisicians
    """
    for i,l in enumerate(limits):
        if x<l:
            return i
        else:
            return len(limits)

toBucketsP = F.udf(to_buckets_p)

def to_buckets_h(x, limits=[1866.64, 7170.82, 29388.13]):
    """
    To be wrapped with udf.
    For Hospitals
    """
    for i,l in enumerate(limits):
        if x<l:
            return i
        else:
            return len(limits)

toBucketsH = F.udf(to_buckets_h)



def showMode(df,cols):
    cols = ['Month','Day','Program_Year']
    for col in cols:
        df.groupBy(col).count().orderBy('count',ascending=False).show()

def TransformColumn(df, cols, userDefinedFunction, newCol=None):
    """
    Gets columns `cols` of `df` and applies a `userDefinedFunction`.

    If newCol dictionary is specified:
            - Won't drop cols and will add the new ones with the new name
                Format ex:

                    {'oldCol1':'newCol1','oldCol2':'newCol2',..,'oldColN':'newColN'} (N cols given)

    If newCol dictionary is not specified:
            - Will drop the old columns and substitute them by the result of the transformation.

    """
    dfNew = df
    if newCol is None:

        for i, col in enumerate(cols):
            dfNew = dfNew.withColumn('%s_idx'%col, userDefinedFunction(dfNew[col]))\
                         .drop(col)\
                         .withColumnRenamed('%s_idx'%col, col)
    else:

        for i, col in enumerate(cols):
            dfNew = dfNew.withColumn(newCol[col], userDefinedFunction(dfNew[col]))

    return dfNew

def indexStringColumns(df, cols):
    """
    Modified from ex2 of Lesson5
    """
    # variable newdf will be updated several times
    newdf = df

    labels_mapping = {}
    for c in cols:
        # For each given colum, fits StringIndexerModel.
        sm = StringIndexer(inputCol=c, outputCol=c+"-num").setHandleInvalid("keep")\
                .fit(newdf)
        # Creates a DataFame by putting the transformed values in the new colum with suffix "-num"
        # then drops the original columns and drop the "-num" suffix.
        labels_mapping[c] = sm.labels
        newdf = sm.transform(newdf).drop(c)
        newdf = newdf.withColumnRenamed(c+"-num", c)
    return newdf, labels_mapping

def oneHotEncodeColumns(df, cols, dropLast=False):
    """
    Taken from ex2 of Lesson5
    """
    newdf = df
    for c in cols:
        print(c)
        # For each given colum, create OneHotEncoder.
        # dropLast : Whether to drop the last category in the encoded vector (default: true)
        onehotenc = OneHotEncoder(inputCol=c, outputCol=c+"-onehot", dropLast=dropLast)

        newdf = onehotenc.transform(newdf).drop(c)
        newdf = newdf.withColumnRenamed(c+"-onehot", c)\

    return newdf

def permuteEntries(df):

    cols = df.columns
    dfnew = df

    print('Permuting column elemements...')
    for col in tqdm_notebook(cols):
        dfnew = df.withColumn('aux', df.select(col).orderBy(F.rand())[col],)\
                    .drop(col)\
                    .withColumnRenamed('aux',col)
    return dfnew
