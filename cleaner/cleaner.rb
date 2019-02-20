require "fuzzy_match"
require 'json'
require "pry-byebug"

class Cleaner
  attr_accessor :category, :used_names
  def initialize
    @entries = []
    @used_names = {}
  end

  def call
    get_entries
    clean_entries
    ensure_entry_name_correctness
    remove_duplicate_entries
    export_json
  end

  def ensure_entry_name_correctness
    all_names = JSON.parse(File.read("./names/names_item_all.json")).map {|entry| entry["name"]}
    matcher = FuzzyMatch.new(all_names)

    @entries.each do |entry|
      unless all_names.include? entry.name
        correct_name = matcher.find_best(entry.name).first
        puts "#{entry.name}, replaced with #{correct_name}"
        entry.name = correct_name
      end

      if @used_names[entry.name]
        @used_names[entry.name] << entry
      else
        @used_names[entry.name] = [entry]
      end 
      
    end
  end

  def remove_duplicate_entries
    entries_to_be_removed = []
    
    @used_names.each do |key, array|
      if array.count > 1
        best_entry = array.reduce do |acc, elem|
          acc.prices.count > elem.prices.count ? acc : elem
        end

        entries_to_be_removed = array.select do |candidate_entry|
          candidate_entry != best_entry
        end

        @entries = @entries.select do |entry|
          !entries_to_be_removed.include?(entry)
        end
        
        puts "removed dupe from #{best_entry.name}"
      end
    end
  end

  def to_json
    @entries.map(&:to_json)
  end  

  private

    def clean_entries
      @entries.map(&:clean)
    end

    def export_json
      File.write("fredrick_data.json", JSON.pretty_generate(self.to_json))
    end

    def get_entries
      Dir.glob("./export/**").each do |category_dir| # Get each categorical folder
        Dir.glob("#{category_dir}/**").each do |entry_dir| # Get all entries from categorical folders
          category = entry_dir.split("/")[-2]
          number = entry_dir.split("/")[-1]

          @entries << Entry.new(category, number)
        end
      end
    end
end

class Entry
  attr_accessor :category, :number, :name, :prices
  def initialize(category, number)
    @category = category
    @number = number
    @name
    @prices = []
  end

  def clean
    get_clean_name
    get_clean_prices
  end

  def to_json
    {
      name: @name,
      prices: @prices
    }
  end  

  private

    def filepath
      "./export/#{@category}/#{number}"
    end

    def get_clean_name
      @name = File.read("#{filepath}/name.txt").strip
    end

    def get_clean_prices
      @prices = File.read("#{filepath}/data.txt")
                    .scan(/of (\d*.*) m/)
                    .flatten
                    .map{|h| h.gsub(/,/, "").to_i }
                    .reverse # So the newest entries come at the end. When uploading to database, the newest entries are created last and therefore the newest
    end
end

c = Cleaner.new.call