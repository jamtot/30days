N = gets.to_i

if N%2==1 or N.between?(5,21)
    puts 'Weird'
else
    puts 'Not Weird'
end
