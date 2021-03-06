from typing import List, Optional, Union, Dict

from slack_sdk.models.attachments import Attachment
from slack_sdk.models.blocks import Block, Option, OptionGroup
from slack_sdk.models.views import View

from slack_bolt.context.ack.internals import _set_response
from slack_bolt.response.response import BoltResponse


class Ack:
    response: Optional[BoltResponse]

    def __init__(self):
        self.response: Optional[BoltResponse] = None

    def __call__(
        self,
        text: Union[str, dict] = "",  # text: str or whole_response: dict
        blocks: Optional[List[Union[dict, Block]]] = None,
        attachments: Optional[List[Union[dict, Attachment]]] = None,
        response_type: Optional[str] = None,  # in_channel / ephemeral
        # block_suggestion / dialog_suggestion
        options: Optional[List[Union[dict, Option]]] = None,
        option_groups: Optional[List[Union[dict, OptionGroup]]] = None,
        # view_submission
        response_action: Optional[str] = None,  # errors / update / push / clear
        errors: Optional[Dict[str, str]] = None,
        view: Optional[Union[dict, View]] = None,
    ) -> BoltResponse:
        return _set_response(
            self,
            text_or_whole_response=text,
            blocks=blocks,
            attachments=attachments,
            response_type=response_type,
            options=options,
            option_groups=option_groups,
            response_action=response_action,
            errors=errors,
            view=view,
        )
