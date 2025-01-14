from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """
      Custom exception handler to standardize error responses.

      :param exc: The exception instance raised during the view's execution.
      :param context: Context information about the exception, including view and request.
      :return: Modified DRF response with standardized error structure.
    """
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError) and response is not None:
        # Flatten ValidationError response
        errors = []
        for field, messages in response.data.items():
            for message in messages:
                errors.append(f"{field}: {message}")

        response.data = {
            "detail": errors[0] if len(errors) == 1 else errors, # Return list of errors if it's more than one or single error as string
            "status": response.status_code
        }

    return response
