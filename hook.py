from delegator import Delegator
from manager import Manager
import web

urls = ('/.*', 'hooks')
app = web.application(urls, globals())


class hooks:
    def POST(self):
        # Json from github
        payload = web.data()
        print
        print 'DATA RECEIVED:'
        print payload
        print
        # send payload to delegator
        delegator = Delegator(payload)
        if delegator.action:
            man = Manager(delegator.action)
            man.do()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()