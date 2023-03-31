from collections import defaultdict


subscribers = defaultdict(list)


def map_event(event_type: str, function: callable):
    subscribers[event_type].append(function)
    

def publish_event(event_type: str):
    if not event_type in subscribers:
        return
    
    for function in subscribers[event_type]:
        function()
