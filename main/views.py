from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime, timezone

# Create your views here.
@api_view(['GET'])
def me(request):
    try:
        # Get random cat fact
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()  # Raise for bad responses
        data_fact = response.json()
        cat_fact = data_fact.get("fact", "No cat fact found")

    # Connection error
    except requests.exceptions.ConnectionError:
        cat_fact = "Error: Unable to connect to the cat fact service."
    # Timeout error
    except requests.exceptions.Timeout:
        cat_fact = "Error: The request to the cat fact service timed out."
    # HTTP error
    except requests.exceptions.HTTPError as http_err:
        cat_fact = f"HTTP error occurred: {http_err}"
    # Any other request error
    except requests.exceptions.RequestException:
        cat_fact = "An error occurred while fetching the cat fact."

    # ✅ This part should be *outside* the try/except
    response_data = {
        "status": "success",
        "user": {
            "email": "zyusuf957@gmail.com",
            "name": "Zainab Yusuf",
            "stack": "Python/Django",
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cat_fact": cat_fact
    }

    return Response(response_data, content_type="application/json")


@api_view(['GET'])
def home(request):
    return redirect("me")