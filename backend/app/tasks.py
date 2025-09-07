import email
import dramatiq
from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(url="redis://redis:6379/0")
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def send_welcome_email(username: str):
    print(f"[dramatiq] sending welcome to {username}")
