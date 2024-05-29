from abc import ABC, abstractmethod

# Abstraction: Restaurant is an abstract class with the abstract method calculate_revenue()
class Restaurant(ABC):
    def __init__(self, name, daily_revenue):
        self._name = name
        self._daily_revenue = daily_revenue

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    def display_name(self):
        print(f"Restaurant name: {self._name}")

    @abstractmethod
    def calculate_revenue(self, num_days):
        pass  # Implementation must be provided by subclasses

# Inheritance: FineDiningRestaurant inherits from Restaurant
class FineDiningRestaurant(Restaurant):
    def __init__(self, name, daily_revenue, rating):
        super().__init__(name, daily_revenue)
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value

    def display_rating(self):
        print(f"Restaurant rating: {self._rating}")

    # Polymorphism: Different implementation of calculate_revenue for FineDiningRestaurant
    def calculate_revenue(self, num_days, tip_percentage=0.15):
        base_revenue = self._daily_revenue * num_days
        tip_amount = self._daily_revenue * tip_percentage * num_days
        total_revenue = base_revenue + tip_amount
        print(f"Total revenue for {num_days} days: ₱{base_revenue:.2f}")
        print(f"Total revenue for {num_days} days (including tips): ₱{total_revenue:.2f}")

# Inheritance: FastFoodRestaurant inherits from Restaurant
class FastFoodRestaurant(Restaurant):
    def __init__(self, name, daily_revenue, is_open_24_hours):
        super().__init__(name, daily_revenue)
        self._is_open_24_hours = is_open_24_hours

    @property
    def is_open_24_hours(self):
        return self._is_open_24_hours

    @is_open_24_hours.setter
    def is_open_24_hours(self, value):
        self._is_open_24_hours = value

    def display_opening_hours(self):
        if self._is_open_24_hours:
            print("Restaurant is open 24 hours.")
        else:
            print("Restaurant has regular opening hours.")

    # Polymorphism: Different implementation of calculate_revenue for FastFoodRestaurant
    def calculate_revenue(self, num_days):
        hours_per_day = 24 if self._is_open_24_hours else 16
        total_hours = num_days * hours_per_day
        total_revenue = self._daily_revenue * total_hours
        print(f"Total revenue for {num_days} days based on {hours_per_day} hours per day: ₱{total_revenue:.2f}")
        
# Demonstrating the modified classes
fine_dining_restaurant = FineDiningRestaurant("Eat in Style", 5500, 4.5)
fine_dining_restaurant.display_name()
fine_dining_restaurant.display_rating()
fine_dining_restaurant.calculate_revenue(6)

fast_food_restaurant = FastFoodRestaurant("Crunchies Fast Food", 2750, False)
fast_food_restaurant.display_name()
fast_food_restaurant.display_opening_hours()
fast_food_restaurant.calculate_revenue(7)
