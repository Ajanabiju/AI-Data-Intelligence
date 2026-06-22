def create_product(
    startup_name,
    source_name,
    source_url,
    pricing_model="FREE"
):

    return {
        "schemaVersion": "1.0",
        "recordType": "PRODUCT",
        "source": {
            "name": source_name,
            "url": source_url
        },
        "content": {
            "startupName": startup_name,
            "pricingModel": pricing_model
        }
    }