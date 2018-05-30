class Commands:
    def __init__(self):
        self.state = False

    async def action(self, msg, args):
        return True

    @staticmethod
    async def help(msg):
        return ""

    def done(self):
        self.state = True

    async def executed(self):
        self.state = True
        return self.state
