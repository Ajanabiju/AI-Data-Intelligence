def create_job(
    company,
    date,
    is_remote=False,
    role_family="Engineering"
):

    return {
        "schemaVersion": "1.0",
        "recordType": "JOB",
        "content": {
            "company": company,
            "date": date,
            "is_remote": is_remote,
            "role_family": role_family
        }
    }