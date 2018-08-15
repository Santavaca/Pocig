class OwnerConsolidator():
    def __init__(self, enriched_address):
        self.enriched_address = enriched_address

    # TODO: determine a smarter way of merging
    # this just finds the first non-null values in the list of owners
    def mergeowners(self):
        merged_first_name = ''
        merged_last_name = ''
        merged_phone = ''
        # all owner fields
        for owner in self.enriched_address[owners]:
            if not merged_first_name:
                merged_first_name = owner[first_name]
            if not merged_last_name:
                merged_last_name = owner[last_name]
            if not merged_phone:
                merged_phone = owner[phone]
        merged_owner = Owner(first_name = merged_first_name,
                             last_name = merged_last_name,
                             phone = merged_phone)
        return merged_owner