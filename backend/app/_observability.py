# backend/app/_observability.py
import os
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

def init_sentry(app):
    """
    Initialize Sentry only if SENTRY_DSN is provided in environment.
    """
    dsn = os.getenv("SENTRY_DSN")
    if dsn:
        sentry_sdk.init(
            dsn=dsn,
            traces_sample_rate=1.0,  # adjust in production
        )
        app.add_middleware(SentryAsgiMiddleware)
        print("[Observability] Sentry initialized")
    else:
        print("[Observability] Sentry not configured (SENTRY_DSN missing)")
