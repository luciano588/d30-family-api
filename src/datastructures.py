
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,

            },
             {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,

            },
             {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,

            }
        ]


# John Jackson
# 33 Years old
# Lucky Numbers: 7, 13, 22
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # Add a new object to an array
        if  member["id"] is None:
            member["id"] = self._generateId()
        member["last_name"]= self.last_name
        self._member.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return`
        status = ""
        try:
            for i,x in enumerate(self._members):
                if x["id"] == id:
                    self._members.pop(i)
                status = {
                    "status": "Successfully deleted member"

                }
                break
            else:
                status = False

        except:
            status = False
        
        return status

    def get_member(self, id):
        # fill this method and update the return
        member = {}
        try:
            for x in self._members:
                if x["id"] == id:
                    member = x
        except:
            member = {
                "Status": "Not Found"
            }
        
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
