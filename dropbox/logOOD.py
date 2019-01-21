#requirement.
# different level of log. error, customized message , event warning
# maybe with diff storage ways.
# level can be set on runtime.
# one subject can subscribe multiple logger
# one logger can listen to many subject

# Observer pattern


#simple example

# class ObserverbleObject:
#     def __init__(self):
#         self._observers=[]
#     def registerObserver(self  , observer ):
#         self._observers.append(observer)
#     def unregisterObserver(self , observer):
#         self._observers.remove(observer)
#     def notifyObserver(self , *args , **kwargs):
#         for ob in self._observers:
#             ob.notify(self , *args , **kwargs)
# class Observer:
#     def __init__(self , ObserverbleObject):
#         ObserverbleObject.registerObserver(self)
#     def notify(self , ObserverbleObject  , *args , **kwargs):
#

# https://zh.wikipedia.org/wiki/%E8%A7%82%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F
class Observerable:
    def __init__(self):
        self.listeners=[]
    def register(self , listener):
        self.listeners.append(listener)
    def deregister(self , listerner):
        self.listeners.remove(listerner)
    def notify_listeners(self , event):
        for listener in self.listeners:
            listener.notify(self , event)
class Listener:
    def __init__(self , name , subject):

        self.name=name
        subject.register(self)
    def notify(self  , subject , event):
        #do things
        print(self.name+ "received event "+event+ ' fromm '+str(subject))

class Subject(Observerable):
    def __init__(self):
        super().__init__()
        self.data=None
    def getUserAction(self):
        self.data = input('Enter something to do:')
        return self.data

if __name__=="__main__":
    # make a subject object to spy on
    subject = Subject()

    # register two listeners to monitor it.
    listenerA = Listener("<listener A>", subject)
    listenerB = Listener("<listener B>", subject)

    # simulated event
    subject.notify_listeners("<event 1>")
    # outputs:
    #     <listener A> received event <event 1>
    #     <listener B> received event <event 1>

    action = subject.getUserAction()
    subject.notify_listeners(action)
    #Enter something to do:hello
    # outputs:
    #     <listener A> received event hello
    #     <listener B> received event hello

