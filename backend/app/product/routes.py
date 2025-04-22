from fastapi import APIRouter, Depends, Query
from app.middleware import get_current_user
from app.config import settings
import requests
import logging
from typing import Optional
import math

# Enable logging to the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/products")
def get_products(
    user: dict = Depends(get_current_user),
    name: Optional[str] = Query(None, alias="name"),
    page: int = Query(1, ge=1),
    per_page: int = Query(10, alias="per_page", le=100)
):
    headers = {
        "Authorization": f"Bearer {settings.RACKBEAT_API_KEY}",
        "Accept": "application/json"
    }

    params = {
        "limit": per_page,
        "page": page
    }

    if name:
        params["name"] = name

    logger.info("Fetching products from Rackbeat...")
    logger.info(f"Headers: {headers}")
    logger.info(f"Params: {params}")

    response = requests.get(
        f"{settings.RACKBEAT_API_URL}/products",
        headers=headers,
        params=params,
    )

    logger.info(f"Request URL: {response.url}")
    response.raise_for_status()

    json_data = response.json()
    logger.info(f"res: {json_data}")
    return json_data;
