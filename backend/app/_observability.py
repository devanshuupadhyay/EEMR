# backend/app/_observability.py
import os
import logging
import sys

import structlog
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


def init_structlog():
    """
    Configure Structlog for structured JSON logging.
    """
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logger = structlog.get_logger()
    logger.info("Structlog initialized")
    return logger


def init_sentry(app: FastAPI):
    """
    Initialize Sentry only if SENTRY_DSN is provided in environment.
    """
    dsn = os.getenv("SENTRY_DSN")
    if dsn:
        sentry_sdk.init(
            dsn=dsn,
            traces_sample_rate=1.0  # adjust in production
        )
        app.add_middleware(SentryAsgiMiddleware)
        print("[Observability] Sentry initialized")
    else:
        print("[Observability] Sentry not configured (SENTRY_DSN missing)")


def init_prometheus(app: FastAPI):
    """
    Instrument FastAPI with Prometheus metrics.
    Exposes /metrics endpoint automatically.
    """
    instrumentator = Instrumentator()
    instrumentator.instrument(app).expose(app)
    print("[Observability] Prometheus metrics exposed at /metrics")


def init_tracing(app: FastAPI):
    """
    Initialize OpenTelemetry tracing and instrument FastAPI app.
    Exports spans to console.
    """
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    span_processor = BatchSpanProcessor(ConsoleSpanExporter())
    trace.get_tracer_provider().add_span_processor(span_processor)
    FastAPIInstrumentor.instrument_app(app)
    print("[Observability] OpenTelemetry tracing initialized")
