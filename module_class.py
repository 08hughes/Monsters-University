class Module:

    module_list = []

    def __init__(self, subject, duration):
        self.subject = subject
        self.duration = duration
        Module.module_list.append(self.subject)


    @classmethod
    def list_modules(cls):
        return Module.module_list
