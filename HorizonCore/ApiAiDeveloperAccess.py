import json
import requests

DEFAULT_VERSION = '20150910'

# https://curl.trillworks.com/


class ApiAiDeveloperAccess:

    def __init__(self, developerAccessToken=None, version=DEFAULT_VERSION):
        self._developerAccessToken = developerAccessToken
        self._base_url = 'api.api.ai'
        self._version = {'v': version}
        self._headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Bearer ' + self._developerAccessToken,
        }

        self.Entities = Entities(self._base_url, self._version, self._headers)
        self.Intents = Intents(self._base_url, self._version, self._headers)

    def SetToken(self, developerAccessToken):
        self._developerAccessToken = developerAccessToken


class Entities:
    """
    The entities endpoint is used to create, retrieve, update, and delete developer-defined entity objects.

    Entity Object
    -------------
        - id
            * String
            * A unique identifier for the entity.
        - name
            * Legal Name
            * The name of the entity.
        - entries
            * Array of objects
            * An array of entry objects, which contain reference values and synonyms.
            - value
                * String
                * For mapping entities:
                    > a canonical name to be used in place of synonyms. Example: "New York"
                * For enum type entities:
                    > a string that can contain references to other entities (with or without aliases).
                    > Example: "@sys.color:color @size:size @clothes:clothes"
            - synonyms
                * Array of strings that can include simple strings (for words and phrases) or references to
                  other entites (with or without aliases).)
                * For mapping entities:
                    > an array of synonyms. Example: ["New York", "NYC", "big Apple"]
                * For enum type entities:
                    > a string that is identical to the value string.
                    > Example: "@sys.color:color @size:size @clothes:clothes"
        - isEnum
            * Boolean
            * Indicates if the entity is a mapping or an enum type entity.
        - automatedExpansion
            * Boolean
            * Indicates if the entity can be automatically expanded.

    Array of Entity Entry Objects
    -----------------------------
        - value
            * String
            * For mapping entities:
                > a reference value.
            * For enum type entities:
                > a string that can contain references to other entities (with or without aliases).
        - synonyms
            * Array of strings
            * For mapping entities:
                > an array of synonyms.
            * For enum type entities:
                > a string that is identical to the value string.
    """

    def __init__(self, base_url, version, headers):
        self._base_url = base_url
        self._version = version
        self._headers = headers

    def GetEntities(self):
        """
        Retrieves a list of all entities for the agent.

        :return: The response will be a JSON object with the following fields:
            - entities
                * Array of objects
                * An array of entity description objects
            - id
                * String
                * ID of the entity
            - name
                * String
                * Name of the entity
            - count
                * int
                * The total number of synonyms in the entity
            - preview
                * String
                * A string that contains summary information about the entity
            - status (
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.get(
            "https://api.api.ai/v1/entities",
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def GetEntity(self, entityId):
        """
        Retrieves the specified entity.

        :param entityId: is the ID of the entity to retrieve. You can specify the entity by its name instead of its ID.
        :return: The response is an entity object.
        """
        response = requests.get(
            "https://api.api.ai/v1/entities/%s" % entityId,
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def CreateEntity(self, entity):
        """
        Creates a new entity.

        :param entity: The POST body is an entity object without the "id", "isEnum", and "automatedExpansion" elements.
        :return: response has the following fields:
            - id
                * String
                * The ID of the new entity.
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.post(
            "https://api.api.ai/v1/entities",
            data=json.dumps(entity),
            # data=entity,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def AddEntityEntries(self, entityId, entries):
        """
        Adds an array of entity entries to the specified entity.

        :param entityId: is the ID of the entity to which the entries will be added. You can specify the
           entity by its name instead of its ID.
        :param entries: The POST body is an array of entity entry objects in JSON format.
        :return: None
        """
        response = requests.post(
            "https://api.api.ai/v1/entities/%s/entries" % entityId,
            data=json.dumps(entries),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def UpdateEntity(self, entity):
        """
        Creates or updates an array of entities.

        :param entity: The PUT body consists of an array of entity objects without the "id", "isEnum", and
            "automatedExpansion" elements.
        :return: None
        """
        response = requests.put(
            "https://api.api.ai/v1/entities",
            data=json.dumps(entity),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def UpdateEntityWithId(self, entityId, entity):
        """
        Updates the specified entity.

        :param entityId:  is the ID of the entity to update. You can specify the entity by its name instead of its ID.
        :param entity: The PUT body is an entity object.
        :return:
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.put(
            "https://api.api.ai/v1/entities/%s" % entityId,
            data=json.dumps(entity),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def UpdateEntityEntries(self, entityId, entries):
        """
        Updates an array of entity entries in the specified entity.

        :param entityId: is the ID of the entity in which entries will be updated. You can specify the entity by
            its name instead of its ID.
        :param entries: The PUT body is an array of entity entry objects in JSON format.
        :return: None
        """
        response = requests.put(
            "https://api.api.ai/v1/entities/%s/entries" % entityId,
            data=json.dumps(entries),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def DeleteEntity(self, entityId):
        """
        Deletes the specified entity.

        :param entityId: is the ID of the entity to delete. You can specify the entity by its name instead of its ID.
        :return:
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.delete(
            "https://api.api.ai/v1/entities/%s" % entityId,
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def DeleteEntityEntries(self, entityId, entryReferenceValueNames):
        """
        Deletes an array of entity entries from the specified entity.
        
        :param entityId: is the ID of the entity from which entries will be deleted. You can specify the entity by
            its name instead of its ID.
        :param entryReferenceValueNames: The DELETE body is an array of strings corresponding to the reference values of
            entity entries to be deleted.
        :return: None
        """
        response = requests.delete(
            "https://api.api.ai/v1/entities/%s/entries" % entityId,
            data=json.dumps(entryReferenceValueNames),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)


class Intents:
    """
    The intents endpoint is used to create, retrieve, update, and delete intent objects.

    Intents convert a number of user expressions or patterns into an action. An action is
    essentially an extraction of the user command or sentence semantics.

    Intent object
    -------------
        - id
            * String
            * A unique identifier for the intent.
        - name
            * String
            * The name of the intent.
        - auto
            * Boolean
            * true if Machine learning is on in this intent.
            * false if Machine learning is off in this intent.
        - contexts
            * Array of legal names
            * A list of contexts required in order for this intent to be triggered (input contexts).
        - templates
            * Array of strings
            * Array of templates this intent will match. Each template is a string that may contain legal names
              corresponding to words and phrases, entity names prefixed with @, accompanied or not by aliases. In
              addition to alphanumerical characters, it may contain the symbols ? and ,.
        - userSays
            * Array of objects
            * Each object corresponds to one example/template from the 'User says' field in the UI.
            - id
                * String
                * The id of the example/template.
            - data
                * Array of objects
                * Information about the text of the example/template and its annotation.
                - text
                    * String
                    * Text corresponding to the entire example/template (for examples without annotation and templates) or
                      to one of example's parts (only for annotated examples).
                - meta
                    * String
                    * Entity name prefixed with @. This field is required for the annotated part of the text and applies only
                      to examples.
                - alias
                    * Legal name
                    * Parameter name for the annotated part of example.
                - userDefined
                    * Boolean
                    * true if the text was annotated by developer.
                    * false in the case of automatic annotation.
            - isTemplate
                * Boolean
                * true for template mode.
                * false for example mode.
            - count
                * Number
                * Equals to n-1 where n indicates how many times this example/template was added to this intent.
        - responses
            * Array of objects
            * A list of responses for this intent.
            - action
                * Legal name
                * The name of the action.
            - resetContexts
                * Boolean
                * true indicates that all contexts will be reset when this intent is triggered. Otherwise the value is false.
            - affectedContexts
                * Array of objects
                * A list of contexts that are activated when this intent is triggered (output contexts).
                - name
                    * Legal name
                    * The name of the context.
                - lifespan
                    * Number
                    * Indicates the number of requests the context will be active until expired.
            - parameters
                * Array of objects
                * A list of parameters for the action.
                - name
                    * Legal name
                    * The name of the parameter.
                - value
                    * String
                    * The value of the parameter. It can be:
                        > a constant string
                        > a variable defined as the parameter name prefixed with $. Example: $date
                        > original value defined as $parameter_name.original
                        > a value from a context defined as #context_name.parameter_name
                - defaultValue
                    * String
                    * Default value to use when the "value" field returns an empty value.
                    * Default value can be extracted from a context by using the format #context_name.parameter_name.
                - required
                    * Boolean
                    * true if the action cannot be completed without collecting this parameter value. false otherwise.
                - dataType
                    * String
                    * Entity name prefixed with @. This field is mandatory if the parameter is required.
                - prompts
                    * Array of strings
                    * Questions that the agent will ask in order to collect a value for a required parameter.
                - isList
                    * Boolean
                    * If true, the parameter value will be returned as a list.
                    * If false, the parameter value can be a string, number, or object.
            - messages
                * Array of objects
                * Agent response corresponding to the 'Response' field in the UI. Array of message objects
            - defaultResponsePlatforms
                * Array of strings
                * Strings correspond to the messaging platform names for which the "Use response from the
                DEFAULT tab as the first response." option is enabled.
        - priority
            * Number
            * Intent priority.
        - webhookUsed
            * Boolean
            * true if webhook is enabled in the agent and in the intent. false otherwise.
        - webhookForSlotFilling
            * Boolean
            * true if webhook is enabled for the intent required parameters. false otherwise.
        - fallbackIntent
            *Boolean
            * true if this is a fallback intent. false if it is a regular intent.
        - cortanaCommand
            * Object
            * Object containing optional values for Cortana integration.
            - navigateOrService
                * String
                * "NAVIGATE" – for a page that the app should navigate to when it launches
                * "SERVICE" – for an app service name that must handle voice command.
            - target
                * String
                * Page or service name.
        - events
            * Array
            * Array containing event objects.
            - name
                * String
                * Event name.

    MESSAGE OBJECTS
    ===============

    Text response message object
    ----------------------------
    - type
        * Number
        * Equals to 0 for the Text response message type.
    - platform
        * String
        * Messaging platform name (only those for which rich messages are supported).
    - speech
        * String or Array
        * Agent's text response(s). String in case of one variation per one 'Text response' element, array of strings
          in case of multiple variations. Line breaks (\n) are currently supported for Facebook Messenger, Kik, Slack,
          and Telegram one-click integrations.

    Image message object
    --------------------
    - type
        * Number
        * Equals to 3 for the Image message type.
    - platform
        * String
        * Messaging platform name (only those for which rich messages are supported).
    - imageUrl
        * String
        * Public URL to the image file.

    Card message object
    -------------------
    - type
        * Number
        * Equals to 1 for the Card message type.
    - platform
        * String
        * Messaging platform name (only those for which rich messages are supported).
    - title
        * String
        * Card title.
    - subtitle
        * String
        * Card subtitle.
    - buttons
        * Array
        * Array of objects corresponding to card buttons.
        - text
            * String
            * Button text.
        - postback
            * String
            * A text sent back to API.AI or a URL to open.

    Quick replies message object
    ----------------------------
    - type
        * Number
        * Equals to 2 for the Quick replies message type.
    - platform
        * String
        * Messaging platform name (only those for which rich messages are supported).
    - title
        * String
        * Quick replies title. Required for the Facebook Messenger, Kik, and Telegram one-click integrations.
    - replies
        * Array
        * Array of strings corresponding to quick replies.

    Custom payload message object
    -----------------------------
    - type
        * Number
        * Equals to 4 for the Custom payload message type.
    - platform
        * String
        * Messaging platform name (only those for which rich messages are supported).
    - payload
        * Object
        * Developer defined JSON. It is sent without modifications.
    """

    def __init__(self, base_url, version, headers):
        self._base_url = base_url
        self._version = version
        self._headers = headers

    def GetIntents(self):
        """
        Retrieves a list of all intents for the agent.

        :return: The response will be a JSON object that is an array of objects with the following fields:
            - id
                * String
                * ID of the intent.
            - name
                * String
                * Name of the intent.
            - contextIn
                * Array of legal names
                * List of input contexts. These contexts serve as a prerequisite for this intent to be triggered.
            - contextOut
                * Array of legal names
                * List of output contexts that are set after this intent is executed.
                - name
                    * String
                    * The name of the output context.
                - lifespan
                    * Number
                    * The number of queries this context will remain active after being invoked.
            - actions
                * Array of strings
                * List of actions set by all responses of this intent.
            - parameters
                * Array of objects
                * List of parameters for the action.
                - name
                    * Legal name
                    * The name of the parameter.
                - value
                    * String
                    * The value of the parameter.
                - defaultValue
                    * String
                    * The default value of the parameter that should be returned when the "value" field returns an empty value.
                - required
                    * Boolean
                    * true if the action cannot be completed without collecting this parameter value. false otherwise.
                - dataType
                    * String
                    * Entity name prefixed with @. This field is mandatory if the parameter is required.
                - prompts
                    * Array of strings
                    * Questions that the agent will ask in order to collect a value for a required parameter.
            - priority
                * Number
                * Intent priority.
            - fallbackIntent
                * Boolean
                * true if this is a fallback intent. false if it is a regular intent.
        """
        response = requests.get(
            "https://api.api.ai/v1/intents",
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def GetIntent(self, intentId):
        """
        Retrieves the specified intent.

        :param intentId: is the ID of the intent to retrieve.
        :return: The response is an intent object.
        """
        response = requests.get(
            "https://api.api.ai/v1/intents/%s" % intentId,
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def CreateIntent(self, intent):
        """
        Creates a new intent.

        :param intent: The POST body is an intent object without the "id" element.
        :return: response has the following fields:
            - id
                * String
                * The ID of the new intent.
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.post(
            "https://api.api.ai/v1/intents",
            data=json.dumps(intent),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def UpdateIntent(self, intentId, intent):
        """
        Updates the specified intent.
        
        :param intentId: is the ID of the intent to update.
        :param intent: The PUT body is an intent object.
        :return:
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.put(
            "https://api.api.ai/v1/intents/%s" % intentId,
            data=json.dumps(intent),
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)

    def DeleteIntent(self, intentId):
        """
        Deletes the specified intent.

        :param intentId: is the ID of the intent to delete.
        :return:
            - status
                * Status object
                * Contains data on how the request succeeded or failed.
        """
        response = requests.delete(
            "https://api.api.ai/v1/intents/%s" % intentId,
            data=None,
            params=self._version,
            headers=self._headers)
        response.raise_for_status()
        return json.loads(response.content)
