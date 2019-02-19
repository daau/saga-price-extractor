require "fuzzy_match"
require 'json'
require "pry-byebug"

f = File.read("./chair_names.json")
chair_json = JSON.parse(f)


chair_names = []

chair_json.each do |hash|
  chair_names << hash["name"]
end

matcher = FuzzyMatch.new(chair_names)

json = []

Dir.entries("./chairs").select {|f| !File.directory? f}.each do |dir|
  name = File.read("./chairs/#{dir}/name.txt").strip
  prices = File.read("./chairs/#{dir}/data.txt").scan(/of (\d*.*) m/).map{|arr| arr.first}.map{|h| h.gsub(/,/, "").to_i }
  json << {"#{name}": prices}
end

File.write("chair_prices.json", JSON.pretty_generate(json))

binding.pry
puts "lol"