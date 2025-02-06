from typing import Optional

from pydantic import BaseModel


class SchemasBase(BaseModel):
    cronjob: Optional[str] = None
