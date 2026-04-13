import json

# user_data_array = [json.load(file) for file in uploaded_files]

def verify(person_json:list):
    errors = []
    warnings = []
    if type(person_json[0]) == list:
        errors.append("Name entry is missing")
    elif type(person_json[0]) != str:
        errors.append("Name entry is of invalid type. Must be str")
    elif person_json[0] == '':
        errors.append("Name entry is empty")
    
    if ('' in person_json):
        warnings.append("File contains empty strings")
    
    def test_schedule_entries(entry:list):
        errors = []
        if len(entry) <= 2:
            errors.append("Schedule entry is of incorrect length")
            return errors
        if type(entry[0]) != list or type(entry[1]) != list:
            errors.append("Clock entries are of invalid type")
        if len(entry[0]) != 2 or len(entry[1]) != 2:
            errors.append("Clock entries are of incorrect length. Must be list of length 2")
        if any(day not in 'MTWRF' for day in entry[2]) or type(entry[2]) != str:
            errors.append("Invalid day string")
        return errors
    
    for entry in person_json[1:]:
        errors = errors + test_schedule_entries(entry)
    
    return errors, warnings


if __name__ == "__main__":
    testFile = json.load(open(r"C:\Users\abrah\.__Scheduler App Data__\Abby.json", 'r'))
    print(testFile)
    print(verify(testFile))