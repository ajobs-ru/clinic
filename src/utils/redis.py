import hashlib
import json

import redis.asyncio as aioredis

from config import REDIS_URL
from utils import helpers

redis = aioredis.from_url(REDIS_URL)


async def set_value(value, timeout=None):
    key = helpers.random_hex(16)
    await redis.set(key, value, ex=timeout)
    return key


async def get_value(key):
    value = await redis.get(key)
    return value.decode("utf-8") if value else None


async def set(key, value, timeout=None):
    return await redis.set(key, value, ex=timeout)


async def get(key):
    value = await get_value(key)
    return helpers.auto_cast(value)


def cache(prefix, ttl=600):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            cache_key = f"{prefix}:{func.__name__}:{hashlib.md5(json.dumps([args, kwargs], sort_keys=True).encode()).hexdigest()}"

            cached_result = await redis.get(cache_key)
            if cached_result:
                return json.loads(cached_result.decode("utf-8"))

            result = await func(*args, **kwargs)

            if hasattr(result, "model_dump"):
                result = result.model_dump()

            await redis.set(cache_key, json.dumps(result), ex=ttl)

            return result

        return wrapper

    return decorator
