require "fuzzy_match"
require 'json'
require "pry-byebug"

class Category
  attr_accessor :category, :names
  def initialize(category)
    @category = category
    @names = []

    get_names
  end

  def get_names
    j = JSON.parse(File.read("./names_item_s.json"))
    j.each do |entry|
      names << hash["name"]
    end
  end
end

# f = File.read("./names_item_s.json")
# chair_json = JSON.parse(f)


# chair_names = []

# chair_json.each do |hash|
#   chair_names << hash["name"]
# end

binding.pry

matcher = FuzzyMatch.new(chair_names)

json = []

Dir.entries("./raw_data/chairs").select {|f| !File.directory? f}.each do |dir|
  name = File.read("./raw_data/chairs/#{dir}/name.txt").strip
  prices = File.read("./raw_data/chairs/#{dir}/data.txt").scan(/of (\d*.*) m/).map{|arr| arr.first}.map{|h| h.gsub(/,/, "").to_i }
  json << {"#{name}": prices}
end

File.write("scroll_prices.json", JSON.pretty_generate(json))

binding.pry
puts "lol"