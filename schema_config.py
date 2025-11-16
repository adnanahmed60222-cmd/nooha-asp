# Auto-generated from schema extraction - Optimized for production
SCHEMA_METADATA = {
    "display_names": {
        "email": ["emailid"],
        "phone": ["telephonenumber"],
        "mobile": ["telephonenumber"],
        "fax": ["telephonenumber"],
        "name": ["applicantname", "contactname", "productname", "companyname", "substancename", "brandname"],
        "address": ["country", "region", "inn", "inventedname"],
        "product": ["productname", "brandname", "principalproductname"],
        "application": ["applicationnumber"],
        "sequence": ["sequencenumber"],
        "status": ["status", "isactive"],
        "authority": ["healthauthority", "agencyname"],
    },
    
    "important_search_columns": {
        "applicationcontactdetails": ["applicantname", "emailid", "telephonenumber"],
        "applications": ["applicationnumber", "companyname", "healthauthority"],
        "products": ["productname", "productmanufacturername", "dosageform"],
        "sequences": ["sequencenumber", "submissionid", "status"],
        "principalproducts": ["principalproductname", "brandname"],
        "substances": ["substancename", "substancemanufacturername"],
        "templates": ["name", "structuretype"],
        "regions": ["region"],
        "countries": ["countryname", "agencyname"],
        "auditlogs": ["username", "activity"],
        "queries": ["title", "status"],
    },
    
    "sample_values": {
        "applicationcontactdetails": {
            "applicantname": ["ahila", "ahila.godbin", "abccc", "AN23"],
            "emailid": ["ahila.godbin@nooha-asp.com", "abc@gmail.com", "de@gmail.com"],
            "telephonenumber": ["01234556666", "0123654789", "08264579227"]
        },
        "applications": {
            "applicationnumber": ["000111", "000456", "000888"],
            "companyname": ["cipla", "Amneal EU, Limited"],
            "healthauthority": ["FDA", "EMA", "EUROPEAN"]
        },
        "products": {
            "productname": ["Amoxicillin Capsule", "Azithromycin 250 mg Tablets"],
            "dosageform": ["CAPSULE", "CREAM", "INJECTION"]
        },
        "sequences": {
            "sequencenumber": ["0000", "0001", "0002", "0003"],
            "status": ["DRAFT", "COMPILED", "ERRORS"]
        },
        "regions": {
            "region": ["EU", "SAHPRA", "ECOWAS", "GCC", "ROW"]
        }
    },
    
    "synonym_keywords": {
        "email": ["email", "emailid", "mail", "contact"],
        "phone": ["phone", "telephone", "telephonenumber", "mobile", "fax", "contact", "number"],
        "name": ["name", "applicant", "contact", "person", "company", "product", "substance"],
        "product": ["product", "medicine", "drug", "substance", "excipient"],
        "application": ["application", "submission", "appid", "appl"],
        "sequence": ["sequence", "seq", "submission", "file"],
        "status": ["status", "state", "active"],
    }
}

def get_search_columns_for_table(table_name):
    """Get best columns to search in for a table"""
    return SCHEMA_METADATA["important_search_columns"].get(table_name, [])

def get_sample_values_for_column(table_name, column_name):
    """Get sample values to help match user input"""
    if table_name in SCHEMA_METADATA["sample_values"]:
        return SCHEMA_METADATA["sample_values"][table_name].get(column_name, [])
    return []

def get_display_name_columns(display_name):
    """Map user-friendly names to actual column names"""
    return SCHEMA_METADATA["display_names"].get(display_name.lower(), [])

def find_synonym_matches(keyword):
    """Find what the user might mean"""
    keyword_lower = keyword.lower()
    for synonym_type, keywords in SCHEMA_METADATA["synonym_keywords"].items():
        if any(keyword_lower in k for k in keywords):
            return synonym_type
    return None
