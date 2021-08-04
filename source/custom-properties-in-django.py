# Want to support my work 🤝? https://buymeacoffee.com/vandad

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        from datetime import date

        if self.birth_date < date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < date(1965, 1, 1):
            return "Baby-boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, newValue: str):
        values = newValue.split(" ")
        self.first_name = values[0]
        self.last_name = values[-1]
