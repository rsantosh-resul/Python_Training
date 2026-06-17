# Real-time traffic tracking
visitor_ids = set()

def track_visit(user_id):
    visitor_ids.add(user_id)  # Duplicates are automatically ignored

# Instant unique count
print(f"Unique shoppers today: {len(visitor_ids)}")