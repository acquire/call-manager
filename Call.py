import uuid

class Call:
    id = uuid.uuid4()
    #we are assuming that calls objects created are straight after the call
    #todo: make now the default, but ultimately let the user choose
    call_datetime = None
    subject = None
    conversation = None