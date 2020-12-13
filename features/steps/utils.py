
def validate_path_regex(path):
    if path:
        return "Path Syntax in Dataset is not valid!"
    return "Path Syntax in Dataset is not valid!"

def validate_dataset_empty_field(datafield):
    if datafield["vendor"] == '""':
        return "The following field is empty: Vendor"
    elif datafield["url"] == '""':
        return "The following field is empty: URL"
    elif datafield["series"] == '""':
        return "The following field is empty: Series"
    elif datafield["category"] == '""':
        return "The following field is empty: Category"
    elif datafield["model"] == '""':
        return "The following field is empty: Model"
    elif datafield["path"] == '""':
        return "The following field is empty: Path"
    elif datafield["release"] == '""':
        return "The following field is empty: Release"