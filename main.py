# main.py

from spicy_ids import SpicyId, get_object_type, get_object_timestamp


def main() -> None:
    # test program
    ## get spicy ids
    spicy_id: SpicyId = SpicyId(obj_type="rec", length=15, timestamp=False)
    print(spicy_id)
    spicy_id_ts: SpicyId = SpicyId(obj_type="tbl", length=10, timestamp=True)
    print(spicy_id_ts)
    ## get spicy ids values
    print(get_object_type(spicy_id=spicy_id))
    print(get_object_timestamp(spicy_id=spicy_id_ts))
    return None


if __name__ == "__main__":
    main()
else:
    pass
