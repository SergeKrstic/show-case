import json


class TrelloPrinter:

    @staticmethod
    def DisplayAllOrganizations(organizations, printList=True):
        TrelloPrinter.DisplayList(organizations, "Organizations List", printList)

    @staticmethod
    def DisplayOrganizationDetails(organization):
        if organization is not None:
            organization.fetch()
            print("Organization details:")
            TrelloPrinter.DisplayProperty("ID: " + str(organization.id))
            TrelloPrinter.DisplayProperty("Name: " + str(organization.name))
            TrelloPrinter.DisplayProperty("Description: " + str(organization.description))
            TrelloPrinter.DisplayProperty("URL: " + str(organization.url))
            print()

    @staticmethod
    def DisplayAllMembers(members, printList=True):
        TrelloPrinter.DisplayList(members, "Members List", printList)

    @staticmethod
    def DisplayMemberDetails(member):
        if member is not None:
            member.fetch()
            print("Member details:")
            TrelloPrinter.DisplayProperty("ID: " + str(member.id))
            TrelloPrinter.DisplayProperty("Full Name: " + str(member.full_name))
            TrelloPrinter.DisplayProperty("Username: " + str(member.username))
            TrelloPrinter.DisplayProperty("Status: " + str(member.status))
            TrelloPrinter.DisplayProperty("Bio: " + str(member.bio))
            TrelloPrinter.DisplayProperty("Initials: " + str(member.initials))
            TrelloPrinter.DisplayProperty("URL: " + str(member.url))
            print()

    @staticmethod
    def DisplayAllBoards(boards, printList=True):
        TrelloPrinter.DisplayList(boards, "Boards List", printList)

    @staticmethod
    def DisplayBoardDetails(board):
        if board is not None:
            board.fetch()
            print("Board details:")
            TrelloPrinter.DisplayProperty("ID: " + str(board.id))
            TrelloPrinter.DisplayProperty("Name: " + str(board.name))
            TrelloPrinter.DisplayProperty("Description: " + str(board.description))
            TrelloPrinter.DisplayProperty("Closed: " + str(board.closed))
            TrelloPrinter.DisplayProperty("DateOfLastActivity: " + str(board.date_last_activity))
            TrelloPrinter.DisplayProperty("URL: " + str(board.url))
            if hasattr(board, 'organization'):
                TrelloPrinter.DisplayProperty("Organization: " + board.organization)
            print()

    @staticmethod
    def DisplayAllLabels(labels, printList=True):
        TrelloPrinter.DisplayList(labels, "Labels List", printList)

    @staticmethod
    def DisplayLabelDetails(label):
        if label is not None:
            label.fetch()
            print("Label details:")
            TrelloPrinter.DisplayProperty("ID: " + str(label.id))
            TrelloPrinter.DisplayProperty("Name: " + str(label.name))
            TrelloPrinter.DisplayProperty("color: " + str(label.color))
            print()

    @staticmethod
    def DisplayAllList(lists, printList=True):
        TrelloPrinter.DisplayList(lists, "List", printList)

    @staticmethod
    def DisplayListDetails(trelloList):
        if trelloList is not None:
            print("List details:")
            TrelloPrinter.DisplayProperty("ID: " + str(trelloList.id))
            TrelloPrinter.DisplayProperty("Name: " + str(trelloList.name))
            TrelloPrinter.DisplayProperty("Board: " + str(trelloList.board.name))
            TrelloPrinter.DisplayProperty("Closed: " + str(trelloList.closed))
            print()

    @staticmethod
    def DisplayAllCards(cards, printList=True):
        TrelloPrinter.DisplayList(cards, "Cards List", printList)

    @staticmethod
    def DisplayCardDetails(card):
        if card is not None:
            card.fetch()
            print("Card details:")
            TrelloPrinter.DisplayProperty("ID: " + str(card.id))
            TrelloPrinter.DisplayProperty("Name: " + str(card.name))
            TrelloPrinter.DisplayProperty("Description: " + str(card.desc))
            TrelloPrinter.DisplayProperty("Closed: " + str(card.closed))
            TrelloPrinter.DisplayProperty("URL: " + str(card.url))
            TrelloPrinter.DisplayProperty("ShortUrl: " + str(card.shortUrl))
            TrelloPrinter.DisplayProperty("idMembers: " + str(card.idMembers))
            TrelloPrinter.DisplayProperty("idShort: " + str(card.idShort))
            TrelloPrinter.DisplayProperty("idList: " + str(card.idList))
            TrelloPrinter.DisplayProperty("idBoard: " + str(card.idBoard))
            TrelloPrinter.DisplayProperty("idLabels: " + str(card.idLabels))
            TrelloPrinter.DisplayProperty("labels: " + str(card.labels))
            TrelloPrinter.DisplayProperty("badges: " + str(card.badges))
            TrelloPrinter.DisplayProperty("Position: " + str(card.pos))
            TrelloPrinter.DisplayProperty("Due: " + str(card.due))
            TrelloPrinter.DisplayProperty("Dhecked: " + str(card.checked))
            TrelloPrinter.DisplayProperty("DateLastActivity: " + str(card.dateLastActivity))
            TrelloPrinter.DisplayProperty("_checklists: " + str(card._checklists))
            TrelloPrinter.DisplayProperty("_comments: " + str(card._comments))
            TrelloPrinter.DisplayProperty("_attachments: " + str(card._attachments))
            print()

    @staticmethod
    def DisplayAllWebHooks(webHooks, printList=True):
        TrelloPrinter.DisplayList(webHooks, "Web Hook List", printList)

    @staticmethod
    def DisplayWebHookDetails(webHook):
        if webHook is not None:
            print("Web Hook details:")
            TrelloPrinter.DisplayProperty("ID: " + str(webHook.id))
            TrelloPrinter.DisplayProperty("Model ID: " + str(webHook.id_model))
            TrelloPrinter.DisplayProperty("Description: " + str(webHook.desc))
            TrelloPrinter.DisplayProperty("Callback URL: " + str(webHook.callback_url))
            TrelloPrinter.DisplayProperty("Active: " + str(webHook.active))
            TrelloPrinter.DisplayProperty("Token: " + str(webHook.token))
            print()

    @staticmethod
    def PrintJsonObjectNicely(jsonObject):
        print(json.dumps(jsonObject, indent=4, sort_keys=True))

    @staticmethod
    def DisplayList(trelloList, title, printList=True):
        if printList:
            print(title + " [{}]:".format(len(trelloList)))
            for item in trelloList:
                TrelloPrinter.DisplayItem(item)
                # print(*cards, sep='\n')
            print()

    @staticmethod
    def DisplayItem(item):
        itemId = '[' + item.id
        if hasattr(item, 'name'):
            itemName = ', ' + item.name + ']'
        elif hasattr(item, 'full_name'):
            itemName = ', ' + item.full_name + ']'
        else:
            itemName = ']'

        print('  - ' + itemId + itemName)

    @staticmethod
    def DisplayProperty(trelloProperty):
        print('  ' + trelloProperty)
