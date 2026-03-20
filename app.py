from pymongo import MongoClient
import time
import random

# Подключение к mongos
client = MongoClient('localhost', 27017)
db = client.app_db
collection = db.ratings

def create_user_rating(user_id, rating, date):
    """Добавить оценку пользователя"""
    result = collection.insert_one({
        'user_id': user_id,
        'rating': rating,
        'date': date
    })
    print(f"Добавлено: user_id={user_id}, rating={rating}, date={date}")

def find_by_user(user_id):
    """Подсчет записей по user_id"""
    start = time.time()
    result = list(collection.find({'user_id': user_id}))
    elapsed = time.time() - start
    print(f"Поиск по user_id={user_id}: найдено записей: {len(result)}, время: {elapsed:.4f} сек")
    return result

def find_by_rating(rating):
    """Подсчет записей по rating"""
    start = time.time()
    result = list(collection.find({'rating': rating}))
    elapsed = time.time() - start
    print(f"Поиск по rating={rating}: найдено записей: {len(result)}, время: {elapsed:.4f} сек")
    return result

def main():
    while True:
        print("\n=== MongoDB Sharding Demo ===")
        print("1. Добавить оценку")
        print("2. Подсчет записей по user_id")
        print("3. Подсчет записей по rating")
        print("4. Общее число записей")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            user_id = int(input("user_id: "))
            rating = int(input("rating (1-5): "))
            date = input("date (YYYY-MM-DD): ")
            create_user_rating(user_id, rating, date)
        
        elif choice == '2':
            user_id = int(input("user_id: "))
            find_by_user(user_id)
        
        elif choice == '3':
            rating = int(input("rating (1-5): "))
            find_by_rating(rating)
        
        elif choice == '4':
            total = collection.count_documents({})
            print(f"\nВсего записей в коллекции: {total}")
                   
        elif choice == '5':
            print("До свидания!")
            break

if __name__ == "__main__":
    print("Подключение к MongoDB...")
    main()