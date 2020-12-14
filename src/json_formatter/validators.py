#These module serve as a weak replacement of the actual development of the WebScraper, they should be changed when there's a real function to validate the Datasets
import re

# For us to validate if the Path to the Product follows UNIX pattern, it was decided to use a regex that only accepts this template:
# Start with / Then Any Letter, Number or other / - Any other Character is not accepted.
def validate_path_regex(path):
    if bool(re.search(r'^/[a-zA-Z0-9/]*$', path)):
        return "Everything is ok"
    return "Path Syntax in Dataset is not valid!"

# Function to check if there's a field in the Dataset that is "null", then return the value. If there's not a single null value, return that everything is Ok
def validate_dataset_empty_field(datafield):
    for field in datafield.keys():
        if datafield[field] == "null":
            return f"The following field is empty: {field}"
    return "Everything is ok"