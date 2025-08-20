def lambda_handler(event, context):
    print("Hello from Jenkins + Git + Lambda 🚀")
    return {
        "statusCode": 200,
        "body": "Lambda executed successfully!"
    }
