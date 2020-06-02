class TriggerSystem:
    """
    Class to manage a collection of triggers. Triggers may be
    registered with an instance of this class. The instance then 
    takes care of updating those triggers and of removing them from
    the system if their lifetime has expired.
    """
    def __init__(self):
        self._triggers = []

    def UpdateTriggers(self):
        """
        This method iterates through all the triggers present in the system and
        calls their Update method in order that their internal state can be
        updated if necessary. It also removes any triggers from the system that
        have their m_bRemoveFromGame field set to true.
        """
        for trigger in self._triggers:
            if trigger.IsToBeRemoved():
                self._triggers.remove(trigger)
            else:
                trigger.Update()

    def TryTriggers(self, entities):
        """
        This method iterates through the container of entities passed as a
        parameter and passes each one to the Try method of each trigger *provided*
        the entity is alive and provided the entity is ready for a trigger update.
        :param entities:
        """
        # Test each entity against the triggers
        for entity in entities:
            # An entity must be ready for its next trigger update
            # before it is tested against each trigger.
            if entity.IsReadyForTriggerUpdate():
                for trigger in self._triggers:
                    trigger.Try(entity)

    def Clear(self):
        """
        This deletes any current triggers and empties the trigger list
        """
        self._triggers = []

    def Update(self, entities):
        """
        This method should be called each update-step of the game. It will first
        update the internal state of the triggers and then try each entity against
        each active trigger to test if any should be triggered.
        :param entities:
        """
        self.UpdateTriggers()
        self.TryTriggers(entities)

    def Register(self, trigger):
        """
        This is used to register triggers with the TriggerSystem (the TriggerSystem
        will take care of tidying up memory used by a trigger)
        :param trigger:
        """
        self._triggers.append(trigger)

    def GetTriggers(self):
        return self._triggers
