# spicy_ids/generate_timestamp_value.py

from datetime import datetime, timezone

from spicy_ids.utils import logger


def get_unix_time() -> int:
    tz_utc: timezone = timezone.utc
    curr_ts: datetime = datetime.now(tz=tz_utc)
    unix_epoch: datetime = datetime(year=1970, month=1, day=1, tzinfo=tz_utc)
    epoch_ts: int = int((curr_ts - unix_epoch).total_seconds())
    logger.debug(f"{epoch_ts = }")
    return epoch_ts


def mask_timestamp(ts: float) -> str:
    masked_ts: int = ts * 4024
    ts_to_str: str = str(masked_ts)
    logger.debug(f"{masked_ts = }; {len(ts_to_str)}")
    return ts_to_str


def get_masked_ts() -> str:
    curr_ts: int = get_unix_time()
    return mask_timestamp(ts=curr_ts)
