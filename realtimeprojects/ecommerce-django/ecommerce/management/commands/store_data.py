from ecommerce.models import Product
from django.core.management import BaseCommand # type: ignore

class Command(BaseCommand):
    help="Inserted data"
    def handle(self,*args,**options:any):
        products= [
               
            {
               "id": 1,
               "product_name": "Wireless Mouse",
               "category": "Electronics",
               "price": 499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/wireless_mouse.jpg"
             },
             {
               "id": 2,
               "product_name": "Bluetooth Headphones",
               "category": "Electronics",
               "price": 1999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.6,
               "is_trending": True,
               "image": "https://example.com/images/bluetooth_headphones.jpg"
             },
             {
               "id": 3,
               "product_name": "Smart LED TV",
               "category": "Electronics",
               "price": 18999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.7,
               "is_trending": True,
               "image": "https://example.com/images/smart_tv.jpg"
             },
             {
               "id": 4,
               "product_name": "Gaming Keyboard",
               "category": "Electronics",
               "price": 2199,
               "quantity":10,
               "in_stock": False,
               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/gaming_keyboard.jpg"
             },
             {
               "id": 5,
               "product_name": "USB-C Hub",
               "category": "Electronics",
               "price": 899,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": False,
               "image": "https://example.com/images/usb_hub.jpg"
             },
             {
               "id": 6,
               "product_name": "Laptop Stand",
               "category": "Electronics",
               "price": 699,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.4,
               "is_trending": True,
               "image": "https://example.com/images/laptop_stand.jpg"
             },
             {
               "id": 7,
               "product_name": "Webcam HD",
               "category": "Electronics",
               "price": 1499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/webcam.jpg"
             },
             {
               "id": 8,
               "product_name": "Portable Speaker",
               "category": "Electronics",
               "price": 2999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/portable_speaker.jpg"
             },
             {
               "id": 9,
               "product_name": "Smartphone Tripod",
               "category": "Electronics",
               "price": 599,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/tripod.jpg"
             },
             {
               "id": 10,
               "product_name": "Noise Cancelling Mic",
               "category": "Electronics",
               "price": 1099,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.6,
               "is_trending": True,
               "image": "https://example.com/images/mic.jpg"
             },
             {
               "id": 11,
               "product_name": "Running Shoes",
               "category": "Footwear",
               "price": 1299,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/running_shoes.jpg"
             },
             {
               "id": 12,
               "product_name": "Formal Shoes",
               "category": "Footwear",
               "price": 1599,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/formal_shoes.jpg"
             },
             {
               "id": 13,
               "product_name": "Sneakers",
               "category": "Footwear",
               "price": 1799,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/sneakers.jpg"
             },
             {
               "id": 14,
               "product_name": "Flip Flops",
               "category": "Footwear",
               "price": 299,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/flipflops.jpg"
             },
             {
               "id": 15,
               "product_name": "Boots",
               "category": "Footwear",
               "price": 2499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.6,
               "is_trending": True,
               "image": "https://example.com/images/boots.jpg"
             },
             {
               "id": 16,
               "product_name": "Casual Loafers",
               "category": "Footwear",
               "price": 1399,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": False,
               "image": "https://example.com/images/loafers.jpg"
             },
             {
               "id": 17,
               "product_name": "Leather Sandals",
               "category": "Footwear",
               "price": 999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/sandals.jpg"
             },
             {
               "id": 18,
               "product_name": "High Heels",
               "category": "Footwear",
               "price": 1599,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": True,
               "image": "https://example.com/images/heels.jpg"
             },
             {
               "id": 19,
               "product_name": "Slip-on Shoes",
               "category": "Footwear",
               "price": 1099,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/slipons.jpg"
             },
             {
               "id": 20,
               "product_name": "Trail Running Shoes",
               "category": "Footwear",
               "price": 1899,
               "quantity":10,
               "in_stock": False,
               "offer":20,
               "delivery":10,
               "rating": 4.4,
               "is_trending": True,
               "image": "https://example.com/images/trail_running.jpg"
             },
             {
               "id": 21,
               "product_name": "Cotton T-Shirt",
               "category": "Clothing",
               "price": 399,
               "quantity":10,
               "in_stock": False,
               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/cotton_tshirt.jpg"
             },
             {
               "id": 22,
               "product_name": "Men's Jeans",
               "category": "Clothing",
               "price": 999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": False,
               "image": "https://example.com/images/mens_jeans.jpg"
             },
             {
               "id": 23,
               "product_name": "Women's Kurti",
               "category": "Clothing",
               "price": 799,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.4,
               "is_trending": True,
               "image": "https://example.com/images/kurti.jpg"
             },
             {
               "id": 24,
               "product_name": "Hoodie",
               "category": "Clothing",
               "price": 1299,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/hoodie.jpg"
             },
             {
               "id": 25,
               "product_name": "Formal Shirt",
               "category": "Clothing",
               "price": 899,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/formal_shirt.jpg"
             },
             {
               "id": 26,
               "product_name": "Polo T-shirt",
               "category": "Clothing",
               "price": 699,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/polo.jpg"
             },
             {
               "id": 27,
               "product_name": "Track Pants",
               "category": "Clothing",
               "price": 599,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/track_pants.jpg"
             },
             {
               "id": 28,
               "product_name": "Denim Jacket",
               "category": "Clothing",
               "price": 1499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.6,
               "is_trending": True,
               "image": "https://example.com/images/denim_jacket.jpg"
             },
             {
               "id": 29,
               "product_name": "Skirt",
               "category": "Clothing",
               "price": 599,
               "quantity":10,
               "in_stock": False,
               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/skirt.jpg"
             },
             {
               "id": 30,
               "product_name": "Casual Shorts",
               "category": "Clothing",
               "price": 499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": False,
               "image": "https://example.com/images/shorts.jpg"
             },       
            {
               "id": 31,
               "product_name": "Wooden Coffee Table",
               "category": "Furniture",
               "price": 4999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.4,
               "is_trending": True,
               "image": "https://example.com/images/coffee_table.jpg"
             },
             {
               "id": 32,
               "product_name": "Office Chair",
               "category": "Furniture",
               "price": 3999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": True,
               "image": "https://example.com/images/office_chair.jpg"
             },
             {
               "id": 33,
               "product_name": "Bookshelf",
               "category": "Furniture",
               "price": 2999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/bookshelf.jpg"
             },
             {
               "id": 34,
               "product_name": "Dining Table Set",
               "category": "Furniture",
               "price": 8999,
               "quantity":10,
               "in_stock": False,
               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/dining_table.jpg"
             },
             {
               "id": 35,
               "product_name": "Shoe Rack",
               "category": "Furniture",
               "price": 1999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/shoe_rack.jpg"
             },
             {
               "id": 36,
               "product_name": "TV Unit",
               "category": "Furniture",
               "price": 5999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": True,
               "image": "https://example.com/images/tv_unit.jpg"
             },
             {
               "id": 37,
               "product_name": "Recliner Chair",
               "category": "Furniture",
               "price": 8999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.6,
               "is_trending": True,
               "image": "https://example.com/images/recliner.jpg"
             },
             {
               "id": 38,
               "product_name": "Study Table",
               "category": "Furniture",
               "price": 3499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               
               "rating": 4.4,
               "is_trending": False,
               "image": "https://example.com/images/study_table.jpg"
             },
             {
               "id": 39,
               "product_name": "Wardrobe",
               "category": "Furniture",
               "price": 10999,
               
               "in_stock": False,
               "quantity":10,
               "offer":20,

               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/wardrobe.jpg"
             },
             {
               "id": 40,
               "product_name": "Single Bed",
               "category": "Furniture",
               "price": 5999,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/single_bed.jpg"
             },
           
             {
               "id": 41,
               "product_name": "Leather Wallet",
               "category": "Accessories",
               "price": 499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": False,
               "image": "https://example.com/images/wallet.jpg"
             },
             {
               "id": 42,
               "product_name": "Sunglasses",
               "category": "Accessories",
               "price": 799,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.4,
               "is_trending": True,
               "image": "https://example.com/images/sunglasses.jpg"
             },
             {
               "id": 43,
               "product_name": "Wrist Watch",
               "category": "Accessories",
               "price": 1999,
               
               "in_stock": False,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.5,
               "is_trending": True,
               "image": "https://example.com/images/watch.jpg"
             },
             {
               "id": 44,
               "product_name": "Backpack",
               "category": "Accessories",
               "price": 1499,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/backpack.jpg"
             },
             {
               "id": 45,
               "product_name": "Cap",
               "category": "Accessories",
               "price": 299,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/cap.jpg"
             },
             {
               "id": 46,
               "product_name": "Scarf",
               "category": "Accessories",
               "price": 399,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/scarf.jpg"
             },
             {
               "id": 47,
               "product_name": "Belt",
               "category": "Accessories",
               "price": 349,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.3,
               "is_trending": True,
               "image": "https://example.com/images/belt.jpg"
             },
             {
               "id": 48,
               "product_name": "Gloves",
               "category": "Accessories",
               "price": 299,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.1,
               "is_trending": False,
               "image": "https://example.com/images/gloves.jpg"
             },
             {
               "id": 49,
               "product_name": "Hair Band",
               "category": "Accessories",
               "price": 199,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.0,
               "is_trending": False,
               "image": "https://example.com/images/hairband.jpg"
             },
             {
               "id": 50,
               "product_name": "Key Chain",
               "category": "Accessories",
               "price": 149,
               
               "in_stock": True,
               "quantity":10,
               

               "offer":20,
               "delivery":10,
               "rating": 4.2,
               "is_trending": False,
               "image": "https://example.com/images/keychain.jpg"
             }
]           
        for data in products:  
          Product.objects.create(product_name=data.get('product_name'),price=data['price'],quantity=data.get('quantity'),category=data.get('category'),rating=data['rating'],is_trending=data['is_trending'],is_stock=data.get('in_stock'),delivery=data['delivery'],offer=data['offer'])    
        self.stdout.write(self.style.SUCCESS("Completed Inserted Data"))         
             
           