require "fuzzy_match"
require 'json'
require "pry-byebug"

class Category
  attr_accessor :category, :names
  def initialize(category)
    @category = category
    @names = []
  end

  def call
    get_names
    match_names
  end

  def get_names
    j = JSON.parse(File.read("./names_item_s.json"))
    j.each do |entry|
      names << entry["name"]
    end
  end

  def match_names
    matcher = FuzzyMatch.new(@names)
    binding.pry
    Dir.entries("./raw_data/100%").select {|f| !File.directory? f}.each do |dir|
      name = File.read("./raw_data/100%/#{dir}/name.txt").strip
      unless @names.include? name
        result = matcher.find_best(name)
        puts "#{name}, best was #{result}"
      end
      # prices = File.read("./raw_data/chairs/#{dir}/data.txt").scan(/of (\d*.*) m/).map{|arr| arr.first}.map{|h| h.gsub(/,/, "").to_i }
      # json << {"#{name}": prices}
    end
    
    # File.write("scroll_prices.json", JSON.pretty_generate(json))
  end
end

c = Category.new("scrolls").call