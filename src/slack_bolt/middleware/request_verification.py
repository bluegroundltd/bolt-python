from typing import Callable, Dict

from slack_bolt.request import BoltRequest
from slack_bolt.response import BoltResponse
from slack_sdk.signature import SignatureVerifier
from .middleware import Middleware
from ..logger import get_bolt_logger


class RequestVerification(Middleware):
    def __init__(self, signing_secret: str):
        self.verifier = SignatureVerifier(signing_secret=signing_secret)
        self.logger = get_bolt_logger(RequestVerification)

    def can_skip(self, payload: Dict[str, any]) -> bool:
        return payload and payload.get("ssl_check", None) == "1"

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        next: Callable[[], BoltResponse],
    ) -> BoltResponse:
        if self.can_skip(req.payload):
            return next()

        body = req.body
        timestamp = req.headers.get("x-slack-request-timestamp", "0")
        signature = req.headers.get("x-slack-signature", "")
        if self.verifier.is_valid(body, timestamp, signature):
            return next()
        else:
            self.logger.info(
                "Invalid request signature detected "
                f"(signature: {signature}, timestamp: {timestamp}, body: {body})")
            return BoltResponse(status=401, body={"error": "invalid request"})