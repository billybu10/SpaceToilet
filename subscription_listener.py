# A class implementing the SubscriptionListener interface
class SubListener:
  def __init__(self, indicator):
    self.indicator = indicator

  def onItemUpdate(self, update):
    print("{time_stamp:<24}: Value{value:>6}".format(
            time_stamp=update.getValue("TimeStamp"),
            value=update.getValue("Value"))) 
    self.indicator.set_label("{value}%".format(value=update.getValue("Value")), "") 
    pass
  def onClearSnapshot(self, itemName, itemPos):
    pass
  def onCommandSecondLevelItemLostUpdates(self, lostUpdates, key):
    pass
  def onCommandSecondLevelSubscriptionError(self, code, message, key):
    pass
  def onEndOfSnapshot(self, itemName, itemPos):
    pass
  def onItemLostUpdates(self, itemName, itemPos, lostUpdates):
    pass
  def onListenEnd(self):
    pass
  def onListenStart(self):
    pass
  def onSubscription(self):
    pass
  def onSubscriptionError(self, code, message):
    pass
  def onUnsubscription(self):
    pass
  def onRealMaxFrequency(self, frequency):
    pass