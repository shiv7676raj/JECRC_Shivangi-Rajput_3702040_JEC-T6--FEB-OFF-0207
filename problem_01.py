#E-Commerce Order Revenue Analyzer
class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        ## Write your code here and don't forget to return value.
        for i in orders:
            city = i["city"]
            amount = i["amount"]
            if city in revenue_dict:
                revenue_dict[city] += amount
            else:
                revenue_dict[city] = amount

        highest_city = None
        highest_revenue = 0
        for city in revenue_dict:
            if revenue_dict[city] > highest_revenue:
                highest_revenue = revenue_dict[city]
                highest_city = city
        
        return revenue_dict, highest_city