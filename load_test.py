from pymongo import MongoClient
import time
import random
import statistics

# Подключение к mongos (роутеру)
client = MongoClient('localhost', 27017)
db = client.app_db
collection = db.ratings

def test_insert(n):
    """Тест вставки n записей"""
    print(f"\n=== Тест вставки {n} записей ===")
    
    start = time.time()
    
    for i in range(n):
        collection.insert_one({
            'user_id': random.randint(3000, 5000),
            'rating': random.randint(1, 5),
            'date': f"2026-03-{random.randint(1, 20)}"
        })
    
    elapsed = time.time() - start
    
    print(f"Время: {elapsed:.2f} сек")
    print(f"Скорость: {n/elapsed:.0f} записей/сек")

def test_query_by_user_id(n):
    """Тест поиска по user_id (быстрый)"""
    print(f"\n=== Тест поиска по user_id ({n} запросов) ===")
    times = []
    
    for i in range(n):
        user_id = random.randint(1, 5000)
        start = time.time()
        list(collection.find({'user_id': user_id}))
        times.append(time.time() - start)
    
    avg = statistics.mean(times)
    median = statistics.median(times)
    
    print(f"Среднее время: {avg:.4f} сек")
    print(f"Медиана: {median:.4f} сек")
    print(f"Мин: {min(times):.4f} сек")
    print(f"Макс: {max(times):.4f} сек")

def test_query_by_rating(n):
    """Тест поиска по rating (медленный)"""
    print(f"\n=== Тест поиска по rating ({n} запросов) ===")
    times = []
    
    for i in range(n):
        rating = random.randint(1, 5)
        start = time.time()
        list(collection.find({'rating': rating}))
        times.append(time.time() - start)
    
    avg = statistics.mean(times)
    median = statistics.median(times)
    
    print(f"Среднее время: {avg:.4f} сек")
    print(f"Медиана: {median:.4f} сек")
    print(f"Мин: {min(times):.4f} сек")
    print(f"Макс: {max(times):.4f} сек")

def main():
    print("=" * 50)
    print("НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ MONGODB SHARDING")
    print("=" * 50)
    
    # Текущее состояние
    total = collection.count_documents({})
    print(f"\nТекущее состояние:")
    print(f"  Всего записей: {total}")
    
    # Тесты
    test_insert(10000)
    test_query_by_user_id(500)
    test_query_by_rating(500)
    
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 50)

if __name__ == "__main__":
    main()