from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class PocketbaseCollections(str, Enum):
    """Name of Pocketbase collections (tables) for different browsers' extensions."""

    FIREFOX_ADDONS = "firefox_extensions"
    CHROME_EXTENSIONS = "chrome_extensions"


class LogType(str, Enum):
    STATUS = "status"
    RESULT = "result"


class LogTypeStatus(BaseModel):
    hostIdentifier: str
    calendarTime: str
    unixTime: int
    severity: int
    filename: str
    line: int
    message: str
    version: str


class FirefoxAddonsColumns(BaseModel):
    uid: Optional[str] = ""
    name: Optional[str] = ""
    identifier: Optional[str] = ""
    creator: Optional[str] = ""
    type_: Annotated[
        Optional[str], "`type` is a reseved keyword in Python, so we alias it to type_"
    ] = Field("", alias="type")
    version: Optional[str] = ""
    description: Optional[str] = ""
    source_url: Optional[str] = ""
    visible: Optional[str] = ""
    active: Optional[str] = ""
    disabled: Optional[str] = ""
    autoupdate: Optional[str] = ""
    location: Optional[str] = ""
    path: Optional[str] = ""

    def __name__(self):
        return PocketbaseCollections.FIREFOX_ADDONS


class ChromeExtensionsColumns(BaseModel):
    browser_type: Optional[str] = ""
    uid: Optional[str] = ""
    name: Optional[str] = ""
    profile: Optional[str] = ""
    profile_path: Optional[str] = ""
    referenced_identifier: Optional[str] = ""
    identifier: Optional[str] = ""
    version: Optional[str] = ""
    description: Optional[str] = ""
    default_locale: Optional[str] = ""
    current_locale: Optional[str] = ""
    update_url: Optional[str] = ""
    author: Optional[str] = ""
    persistent: Optional[str] = ""
    path: Optional[str] = ""
    permissions: Optional[str] = ""
    permissions_json: Optional[str] = ""
    optional_permissions: Optional[str] = ""
    optional_permissions_json: Optional[str] = ""
    manifest_hash: Optional[str] = ""
    referenced: Optional[str] = ""
    from_webstore: Optional[str] = ""
    state: Optional[str] = ""
    install_time: Optional[str] = ""
    install_timestamp: Optional[str] = ""
    manifest_json: Optional[str] = ""
    key: Optional[str] = ""

    def __name__(self):
        return PocketbaseCollections.CHROME_EXTENSIONS


class LogTypeResult(BaseModel):
    name: str
    hostIdentifier: str
    calendarTime: str
    unixTime: int
    epoch: int
    counter: int
    numerics: bool
    columns: dict[str, str] = {}
    action: str
