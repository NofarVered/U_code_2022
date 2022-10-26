
def parse_str_tags_to_list(tags_str: str):
    if not tags_str:
        return []
    tags = tags_str.split(" ")
    tags = [tag.lower() for tag in tags]
    return tags

def validate_category(category):
    pass