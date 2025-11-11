* used TypedDict from typing to create a clear data structure for a return type
    of to\_dict() function
* I should never implement __dict__ manually - Python does that automatically,
    for simple data structures.
* __dict__ should never be used in cases when the data type is complex, has private attributes, has object attributes.
* __dict__ should be used when all attributes are public and are JSON serializable
* when creating instances of TypedDict I should create it like a normal dictionary
* TypedDict are supposed to be used as type hints
* TypedDict cannot be checked for with isinsatnce() and issubclass()
* using datetime module for date implementation
* using dt.datetime.strptime(string, "%Y-%m-%d").date() to extract a date from a string representation of dt.date instance
* when using pandas to transform a df into a dictionary with DataFrame.to\_dict(), use orient="records" to get a list of dictionaries (colnames : vals)
* convert dates in dfs using df["date"] = pd.to\_datetime(df["date"], format="%Y-%m-%d")
* when comparing pandas series or numpy arrays (or bitwise operations) use '&' and '|' instead of 'and' and 'or'
* pandas cannot convert a dictionary which does not has an iterable as value into a dataframe
* pandas has a parameter "errors" in functions like pd.to\_datetime(errors=), and when i do pd.to\_datetime(df["date"], errors="coerce") if the date is none then pandas will parse it as NaT, same goes for other conversions i guess
* monkeypatch fixture can allow for mock inputs using monkeypatch.setattr("builtins.input", lambda \_: inputs)
* when importing whole modules it is better to not pollute the namespace and "import module\_name" -- this is clean

