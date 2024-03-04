__copyright__ = "Copyright (c) 2018 Alex Laird"
__license__ = "MIT"

import logging

from django.db import models

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    """
    The abstract base model from which most other models should inherit to ensure common base attributes.
    """

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
