Data is from http://build.kiva.org/docs/data/snapshots

kiva_ds_json.zip downloaded, unzipped, and run through [jshon](http://kmkeen.com/jshon/) so that humans can make sense of it too.

# Notes about this data

Kiva loans in an array. Each array item is a loan. Within each loan there are other repeating items.

There are 3502 loans split between the seven JSON files.

## Fields with some varience

$ ack -h "\"delinquent\":" | sort | uniq
   "delinquent": null,
   "delinquent": true,

$ ack -h "\"status\":" | sort | uniq
   "status": "defaulted",
   "status": "deleted",
   "status": "inactive",
   "status": "inactive_expired",
   "status": "paid",
   "status": "refunded",
   "status": "reviewed",


$ ack -h "\"activity\":" | sort | uniq
   "activity": "Agriculture",
   "activity": "Air Conditioning",
   "activity": "Animal Sales",
   "activity": "Arts",
   "activity": "Auto Repair",
   "activity": "Bakery",
   "activity": "Barber Shop",
   "activity": "Beauty Salon",
   "activity": "Bicycle Repair",
   "activity": "Bicycle Sales",
   "activity": "Blacksmith",
   "activity": "Bookstore",
   "activity": "Bricks",
   "activity": "Butcher Shop",
   "activity": "Cafe",
   "activity": "Call Center",
   "activity": "Carpentry",
   "activity": "Catering",
   "activity": "Cattle",
   "activity": "Cereals",
   "activity": "Charcoal Sales",
   "activity": "Cheese Making",
   "activity": "Child Care",
   "activity": "Cloth & Dressmaking Supplies",
   "activity": "Clothing Sales",
   "activity": "Clothing",
   "activity": "Cobbler",
   "activity": "Computers",
   "activity": "Construction Supplies",
   "activity": "Construction",
   "activity": "Consumer Goods",
   "activity": "Cosmetics Sales",
   "activity": "Crafts",
   "activity": "Dairy",
   "activity": "Decorations Sales",
   "activity": "Education provider",
   "activity": "Electrical Goods",
   "activity": "Electrician",
   "activity": "Electronics Repair",
   "activity": "Electronics Sales",
   "activity": "Embroidery",
   "activity": "Entertainment",
   "activity": "Farm Supplies",
   "activity": "Farming",
   "activity": "Fish Selling",
   "activity": "Fishing",
   "activity": "Flowers",
   "activity": "Food Market",
   "activity": "Food Production/Sales",
   "activity": "Food Stall",
   "activity": "Food",
   "activity": "Fruits & Vegetables",
   "activity": "Fuel/Firewood",
   "activity": "Furniture Making",
   "activity": "Games",
   "activity": "General Store",
   "activity": "Goods Distribution",
   "activity": "Grocery Store",
   "activity": "Hardware",
   "activity": "Health",
   "activity": "Higher education costs",
   "activity": "Home Appliances",
   "activity": "Home Products Sales",
   "activity": "Hotel",
   "activity": "Internet Cafe",
   "activity": "Jewelry",
   "activity": "Knitting",
   "activity": "Laundry",
   "activity": "Liquor Store / Off-License",
   "activity": "Livestock",
   "activity": "Manufacturing",
   "activity": "Medical Clinic",
   "activity": "Metal Shop",
   "activity": "Milk Sales",
   "activity": "Mobile Phones",
   "activity": "Motorcycle Transport",
   "activity": "Movie Tapes & DVDs",
   "activity": "Music Discs & Tapes",
   "activity": "Musical Performance",
   "activity": "Natural Medicines",
   "activity": "Office Supplies",
   "activity": "Paper Sales",
   "activity": "Party Supplies",
   "activity": "Patchwork",
   "activity": "Perfumes",
   "activity": "Personal Housing Expenses",
   "activity": "Personal Medical Expenses",
   "activity": "Personal Products Sales",
   "activity": "Personal Purchases",
   "activity": "Pharmacy",
   "activity": "Phone Accessories",
   "activity": "Phone Repair",
   "activity": "Phone Use Sales",
   "activity": "Photography",
   "activity": "Pigs",
   "activity": "Plastics Sales",
   "activity": "Poultry",
   "activity": "Primary/secondary school costs",
   "activity": "Printing",
   "activity": "Property",
   "activity": "Pub",
   "activity": "Quarrying",
   "activity": "Recycled Materials",
   "activity": "Recycling",
   "activity": "Religious Articles",
   "activity": "Renewable Energy Products",
   "activity": "Restaurant",
   "activity": "Retail",
   "activity": "Rickshaw",
   "activity": "Secretarial Services",
   "activity": "Services",
   "activity": "Sewing",
   "activity": "Shoe Sales",
   "activity": "Soft Drinks",
   "activity": "Souvenir Sales",
   "activity": "Spare Parts",
   "activity": "Tailoring",
   "activity": "Taxi",
   "activity": "Textiles",
   "activity": "Timber Sales",
   "activity": "Transportation",
   "activity": "Traveling Sales",
   "activity": "Upholstery",
   "activity": "Used Clothing",
   "activity": "Used Shoes",
   "activity": "Vehicle Repairs",
   "activity": "Vehicle",
   "activity": "Veterinary Sales",
   "activity": "Water Distribution",
   "activity": "Weaving",
   "activity": "Wholesale",

 $ ack -h "\"sector\":" | sort | uniq
   "sector": "Agriculture",
   "sector": "Arts",
   "sector": "Clothing",
   "sector": "Construction",
   "sector": "Education",
   "sector": "Entertainment",
   "sector": "Food",
   "sector": "Health",
   "sector": "Housing",
   "sector": "Manufacturing",
   "sector": "Personal Use",
   "sector": "Retail",
   "sector": "Services",
   "sector": "Transportation",
   "sector": "Wholesale",

$ ack -h "\"repayment_interval\":" | sort | uniq
    "repayment_interval": "At end of term",
    "repayment_interval": "Irregularly",
    "repayment_interval": "Monthly",
    "repayment_interval": null,

 $ ack -h "\"repayment_term\":" | sort | uniq
    "repayment_term": 10,
    "repayment_term": 11,
    "repayment_term": 12,
    "repayment_term": 13,
    "repayment_term": 14,
    "repayment_term": 15,
    "repayment_term": 16,
    "repayment_term": 17,
    "repayment_term": 18,
    "repayment_term": 19,
    "repayment_term": 20,
    "repayment_term": 21,
    "repayment_term": 22,
    "repayment_term": 23,
    "repayment_term": 24,
    "repayment_term": 25,
    "repayment_term": 26,
    "repayment_term": 27,
    "repayment_term": 28,
    "repayment_term": 3,
    "repayment_term": 30,
    "repayment_term": 32,
    "repayment_term": 38,
    "repayment_term": 39,
    "repayment_term": 4,
    "repayment_term": 43,
    "repayment_term": 5,
    "repayment_term": 50,
    "repayment_term": 6,
    "repayment_term": 7,
    "repayment_term": 72,
    "repayment_term": 8,
    "repayment_term": 9,
    "repayment_term": null,

 There are more fields to analyze. Those listed above were after a quick analysis.