# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent)
tip_cost = meal_cost / 100 * tip_percent
tax_cost = meal_cost / 100 * tax_percent
puts (meal_cost+tip_cost+tax_cost+0.5).to_i
end

meal_cost = gets.to_f

tip_percent = gets.to_i

tax_percent = gets.to_i

solve meal_cost, tip_percent, tax_percent
