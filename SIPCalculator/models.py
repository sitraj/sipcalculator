from django.db import models

class SIPCalculator(models.Model):
    initial_investment = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_investment = models.DecimalField(max_digits=10, decimal_places=2)
    annual_rate = models.DecimalField(max_digits=5, decimal_places=2)
    time_period = models.PositiveIntegerField()

    def calculate_future_value(self):
        monthly_rate = self.annual_rate / 12 / 100
        num_months = self.time_period * 12

        future_value = self.initial_investment
        for month in range(1, num_months + 1):
            future_value += self.monthly_investment
            future_value *= (1 + monthly_rate)

        future_total_investment = (self.monthly_investment * num_months) + self.initial_investment
        future_total_gain = future_value - future_total_investment
        return future_value, future_total_investment, future_total_gain

    def __str__(self):
        return f"SIP Calculator - ID: {self.id}"
