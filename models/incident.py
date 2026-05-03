class Incident:
    def __init__(self, asset_id, description, severity, date_reported, resolved="no"):
        self.asset_id = asset_id
        self.description = description
        self.severity = severity
        self.date_reported = date_reported
        self.resolved = resolved

    def to_tuple(self):
        return (self.asset_id, self.description, self.severity, self.date_reported, self.resolved)

    def __repr__(self):
        return (f"\n--- Incident ---"
                f"\nAsset ID    : {self.asset_id}"
                f"\nDescription : {self.description}"
                f"\nSeverity    : {self.severity}"
                f"\nDate        : {self.date_reported}"
                f"\nResolved    : {self.resolved}\n")