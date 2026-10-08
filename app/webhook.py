import hmac
import hashlib

import logging
from fastapi import APIRouter, Header, HTTPException, Request

from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter()



def signature_is_valid(body: bytes, signature_header: str) -> bool:
    if not settings.github_webhook_secret:
        logger.error("GITHUB_WEBHOOK_SECRET is ot set")
        return False

    if not signature_header:
        return False

    digest = hmac.new(
        settings.github_webhook_secret.encode(), body, hashlib.sha256
    ).hexdigest()

    expected = "sha256=" + digest
    
    return hmac.compare_digest(expected.encode(), signature_header.encode())



@router.post("/webhook")
async def received_webhook(request: Request, 
                           x_github_event: str = Header(default=""), 
                           x_hub_signature_256: str = Header(default="")):

    body = await request.body()

    if not signature_is_valid(body, x_hub_signature_256):
        logger.warning("Webhook Rejected: Bad Signature")
        raise HTTPException(status_code=401, detail="Invalid signature")

    logger.info("Webhook received: event=%s", x_github_event)
    return {"message": "received"}
