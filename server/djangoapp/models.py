from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    Name = models.CharField(null=False, max_length=30, default='car maker')
    Description = models.CharField(null=False, max_length=30, default='they make cars')
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.Name + " " + self.Description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    Type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default=SEDAN  # You can set a default value if needed
    )
    Make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    Name = models.CharField(null=False, max_length=30, default='car')
    DealerId = models.AutoField(primary_key=True)
    year = models.DateField()
    def __str__(self):
        return self.year + " " + self.Make + " " + self.Name + " " + self.Type + " " + self.DealerId
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
