* used TypedDict from typing to create a clear data structure for a return type
    of to\_dict() function
* I should never implement __dict__ manually - Python does that automatically,
    for simple data structures.
* __dict__ should never be used in cases when the data type is complex, has private attributes, has object attributes.
* __dict__ should be used when all attributes are public and are JSON serializable
* when creating instances of TypedDict I should create it like a normal dictionary
* TypedDict are supposed to be used as type hints
