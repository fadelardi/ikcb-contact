import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# @app.route(route="httpget", methods=["GET"])
# def http_get(req: func.HttpRequest) -> func.HttpResponse:
#     name = req.params.get("name", "World")

#     logging.info(f"Processing GET request. Name: {name}")

#     return func.HttpResponse(f"Hello, {name}!")

@app.route(route="contact", methods=["POST"])
def contact(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        name = req_body.get('name')
        email = req_body.get('email')
        subject = req_body.get('subject')
        msg = req_body.get('message')
        
        logging.info(f"Processing POST request. Name: {name}, Email: {email}, Subject: {subject}, Message: {msg}")

        if name and isinstance(name, str) and email and isinstance(email, int) and msg and isinstance(msg, str):
            if not subject:
                subject = "No Subject"
            return func.HttpResponse(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {msg}", status_code=200)
        else:
            return func.HttpResponse(
                "Mandatory fields 'name', 'email', 'message' are missing from request body.",
                status_code=400
            )
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON in request body",
            status_code=400
        )
