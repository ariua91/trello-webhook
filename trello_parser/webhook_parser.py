# ### Hacking

# import json
# import os

# fnames = os.listdir('1. API Samples')

# out_dict = {}

# for fn in fnames:
#     with open('1. API Samples/' + fn, 'rb') as f:
#         out_dict[fn[:-5]] = json.load(f)

# for key in out_dict:
#     print "ACTION:",
#     print out_dict[key]['action']['date']

#     ['action']['type'], ',',
#     print out_dict[key]['action']['display']['translationKey']
#     try:
#         # print 'LIST:',
#         # print out_dict[key]['action']['data']['list']['name']
#         # print "BOARD",
#         print out_dict[key]['action']['display']['entities']['board']['text']
#     except:
#         pass


### actual code


###### TEST VARS


APP_KEY = '3678d6f937ac6be6301722abf145346e'
OAUTH_SECRET ='2c5428ac1381397372115f496165b9abfe1e5b6fcd7d3868eab16eb016141fbe'
TOKEN = 'f70f81c6193fa801e250a3784a944838a384159bc99c6ab10b2983dfc713bed8'

WEBHOOK_ID = '5a74a3098797871d458f0658'

BOARD_ID_VF_SPRINT = '5ab5d305038a6e067da0522c'

LIST_ID_QA_BACKLOG = '5a74a3357d8821f3f770f51d' # QA BACKLOG
LIST_ID_PASSED_QA = '5bd46ed4a5feb12d90ad9c9b' # PASSED QA


###### PRODUCTION VARS


class webhook_item(object):
    def __init__(self, raw_json):
        """
        Accepts the raw POST from Trello, parses it if appropriate
        """
        self.raw_json = raw_json
        self.model_id = self.raw_json['model']['id']
        self.action_type = self.raw_json['action']['display']['translationKey']

        if self.model_id == WEBHOOK_ID:
            # Catch the cards moved from VF SPRINT
            if self.action_type == 'action_move_card_to_board' and\
               self.raw_json['action']['data']['boardSource']['id'] ==\
               BOARD_ID_VF_SPRINT:
                self.status = 'PR Submitted'
                self.parse_basic(raw_json)


            elif self.action_type == 'action_move_card_from_list_to_list':
                # Catch the cards moved from ANY OTHER LIST to QA BACKLOG
                if self.raw_json['action']['data']['listAfter']['id'] ==\
                   LIST_ID_QA_BACKLOG:
                    self.status = 'Merged'
                    self.parse_basic(raw_json)

                # Catch the cards moved from ANY OTHER LIST to PASSED QA
                elif self.raw_json['action']['data']['listAfter']['id'] ==\
                     LIST_ID_PASSED_QA:
                    self.status = 'Passed QA'
                    self.parse_basic(raw_json)

    def parse_basic(self, raw_json):
        """
        Basic parsing generic to all webhooks, saves to db
        """
        self.action_date = raw_json['action']['date']
        self.action_by = raw_json['action']['display']['entities']['memberCreator']['text']

        self.card_name = raw_json['action']['data']['card']['name']
        self.card_shortlink = raw_json['action']['data']['card']['shortLink']
        self.save_to_db()

    def save_to_db(self):
        """
        Saves data to db
        """
        return(
            self.status,
            self.card_name,
            self.card_shortlink,
            self.action_by,
            self.action_date,
        )
