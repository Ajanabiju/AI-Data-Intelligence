def create_startup(
    name,
    source_name,
    source_url,
    employee_count=None
):

    return {
        "schemaVersion": "1.0",
        "recordType": "STARTUP",
        "source": {
            "name": source_name,
            "url": source_url
        },
        "content": {
            "entityName": name,
            "data": {
                "employeeCount": employee_count
            }
        }
    }