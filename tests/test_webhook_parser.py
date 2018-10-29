import pytest
import json

from trello_parser.webhook_parser import *


def webhook_json_parse(raw_json_file):
    '''Return a webhook_item from raw_json_file'''
    with open(raw_json_file, 'rb') as f:
        return webhook_item(json.load(f))


@pytest.mark.parametrize('test_json, action_type, action_date,\
action_by, card_name, card_shortlink', [
    ('tests/sample json/move_to_board.json',
     'action_move_card_to_board',
     '2018-10-27T02:26:00.630Z',
     'Arianto',
     '2 card',
     'EQCbbXUt'
    ),
    ('tests/sample json/move_within_board(list_c).json',
     'action_move_card_from_list_to_list',
     '2018-10-27T02:07:51.347Z',
     'Arianto',
     'this is a new card [add some score]',
     'aYSk4ijP',
    ),
    ('tests/sample json/move_within_board(passed_qa).json',
     'action_move_card_from_list_to_list',
     '2018-10-27T13:58:55.103Z',
     'Arianto',
     'hi',
     'sxaTMsJx',
    )
])

def test_parse(test_json,action_type,action_date,action_by,card_name,card_shortlink):
    webhook = webhook_json_parse(test_json)
    print dir(webhook)
    assert webhook.action_type == action_type
    assert webhook.action_date == action_date
    assert webhook.action_by == action_by
    assert webhook.card_name == card_name
    assert webhook.card_shortlink == card_shortlink
