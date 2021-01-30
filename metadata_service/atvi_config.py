from typing import List
from metadata_service.entity.badge import Badge
from metadata_service.config import LocalConfig

class AtviConfig(LocalConfig):
    WHITELIST_BADGES: List[Badge] = [
        Badge(badge_name='partition column',
            category='column'),
    ]
