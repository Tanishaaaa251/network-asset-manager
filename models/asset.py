class Asset:
    def __init__(self, name, asset_type, ip_address, location, status="active"):
        self.name = name
        self.asset_type = asset_type
        self.ip_address = ip_address
        self.location = location
        self.status = status

    def to_tuple(self):
        return (self.name, self.asset_type, self.ip_address, self.location, self.status)

    def __repr__(self):
        return (f"\n--- Asset ---"
                f"\nName     : {self.name}"
                f"\nType     : {self.asset_type}"
                f"\nIP       : {self.ip_address}"
                f"\nLocation : {self.location}"
                f"\nStatus   : {self.status}\n")