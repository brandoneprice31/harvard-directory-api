class Harvard_Person:
    def __init__(self, first_name, last_name, department, phone, residence, unit, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.phone = phone
        self.residence = residence
        self.unit = unit
        self.mail = mail

    def __str__(self):
        return '<Harvard_Person ' + self.first_name + ' ' + self.last_name + '>'
