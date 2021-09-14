class command:
    def __init__(self,name,fac,feature):
        self.name = name
        self.fac = fac
        self.feature = feature

    def feature_introduce(self):
        print(self.feature)

router_ospf_100 = command("ospf","cisco","configure_router")

router_ospf_100.feature_introduce()
